class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # If it's a closing bracket
            if ch in close_to_open:
                # Stack must not be empty AND top must match
                if stack and stack[-1] == close_to_open[ch]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket → push
                stack.append(ch)

        # Valid only if stack is empty at the end
        return len(stack) == 0
