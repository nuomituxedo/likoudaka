class Solution:
    ### binary search
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while (left <= right):
            if nums[left] == target:
                return left
            elif nums[left] < target:
                left += 1
            if nums[right] == target:
                return right
            elif nums[right] > target:
                right -= 1
        return -1