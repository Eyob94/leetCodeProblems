class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        Max = 0

        while left <= right:
            pair_sum = nums[left] + nums[right]
            Max = max(Max, pair_sum)
            left+=1
            right-=1
        
        return Max
