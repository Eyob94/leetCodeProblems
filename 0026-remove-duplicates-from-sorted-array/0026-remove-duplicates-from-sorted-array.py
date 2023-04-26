class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]

        for i in range(len(nums)):
            print(i, len(nums))
            if i ==0:
                continue
            elif i < len(nums) and prev == nums[i]:
                nums[i] = 1000
            elif i<len(nums):
                prev=nums[i]

        nums.sort()
        x = nums.index(1000) if 1000 in nums else len(nums)
        return len(nums[:x])