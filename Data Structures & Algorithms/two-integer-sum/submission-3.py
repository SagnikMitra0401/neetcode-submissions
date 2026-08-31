class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr1 = []
        for minidx in range (len(nums)):
            for i in range (minidx + 1, len(nums)):
                if(nums[minidx] + nums[i] == target):
                    arr1.append(minidx)
                    arr1.append(i)
                    return arr1
        return arr1