class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pointer_s = 0

        for c in t:
            if pointer_s < len(s) and c == s[pointer_s]:
                pointer_s += 1
                
        return pointer_s == len(s)
        