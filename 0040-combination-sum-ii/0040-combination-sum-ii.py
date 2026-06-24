class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(start, remaining, path):

            if remaining == 0:
                res.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                # i + 1 because each number can be used once
                backtrack(i + 1,
                          remaining - candidates[i],
                          path)

                path.pop()

        backtrack(0, target, [])

        return res