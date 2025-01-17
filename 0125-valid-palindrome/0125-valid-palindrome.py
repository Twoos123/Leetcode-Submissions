class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            if not self.alphaNum(s[l]): 
                l += 1
                continue
            if not self.alphaNum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c: str) -> bool:
        return (("a" <= c.lower() <= "z") or ("0" <= c <= "9"))