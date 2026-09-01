class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        nums_set=set(nums)
        for i in nums_set:
            if i-1 not in nums_set:
                current=i
                current_count=1
                while current+1 in nums_set:

                    current+=1
                    current_count+=1
                if current_count>count:
                    count=current_count
        return count