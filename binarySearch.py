class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            midPoint = r - l // 2
            if nums[midPoint] == target:
                return midPoint
            if nums[midPoint] > target:
                r = midPoint - 1
            else:
                l = midPoint + 1
        return -1
