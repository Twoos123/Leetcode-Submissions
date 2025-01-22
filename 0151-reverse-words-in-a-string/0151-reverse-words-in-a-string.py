class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        words = s.split()

        for word in words:
            stack.append(word)
        
        reverseWords = []
        while stack:
            reverseWords.append(stack.pop())
            
        return ' '.join(reverseWords)