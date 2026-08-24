class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Max=-1

        for i in range(len(arr)-1,-1,-1):
            current = arr[i]
            arr[i] = Max
            Max = max(Max,current)
        arr[len(arr)-1]=-1
        return arr