class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        found_idx=0
        current_idx=0
        if len(t)==0:
            return 0
        while (current_idx<len(s)):
            if(found_idx==len(t)):
                break
            if t[found_idx] in s[current_idx:]:
                reference_idx=s.find(t[found_idx],current_idx)
                if(reference_idx>=0):
                    found_idx+=1 
                    current_idx=reference_idx    
            current_idx+=1
        if(len(t)>=found_idx):
            return(len(t)-found_idx)
        else:
            return found_idx
