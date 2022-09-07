class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        curMax = 0
        for money in nums:
            temp = curMax
            curMax = max(prevMax+money, curMax)
            prevMax = temp
        return curMax
            