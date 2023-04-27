class Solution:
    def minTimeToType(self, word: str) -> int:
        curr, time = 97, 0
        for i in word:
            if curr > ord(i):
                time += min(abs(ord(i)-curr),abs(ord(i)-curr+26) )
                
            else:
                time += min(abs(ord(i)-curr), abs(ord(i)-curr-26))
            curr = ord(i)
                
        return time+len(word)
