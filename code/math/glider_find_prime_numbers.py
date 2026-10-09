r"""TODO: port to Python.

Original JavaScript (code/math/glider-find-prime-numbers.js):

const isNumberPrime = num => {
    // Numbers less than or equal to 1 are not prime
    if (num <= 1) {
        return 'No';
    }

    // 2 is the only even prime number
    if (num === 2) {
        return 'Yes';
    }

    // Even numbers greater than 2 are not prime
    if (num % 2 === 0) {
        return 'No';
    }

    // Check for divisibility from 3 up to the square root of the number,
    // incrementing by 2 to only check odd divisors
    for (let i = 3; i * i <= num; i += 2) {
        // console.log(i)
        // console.log(`${i * i} <= ${num}`)
        // console.log(`${num} / ${i}?`)
        if (num % i === 0) {
            return 'No'; // Found a divisor, so it's not prime
        }
    }

    return 'Yes'; // No divisors found, so it's prime
};

module.exports = isNumberPrime;

// console.log(isNumberPrime(99))

"""
