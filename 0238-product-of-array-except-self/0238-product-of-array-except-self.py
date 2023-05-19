class Solution:
    def mult(self, arr):
        mult = 1
        for i in arr:
            mult *= i
        return mult
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        left = 1
        right = 1

        for i in range(len(nums)):
            out[i] *= left
            out[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        
        return out