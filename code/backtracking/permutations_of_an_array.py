def permutations_of_an_array(nums):
    results = []

    def backtrack(path, remaining):
        if len(remaining) == 0:
            results.append(list(path))
            return

        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1:])
            path.pop()

    backtrack([], nums)
    return results
