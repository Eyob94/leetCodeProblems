class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                if target in i:
                    return True
                else:
                    return False