class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        return (sum(bool(x) for x in counter.keys()))
        

