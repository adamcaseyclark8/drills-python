r"""TODO: port to Python.

Original JavaScript (code/greedy/perform-column-addition.js):

const performColumnAddition = (num1, num2) => {
    const reversedNum1 = [...num1].reverse();
    const reversedNum2 = [...num2].reverse();
    const maxLength = Math.max(reversedNum1.length, reversedNum2.length);
    let carry = 0;
    const results = [];

    for (let i = 0; i < maxLength || carry; i++) {
        const digit1 = Number(reversedNum1[i] || 0);
        const digit2 = Number(reversedNum2[i] || 0);
        const sum = digit1 + digit2 + carry;
        carry = Math.floor(sum / 10);
        results.push(sum % 10);
    }

    return results.reverse().join('');
};

module.exports = performColumnAddition;

"""
