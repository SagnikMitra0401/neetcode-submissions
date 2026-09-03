class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=i
            s+="$pest$"
        return s

    def decode(self, s: str) -> List[str]:
        list=s.split("$pest$")
        return list[:len(list)-1]
