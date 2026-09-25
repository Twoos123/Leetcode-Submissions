class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:

        res = []
        
        if len(original) != m * n:
            return res

        for i in range(0, len(original), n):
            res.append(original[i: i + n])
        
        return res
