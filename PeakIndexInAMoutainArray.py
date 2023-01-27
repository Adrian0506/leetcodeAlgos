class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            midPoint = (l + r) // 2
            if arr[midPoint] > arr[midPoint - 1] and arr[midPoint] > arr[midPoint + 1]:
                return midPoint
            if arr[midPoint] > arr[midPoint - 1]:
                l += 1
            if arr[midPoint] > arr[midPoint + 1]:
                r -= 1
        return -1
            
