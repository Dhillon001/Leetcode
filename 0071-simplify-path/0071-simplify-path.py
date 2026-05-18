class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        # Split by "/"
        parts = path.split("/")

        for part in parts:

            # Ignore empty strings and "."
            if part == "" or part == ".":
                continue

            # Go back one directory
            elif part == "..":
                if stack:
                    stack.pop()

            # Valid directory name
            else:
                stack.append(part)

        return "/" + "/".join(stack)