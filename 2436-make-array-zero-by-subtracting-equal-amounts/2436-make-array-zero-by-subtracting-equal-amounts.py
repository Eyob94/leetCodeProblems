class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set(nums)
        step = 0
        for i in a:
            if i != 0:
                step += 1

        return step

