#!/usr/bin/env python3
"""Generate a practice stub from a Python source file.

Replaces function and method bodies with `raise NotImplementedError('TODO: implement')`
while keeping imports, constants and signatures, and stripping trailing comment blocks.
"""

import ast
import re
import sys

STUB_BODY = "raise NotImplementedError('TODO: implement')"


def signature_end(lines, node):
    """Return the 0-based index of the line holding the colon that ends a def's signature."""
    depth = 0
    for i in range(node.lineno - 1, node.body[0].lineno - 1):
        code = lines[i].split('#', 1)[0].rstrip()
        depth += sum(code.count(c) for c in '([{') - sum(code.count(c) for c in ')]}')
        if depth == 0 and code.endswith(':'):
            return i
    return node.lineno - 1


def functions_to_stub(tree):
    """Top-level functions plus the methods of top-level classes."""
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            yield node
        elif isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    yield item


def find_exported_names(test_path, module_path):
    """Names the test file imports from the module under test, in import order."""
    if not test_path:
        return []
    try:
        with open(test_path) as f:
            tree = ast.parse(f.read())
    except (OSError, SyntaxError):
        return []

    module = module_path.removesuffix('.py').replace('/', '.')
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and module.endswith(node.module):
            names.extend(alias.name for alias in node.names)
    return names


def _extract_balanced_parens(text, open_paren_idx):
    """text[open_paren_idx] must be '('. Returns the text between the matching
    parens, or None if unbalanced."""
    depth = 0
    for i in range(open_paren_idx, len(text)):
        if text[i] == '(':
            depth += 1
        elif text[i] == ')':
            depth -= 1
            if depth == 0:
                return text[open_paren_idx + 1:i]
    return None


def find_example_call(test_path, function_name):
    """Find the first `function_name(...)` call in the associated test file whose
    arguments are all literals (so it runs on its own) and return its argument
    text, or None if none is found."""
    if not test_path:
        return None
    try:
        with open(test_path) as f:
            content = f.read()
    except OSError:
        return None

    for m in re.finditer(r'\b' + re.escape(function_name) + r'\s*\(', content):
        line_start = content.rfind('\n', 0, m.start()) + 1
        line = content[line_start:content.find('\n', m.start())]
        if line.lstrip().startswith(('import ', 'from ', 'def ', '#')):
            continue
        args = _extract_balanced_parens(content, m.end() - 1)
        if args is None:
            continue
        args = re.sub(r'\s+', ' ', args).strip().rstrip(',')
        try:
            ast.literal_eval(f'({args},)')
        except (ValueError, SyntaxError):
            continue
        return args
    return None


def stub_py_file(path, test_path=None):
    with open(path) as f:
        source = f.read()
    lines = source.splitlines(keepends=True)
    tree = ast.parse(source)

    # Replace each body with the stub, working bottom-up so earlier line numbers stay valid
    stubs = []
    for node in functions_to_stub(tree):
        start = signature_end(lines, node) + 1
        indent = re.match(r'\s*', lines[node.body[0].lineno - 1]).group(0)
        stubs.append((start, node.end_lineno, f'{indent}{STUB_BODY}\n'))
    for start, end, stub in sorted(stubs, reverse=True):
        lines[start:end] = [stub]

    output = lines

    # Strip trailing comment blocks (lines that start with #) and blank lines
    while output and (not output[-1].strip() or output[-1].lstrip().startswith('#')):
        output.pop()

    # Append a runnable driver so `python <file>.py` works with no manual edits,
    # using the same call the associated test makes. Skipped for classes
    # (there's no single call to make) and anything that already has a runner.
    defined_functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}
    already_has_runner = any('__name__' in line and '__main__' in line for line in output)
    if not already_has_runner:
        # Prefer the function the file is named after over helpers it also exports
        stem = path.rsplit('/', 1)[-1].removesuffix('.py')
        names = sorted(find_exported_names(test_path, path), key=lambda name: name not in stem)
        for name in names:
            if name not in defined_functions:
                continue
            args = find_example_call(test_path, name)
            if args is not None:
                output.append('\n\n')
                output.append("if __name__ == '__main__':\n")
                output.append(f'    print({name}({args}))\n')
                break

    # Normalize to single trailing newline
    return ''.join(output).rstrip('\n') + '\n'


if __name__ == '__main__':
    if len(sys.argv) not in (2, 3):
        print(f'Usage: {sys.argv[0]} <file.py> [test_file.py]', file=sys.stderr)
        sys.exit(1)
    test_path = sys.argv[2] if len(sys.argv) == 3 else None
    print(stub_py_file(sys.argv[1], test_path), end='')
