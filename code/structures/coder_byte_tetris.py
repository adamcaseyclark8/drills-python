SHAPES = {
    'I': [[0, 0], [0, 1], [0, 2], [0, 3]],
    'O': [[0, 0], [0, 1], [1, 0], [1, 1]],
    'T': [[0, 0], [0, 1], [0, 2], [1, 1]],
    'S': [[0, 0], [0, 1], [1, 1], [1, 2]],
    'Z': [[0, 1], [0, 2], [1, 0], [1, 1]],
    'J': [[0, 0], [0, 1], [0, 2], [1, 0]],
    'L': [[0, 0], [0, 1], [0, 2], [1, 2]],
}


def rotate_shape(shape):
    rotated = [[col, -row] for row, col in shape]
    min_row = min(r for r, c in rotated)
    min_col = min(c for r, c in rotated)
    return [[r - min_row, c - min_col] for r, c in rotated]


def get_all_rotations(shape):
    rotations = []
    seen = set()
    current = shape

    for _ in range(4):
        key = tuple(sorted(tuple(cell) for cell in current))
        if key not in seen:
            rotations.append([list(cell) for cell in current])
            seen.add(key)
        current = rotate_shape(current)

    return rotations


def place_shape_on_heights(heights, shape, start_col):
    max_shape_col = max(c for r, c in shape)

    if start_col < 0 or start_col + max_shape_col >= len(heights):
        return None

    # Find drop height
    drop_height = float('-inf')
    for row, col in shape:
        target_col = start_col + col
        drop_height = max(drop_height, heights[target_col] - row)

    # Place blocks
    new_heights = list(heights)
    for row, col in shape:
        target_col = start_col + col
        block_top = drop_height + row + 1
        new_heights[target_col] = max(new_heights[target_col], block_top)

    return new_heights


def count_complete_rows(heights):
    if len(heights) == 0 or min(heights) == 0:
        return 0

    rows_cleared = 0
    current_heights = list(heights)

    while True:
        min_height = min(current_heights)
        if min_height == 0:
            break

        # Check if bottom-most row is complete
        row_complete = all(h >= min_height for h in current_heights)

        if row_complete:
            # Clear this row
            rows_cleared += 1
            current_heights = [h - 1 for h in current_heights]
        else:
            break

    return rows_cleared


def get_max_number_of_rows_cleared(heights, shape_name):
    shape = SHAPES.get(shape_name)
    if not shape:
        raise ValueError(f'Invalid shape: {shape_name}')

    max_cleared = 0
    rotations = get_all_rotations(shape)

    for rotation in rotations:
        for col in range(len(heights)):
            new_heights = place_shape_on_heights(heights, rotation, col)

            if new_heights is not None:
                cleared = count_complete_rows(new_heights)
                max_cleared = max(max_cleared, cleared)

    return max_cleared
