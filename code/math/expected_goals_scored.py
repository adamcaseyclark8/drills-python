r"""TODO: port to Python.

Original JavaScript (code/math/expected-goals-scored.js):

const expectedGoalsRange = (scoredNumbers, allowedNumbers, attemptsTakenNumbers, attemptsAllowedNumbers, decay = 0.8, attemptsWeight = 0.5) => {
    const weightedStats = (numbers) => {
        const weights = numbers.map((_, index) => decay ** (numbers.length - 1 - index));
        const totalWeight = weights.reduce((sum, weight) => sum + weight, 0);
        const mean = numbers.reduce((sum, value, index) => sum + value * weights[index], 0) / totalWeight;
        const variance = numbers.reduce((sum, value, index) => sum + weights[index] * (value - mean) ** 2, 0) / totalWeight;
        return { mean, variance };
    };
    const scored = weightedStats(scoredNumbers);
    const allowed = weightedStats(allowedNumbers);
    const taken = weightedStats(attemptsTakenNumbers);
    const conceded = weightedStats(attemptsAllowedNumbers);
    const goalsExpected = (scored.mean + allowed.mean) / 2;
    const attemptsExpected = (taken.mean + conceded.mean) / 2;
    const scoringRate = taken.mean > 0 ? scored.mean / taken.mean : 0;
    const concedingRate = conceded.mean > 0 ? allowed.mean / conceded.mean : 0;
    const conversionExpected = (scoringRate + concedingRate) / 2;
    const attemptsBasedExpected = attemptsExpected * conversionExpected;
    const expected = goalsExpected * (1 - attemptsWeight) + attemptsBasedExpected * attemptsWeight;
    const spread = Math.sqrt((scored.variance + allowed.variance) / 4);
    const results = {
        low: Math.max(0, Math.floor(expected - spread)),
        high: Math.ceil(expected + spread)
    };
    return results;
};

module.exports = expectedGoalsRange;
"""
