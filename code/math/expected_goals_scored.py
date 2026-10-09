import math


def expected_goals_range(
    scored_numbers,
    allowed_numbers,
    attempts_taken_numbers,
    attempts_allowed_numbers,
    decay=0.8,
    attempts_weight=0.5,
):
    def weighted_stats(numbers):
        weights = [decay ** (len(numbers) - 1 - index) for index in range(len(numbers))]
        total_weight = sum(weights)
        mean = sum(value * weight for value, weight in zip(numbers, weights)) / total_weight
        variance = sum(weight * (value - mean) ** 2 for value, weight in zip(numbers, weights)) / total_weight
        return {'mean': mean, 'variance': variance}

    scored = weighted_stats(scored_numbers)
    allowed = weighted_stats(allowed_numbers)
    taken = weighted_stats(attempts_taken_numbers)
    conceded = weighted_stats(attempts_allowed_numbers)
    goals_expected = (scored['mean'] + allowed['mean']) / 2
    attempts_expected = (taken['mean'] + conceded['mean']) / 2
    scoring_rate = scored['mean'] / taken['mean'] if taken['mean'] > 0 else 0
    conceding_rate = allowed['mean'] / conceded['mean'] if conceded['mean'] > 0 else 0
    conversion_expected = (scoring_rate + conceding_rate) / 2
    attempts_based_expected = attempts_expected * conversion_expected
    expected = goals_expected * (1 - attempts_weight) + attempts_based_expected * attempts_weight
    spread = math.sqrt((scored['variance'] + allowed['variance']) / 4)
    return {
        'low': max(0, math.floor(expected - spread)),
        'high': math.ceil(expected + spread),
    }
