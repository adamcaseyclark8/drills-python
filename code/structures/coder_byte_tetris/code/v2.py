r"""TODO: port to Python.

Original JavaScript (code/structures/coder-byte-tetris/code/v2.js):

// tetris.js

const SHAPES = {
    I: [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3]
    ],
    O: [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ],
    T: [
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 1]
    ],
    S: [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 2]
    ],
    Z: [
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 1]
    ],
    J: [
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 2]
    ],
    L: [
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 0]
    ]
};
//     o
// o o o

function rotateShape(shape) {
    const rotated = shape.map(([row, col]) => [col, -row]);
    const minRow = Math.min(...rotated.map(([r, c]) => r));
    const minCol = Math.min(...rotated.map(([r, c]) => c));
    return rotated.map(([r, c]) => [r - minRow, c - minCol]);
}

function getAllRotations(shape) {
    const rotations = [];
    const seen = new Set();
    let current = shape;

    for (let i = 0; i < 4; i++) {
        const key = JSON.stringify(current.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]));
        if (!seen.has(key)) {
            rotations.push(JSON.parse(JSON.stringify(current)));
            seen.add(key);
        }
        current = rotateShape(current);
    }

    return rotations;
}

function clearAllCompleteRows(heights) {
    const newHeights = [...heights];
    let totalCleared = 0;

    while (true) {
        const minHeight = Math.min(...newHeights);
        if (minHeight === 0) break;

        const rowComplete = newHeights.every(h => h >= minHeight);
        if (rowComplete) {
            totalCleared++;
            for (let i = 0; i < newHeights.length; i++) {
                newHeights[i]--;
            }
        } else {
            break;
        }
    }

    return { heights: newHeights, cleared: totalCleared };
}

function placeShapeOnHeights(heights, shape, startCol) {
    const maxShapeCol = Math.max(...shape.map(([r, c]) => c));

    if (startCol < 0 || startCol + maxShapeCol >= heights.length) {
        return null;
    }

    let dropHeight = -Infinity;
    for (const [row, col] of shape) {
        const targetCol = startCol + col;
        dropHeight = Math.max(dropHeight, heights[targetCol] - row);
    }

    const newHeights = [...heights];
    for (const [row, col] of shape) {
        const targetCol = startCol + col;
        const blockTop = dropHeight + row + 1;
        newHeights[targetCol] = Math.max(newHeights[targetCol], blockTop);
    }

    return newHeights;
}

function getMaxNumberOfRowsCleared(heights, shapeName) {
    const shape = SHAPES[shapeName];
    if (!shape) {
        throw new Error(`Invalid shape: ${shapeName}`);
    }

    // First, clear any existing complete rows
    const { heights: clearedHeights } = clearAllCompleteRows(heights);

    let maxCleared = 0;
    const rotations = getAllRotations(shape);

    for (const rotation of rotations) {
        for (let col = 0; col < heights.length; col++) {
            const newHeights = placeShapeOnHeights(clearedHeights, rotation, col);

            if (newHeights !== null) {
                const { cleared } = clearAllCompleteRows(newHeights);
                maxCleared = Math.max(maxCleared, cleared);
            }
        }
    }

    return maxCleared;
}

module.exports = {
    getMaxNumberOfRowsCleared,
    placeShapeOnHeights,
    clearAllCompleteRows,
    getAllRotations,
    SHAPES
};

"""
