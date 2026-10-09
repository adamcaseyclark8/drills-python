#!/usr/bin/env python3
"""Generate a practice stub from a JavaScript source file.

Replaces function bodies with `throw new Error('TODO: implement');`
while preserving module.exports lines and stripping trailing comment blocks.
"""

import re
import sys


def is_function_start(line):
    """Return True if line begins a function declaration, arrow function, or class method."""
    # Regular function: function name(...) {
    if re.search(r'\bfunction\b.*\{', line):
        return True
    # Arrow function assigned to const/let/var: const name = (...) => {
    if re.search(r'\b(?:const|let|var)\b.*=.*=>\s*\{', line):
        return True
    # Class method: methodName(...) { — indented, not a control-flow keyword
    _CONTROL_FLOW = r'(?:if|else|for|while|switch|do|try|catch|finally)\b'
    if re.search(r'^\s+(?!' + _CONTROL_FLOW + r')\w+\s*\([^)]*\)\s*\{', line):
        return True
    return False


def is_module_exports(line):
    return line.strip().startswith('module.exports')


def find_export_name(lines):
    """Return the identifier a file does `module.exports = NAME;` with, or None
    if the export isn't a single simple identifier (object/class/etc.)."""
    for line in lines:
        m = re.match(r'^module\.exports\s*=\s*([A-Za-z_$][A-Za-z0-9_$]*)\s*;?\s*$', line.strip())
        if m:
            return m.group(1)
    return None


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


def find_example_call(test_path, export_name):
    """Find the first `exportName(...)` call in the associated test file (skipping
    the require() line) and return its argument text, or None if none is found."""
    if not test_path:
        return None
    try:
        with open(test_path) as f:
            content = f.read()
    except OSError:
        return None

    for m in re.finditer(re.escape(export_name) + r'\s*\(', content):
        line_start = content.rfind('\n', 0, m.start()) + 1
        line_end = content.find('\n', m.start())
        line = content[line_start:line_end if line_end != -1 else len(content)]
        if 'require(' in line:
            continue
        args = _extract_balanced_parens(content, m.end() - 1)
        if args is not None:
            return re.sub(r'\s+', ' ', args).strip()
    return None


def stub_js_file(path, test_path=None):
    with open(path) as f:
        lines = f.readlines()

    output = []
    i = 0
    while i < len(lines):
        line = lines[i]

        if is_module_exports(line):
            output.append(line)
            i += 1
            continue

        if is_function_start(line):
            output.append(line)
            i += 1
            # Count braces to find end of function body
            depth = line.count('{') - line.count('}')
            body_lines = []
            while i < len(lines) and depth > 0:
                body_lines.append(lines[i])
                depth += lines[i].count('{') - lines[i].count('}')
                i += 1
            # Emit stub body instead of real body
            output.append("    throw new Error('TODO: implement');\n")
            # Emit the closing brace line (depth hit 0 on the last body line)
            if body_lines:
                closing = body_lines[-1]
                # Strip everything except the closing brace and trailing chars
                stripped = closing.rstrip()
                # Find the last } and emit just that
                idx = stripped.rfind('}')
                if idx != -1:
                    output.append(stripped + '\n')
            continue

        output.append(line)
        i += 1

    # Strip trailing comment blocks (lines that start with //)
    while output and output[-1].strip().startswith('//'):
        output.pop()

    # Append a runnable driver so `node <file>.js` works with no manual edits,
    # using the same call the associated test makes. Skipped for class exports
    # (calling a class like a function throws) and anything already stubbed.
    export_name = find_export_name(lines)
    is_class_export = export_name and any(re.match(r'^class\s+' + re.escape(export_name) + r'\b', l.strip()) for l in lines)
    already_has_runner = any('require.main' in l for l in output)
    if export_name and not is_class_export and not already_has_runner:
        args = find_example_call(test_path, export_name)
        if args is not None:
            output.append('\n')
            output.append('if (require.main === module) {\n')
            output.append(f'    console.log({export_name}({args}));\n')
            output.append('}\n')

    # Normalize to single trailing newline
    content = ''.join(output).rstrip('\n') + '\n'
    return content


if __name__ == '__main__':
    if len(sys.argv) not in (2, 3):
        print(f'Usage: {sys.argv[0]} <file.js> [test_file.js]', file=sys.stderr)
        sys.exit(1)
    test_path = sys.argv[2] if len(sys.argv) == 3 else None
    print(stub_js_file(sys.argv[1], test_path), end='')
