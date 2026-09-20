class Solution:
    def isPalindrome(self, x: int) -> bool:

        if str(x)[::-1] != str(x):
            return False
        else:
            return True
        