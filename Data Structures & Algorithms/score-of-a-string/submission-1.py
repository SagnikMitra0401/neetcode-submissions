class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        current_idx=0
        if len(s)==1:
            return 0
        while(current_idx<len(s)-1):
            score+=abs(ord(s[current_idx])-ord(s[current_idx+1]))
            current_idx+=1
        return score
