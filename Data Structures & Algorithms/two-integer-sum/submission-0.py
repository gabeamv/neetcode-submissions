class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLoc = {}
        for i in range(len(nums)):
            if target - nums[i] in numLoc:
                return [numLoc[target - nums[i]], i]
            elif nums[i] not in numLoc:
                numLoc[nums[i]] = i
        
