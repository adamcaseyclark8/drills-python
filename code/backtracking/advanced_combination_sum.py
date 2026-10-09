def perform_advanced_combination_sum(candidates, target):
    result = []
    candidates.sort()

    def dfs(start, current, remaining):
        if remaining == 0:
            result.append(list(current))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            dfs(i + 1, current, remaining - candidates[i])
            current.pop()

    dfs(0, [], target)
    return result
