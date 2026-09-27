class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        boat = 0

        people.sort()

        while l <= r:
            if l < r and people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boat += 1

        return boat


    

        