r"""TODO: port to Python.

Original JavaScript (code/arrays/filter-all-prime-numbers.js):

const filterAllPrimeNumbers = array => {
    const isPrimeNumber = number => {
        if (number < 2) return false;
        for (let i = 2; i <= Math.sqrt(number); i++) {
            if (number % i === 0) return false;
        }
        return true;
    };
    return array.filter(isPrimeNumber);
};

module.exports = filterAllPrimeNumbers;

"""
