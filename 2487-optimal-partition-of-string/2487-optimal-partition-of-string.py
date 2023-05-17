class Solution:
    def partitionString(self, s: str) -> int:
        unique = set()
        count = 0

        for i in s:
            if i not in unique:
                unique.add(i)
            else:
                count += 1
                unique =set([i])

        return count+1