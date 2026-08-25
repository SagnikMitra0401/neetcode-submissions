class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag=False
        current=0
        if s=="":
            return(True)
        for i in s:
            if i in t[current:]:
                flag=True
                current=t.index(i,current)+1
            else:
                flag=False
                break
        return(flag)