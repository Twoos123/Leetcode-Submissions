class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverseWords = words[::-1]
        return ' '.join(reverseWords)