class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=0
        flag=False

        for i in range(len(nums)):
            if (i> last):
                continue

            last=max(last,i+nums[i])

            if (last>=len(nums)-1):
                flag=True

        return(flag)