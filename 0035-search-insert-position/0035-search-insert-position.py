class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        pos = 0

        while lo <= hi:
            mid = int((lo+hi)/2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                
                lo = mid+1
            else:
                
                hi = mid-1
        return hi + 1