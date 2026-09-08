class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(i, parts):
            # We have 4 parts
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return

            # Try taking 1, 2, or 3 digits
            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]

                # Leading zero
                if len(part) > 1 and part[0] == "0":
                    break

                # Must be <= 255
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(j + 1, parts)
                parts.pop()

        backtrack(0, [])
        return res