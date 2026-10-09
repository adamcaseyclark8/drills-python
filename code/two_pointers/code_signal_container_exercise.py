r"""TODO: port to Python.

Original JavaScript (code/two-pointers/code-signal-container-exercise.js):

const codeSignalContainerExercise = queries => {
    const valueSet = new Set();
    const values = [];
    const results = [];

    for (let i = 0; i < queries.length; i++) {
        const [operation, valueStr] = queries[i];
        const value = parseInt(valueStr);

        switch (operation) {
            case 'ADD': {
                if (!valueSet.has(value)) {
                    valueSet.add(value);
                    let inserted = false;
                    for (let j = 0; j < values.length; j++) {
                        if (values[j] > value) {
                            values.splice(j, 0, value);
                            inserted = true;
                            break;
                        }
                    }
                    if (!inserted) {
                        values.push(value);
                    }
                }
                results.push('');
                break;
            }
            case 'REMOVE': {
                const existed = valueSet.has(value);
                if (existed) {
                    valueSet.delete(value);
                    const index = values.indexOf(value);
                    if (index !== -1) {
                        values.splice(index, 1);
                    }
                }
                results.push(existed.toString());
                break;
            }
            case 'EXISTS': {
                results.push(valueSet.has(value).toString());
                break;
            }
            case 'NEXT_UP': {
                let nextValue = '';
                for (let j = 0; j < values.length; j++) {
                    if (values[j] > value) {
                        nextValue = values[j].toString();
                        break;
                    }
                }
                results.push(nextValue);
                break;
            }
            default: {
                results.push('');
                break;
            }
        }
    }
    return results;
};

module.exports = codeSignalContainerExercise;

"""
