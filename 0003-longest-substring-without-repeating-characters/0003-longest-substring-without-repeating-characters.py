class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        path = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in path:
                path.remove(s[l])
                l += 1
            path.add(s[r])
            result = max(result, len(path))
        return result

