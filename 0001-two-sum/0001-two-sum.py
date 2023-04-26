class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, element in enumerate(nums):
            neededVal = target - element
            if(neededVal in nums and i != nums.index(neededVal)):
                return([i, nums.index(neededVal)])
        