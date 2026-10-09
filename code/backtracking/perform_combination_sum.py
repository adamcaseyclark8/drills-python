def perform_combination_sum(candidates, target):
    results = []

    def backtrack(remaining, path, start):
        if remaining == 0:
            results.append(list(path))
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                continue
            path.append(candidates[i])
            backtrack(remaining - candidates[i], path, i)
            path.pop()

    backtrack(target, [], 0)
    return results
