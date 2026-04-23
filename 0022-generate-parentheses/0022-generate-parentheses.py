class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def backtrack(curr, open_used, close_used):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            if open_used < n:
                backtrack(curr + "(", open_used + 1, close_used)
            
            if close_used < open_used:
                backtrack(curr + ")", open_used, close_used + 1)
        
        backtrack("", 0, 0)
        return res