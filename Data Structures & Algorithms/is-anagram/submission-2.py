class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i] = s.count(i)
        dict2={}
        for i in t:
            if i not in dict2:
                dict2[i] = t.count(i)
        return dict1==dict2
