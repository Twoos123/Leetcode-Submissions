class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        seen = set(nums)
        res = []

        for n in range(1, len(nums) + 1):
            if n not in seen:
                res.append(n)
        return res