class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty=[]
        for i in nums:
            if i not in empty:
                empty.append(i)
            else:
                return True
        return False
        