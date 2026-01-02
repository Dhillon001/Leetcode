class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dictS = {}
        dictT = {}

        for letter in s:
            if letter in dictS:
                dictS[letter] += 1
            else:
                dictS.update({letter : 1})

        for letter in t:
            if letter in dictT:
                dictT[letter] += 1
            else:
                dictT.update({letter : 1})

        if dictS == dictT:
            return True
        return False