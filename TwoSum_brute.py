class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    arr = []
                    arr.append(i)
                    arr.append(j)
                    return arr
        else:
            print("No available combinations")
