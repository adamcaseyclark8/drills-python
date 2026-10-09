# tetris.py

SHAPES = {
    'I': [[0, 0], [0, 1], [0, 2], [0, 3]],
    'O': [[0, 0], [0, 1], [1, 0], [1, 1]],
    'T': [[0, 0], [0, 1], [0, 2], [1, 1]],
    'S': [[0, 0], [0, 1], [1, 1], [1, 2]],
    'Z': [[0, 1], [0, 2], [1, 0], [1, 1]],
    'J': [[0, 0], [0, 1], [0, 2], [1, 2]],
    'L': [[0, 0], [0, 1], [0, 2], [1, 0]],
}
#     o
# o o o


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


def clear_all_complete_rows(heights):
    new_heights = list(heights)
    total_cleared = 0

    while True:
        min_height = min(new_heights)
        if min_height == 0:
            break

        row_complete = all(h >= min_height for h in new_heights)
        if row_complete:
            total_cleared += 1
            for i in range(len(new_heights)):
                new_heights[i] -= 1
        else:
            break

    return {'heights': new_heights, 'cleared': total_cleared}


def place_shape_on_heights(heights, shape, start_col):
    max_shape_col = max(c for r, c in shape)

    if start_col < 0 or start_col + max_shape_col >= len(heights):
        return None

    drop_height = float('-inf')
    for row, col in shape:
        target_col = start_col + col
        drop_height = max(drop_height, heights[target_col] - row)

    new_heights = list(heights)
    for row, col in shape:
        target_col = start_col + col
        block_top = drop_height + row + 1
        new_heights[target_col] = max(new_heights[target_col], block_top)

    return new_heights


def get_max_number_of_rows_cleared(heights, shape_name):
    shape = SHAPES.get(shape_name)
    if not shape:
        raise ValueError(f'Invalid shape: {shape_name}')

    # First, clear any existing complete rows
    cleared_heights = clear_all_complete_rows(heights)['heights']

    max_cleared = 0
    rotations = get_all_rotations(shape)

    for rotation in rotations:
        for col in range(len(heights)):
            new_heights = place_shape_on_heights(cleared_heights, rotation, col)

            if new_heights is not None:
                cleared = clear_all_complete_rows(new_heights)['cleared']
                max_cleared = max(max_cleared, cleared)

    return max_cleared
