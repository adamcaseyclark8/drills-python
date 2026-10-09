r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/for-loops.js):

// 5 TYPES LOOPING BEYOND STANDARD

console.log('');
console.log('--------------------------------------------------');
console.log('type 1 loop');
console.log('--------------------------------------------------');
console.log('');

// WHEN INDEX MIMICS COUNTING (TO SEE WHAT IS MISSING)
// STARTS AT 1, NOT ZERO
// USED IN: FIRST REPEATING, FIRST MISSING

const loopingTypeOne = array => {
    for (let i = 1; i < array.length; i++) {
        console.log(i);
    }
};

loopingTypeOne([1, 2, 3, 4, 5]);

console.log('');
console.log('--------------------------------------------------');
console.log('type 2 loop');
console.log('--------------------------------------------------');
console.log('');

// WHEN STARTING WITH LARGEST TO SMALLEST INDICES ()
// USED IN: STRING A REVERSE (NOT IN PLACE)

const loopingTypeTwo = array => {
    for (let i = array.length - 1; i >= 0; i--) {
        console.log(`number @ index ${i} => ${array[i]}`);
    }
};

loopingTypeTwo([1, 2, 3, 4, 5, 6, 7, 8, 9]);

console.log('');
console.log('--------------------------------------------------');
console.log('type 3 loop');
console.log('--------------------------------------------------');
console.log('');

// NESTED LOOP TO CREATE SMALLER LOOPS STARTING WITH INDEX
// USED IN:

const loopingTypeThree = array => {
    for (let i = 0; i < array.length; i++) {
        for (let j = i; j < i + 2; j++) {
            console.log(`index i => ${i}, index j => ${j}`);
        }
    }
};

loopingTypeThree([1, 2, 3, 4]);

console.log('');
console.log('--------------------------------------------------');
console.log('type 4 loop');
console.log('--------------------------------------------------');
console.log('');

// LOOP THAT INCREMENTS TO LARGER THAN ONE - MAKE LESS THAN LENGTH
// USED IN: SPLIT STRING

const loopingTypeFour = (array, interval) => {
    for (let i = 0; i < array.length; i += interval) {
        console.log(`array @ index ${i} => ` + array[i]);
    }
};

loopingTypeFour([1, 2, 3, 4, 5, 6, 7, 8, 9], 3);

console.log('');
console.log('--------------------------------------------------');
console.log('type 5 loop');
console.log('--------------------------------------------------');
console.log('');

// LOOPS THROUGH ENTIRE ARRAY THEN DECREASES THE ARRAY BY 1 FOR EACH OF THE NEXT LOOPS
// USED IN: BUBBLE SORT

const loopingTypeFive = array => {
    let count = 0;

    while (count < 2) {
        console.log('count => ' + count);
        for (let i = 0; i < array.length - count; i++) {
            console.log(`array @ index ${i} => ` + array[i]);
        }
        count++;
    }
};

loopingTypeFive([1, 2, 3, 4]);

"""
