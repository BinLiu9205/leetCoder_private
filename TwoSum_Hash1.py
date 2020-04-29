class Solution:
    def twoSum(self, nums: List[int], target: int):
        sumDict = {}
        for i in range(len(nums)):
            if target-nums[i] not in sumDict:
                sumDict[nums[i]] = i
            else:
                return [sumDict[target-nums[i]],i]
