#!/usr/bin/env bash
# Interview Drill Tool for JavaScript/Jest
#
# Usage:
#   ./drill.sh                        - list available problems
#   ./drill.sh random                 - pick a random problem and start it
#   ./drill.sh <category/problem>     - start a drill (back up solution, show stub + tests)
#   ./drill.sh test <category/problem> - run just that test
#   ./drill.sh show <category/problem> - print the saved solution
#   ./drill.sh reset <category/problem> - restore the saved solution
#   ./drill.sh reset-all              - restore all problems

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOLUTIONS_DIR="$SCRIPT_DIR/.solutions"
CODE_DIR="$SCRIPT_DIR/code"
TEST_DIR="$SCRIPT_DIR/test"

list_problems() {
    echo "Available problems:"
    find "$CODE_DIR" -maxdepth 2 -name "*.js" | sort | while read -r f; do
        rel="${f#$CODE_DIR/}"
        problem="${rel%.js}"
        if [[ -f "$TEST_DIR/${problem}.test.js" ]]; then
            echo "  $problem"
        fi
    done
}

drill() {
    local problem="$1"
    local src="$CODE_DIR/${problem}.js"
    local test_file="$TEST_DIR/${problem}.test.js"
    local backup="$SOLUTIONS_DIR/${problem}.js"

    if [[ ! -f "$src" ]]; then
        echo "Error: source file not found: $src" >&2
        exit 1
    fi

    # Back up original solution (only if no backup exists, to preserve original)
    mkdir -p "$(dirname "$backup")"
    if [[ ! -f "$backup" ]]; then
        cp "$src" "$backup"
        echo "Backed up solution to $backup"
    fi

    # Generate stub in place
    python3 "$SCRIPT_DIR/drill_stub.py" "$src" "$test_file" > "${src}.stub"
    mv "${src}.stub" "$src"
    echo "Stubbed $src"

    # Show the test file
    if [[ -f "$test_file" ]]; then
        echo ""
        echo "=== Test: $test_file ==="
        cat "$test_file"
    else
        echo "Warning: test file not found: $test_file"
    fi
}

run_test() {
    local problem="$1"
    local test_file="$TEST_DIR/${problem}.test.js"

    if [[ ! -f "$test_file" ]]; then
        echo "Error: test file not found: $test_file" >&2
        exit 1
    fi

    if [[ ! -d "$SCRIPT_DIR/node_modules" ]]; then
        echo "Installing dependencies..."
        (cd "$SCRIPT_DIR" && npm install)
    fi

    (cd "$SCRIPT_DIR" && npx jest "$test_file" --no-coverage)
}

show_solution() {
    local problem="$1"
    local backup="$SOLUTIONS_DIR/${problem}.js"

    if [[ ! -f "$backup" ]]; then
        echo "Error: no saved solution for '$problem'. Have you run the drill yet?" >&2
        exit 1
    fi

    cat "$backup"
}

random_drill() {
    local problems=()
    while IFS= read -r f; do
        local rel="${f#$CODE_DIR/}"
        local problem="${rel%.js}"
        if [[ -f "$TEST_DIR/${problem}.test.js" ]]; then
            problems+=("$problem")
        fi
    done < <(find "$CODE_DIR" -maxdepth 2 -name "*.js" | sort)

    if [[ ${#problems[@]} -eq 0 ]]; then
        echo "No problems found." >&2
        exit 1
    fi

    local pick="${problems[$RANDOM % ${#problems[@]}]}"
    echo "Selected: $pick"
    drill "$pick"
}

reset_all() {
    local found=0
    while IFS= read -r f; do
        local rel="${f#$CODE_DIR/}"
        local problem="${rel%.js}"
        if [[ -f "$TEST_DIR/${problem}.test.js" ]]; then
            reset_solution "$problem"
            found=1
        fi
    done < <(find "$CODE_DIR" -maxdepth 2 -name "*.js" | sort)

    if [[ $found -eq 0 ]]; then
        echo "No problems found." >&2
        exit 1
    fi
}

reset_solution() {
    local problem="$1"
    local src="$CODE_DIR/${problem}.js"
    local rel_path="code/${problem}.js"

    # Prefer restoring from git (always the real committed solution)
    if git -C "$SCRIPT_DIR" show HEAD:"$rel_path" > "$src" 2>/dev/null; then
        echo "Restored $src from git."
        return
    fi

    # Fall back to .solutions backup
    local backup="$SOLUTIONS_DIR/${problem}.js"
    if [[ ! -f "$backup" ]]; then
        echo "Error: no saved solution for '$problem'. Have you run the drill yet?" >&2
        exit 1
    fi

    cp "$backup" "$src"
    echo "Restored $src from backup."
}

# --- Main ---

if [[ $# -eq 0 ]]; then
    list_problems
    exit 0
fi

ACTION="$1"
_raw="${2:-}"
PROBLEM="${_raw#code/}"

case "$ACTION" in
    random)
        random_drill
        ;;
    test)
        if [[ $# -lt 2 ]]; then
            echo "Usage: $0 test <category/problem>" >&2
            exit 1
        fi
        run_test "$PROBLEM"
        ;;
    show)
        if [[ $# -lt 2 ]]; then
            echo "Usage: $0 show <category/problem>" >&2
            exit 1
        fi
        show_solution "$PROBLEM"
        ;;
    reset-all)
        reset_all
        ;;
    reset)
        if [[ $# -lt 2 ]]; then
            echo "Usage: $0 reset <category/problem>" >&2
            exit 1
        fi
        reset_solution "$PROBLEM"
        ;;
    *)
        # Default: treat first arg as problem name
        drill "${ACTION#code/}"
        ;;
esac
