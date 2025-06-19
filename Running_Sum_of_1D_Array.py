class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        S = 0
        running_Sum = []
        for i in range(n):
            S = S + nums[i]
            running_Sum.append(S)
        return running_Sum
