class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [0 for _ in range(len(nums))]
        postfixProd = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            prefixProd[i] = nums[i] * prefixProd[i-1] if i - 1 >= 0 else nums[i]
        for i in range(len(nums) - 1, -1, -1):
            postfixProd[i] = nums[i] * postfixProd[i+1] if i + 1 <= len(nums) - 1 else nums[i]
        ret = []
        for i in range(len(nums)):
            prefixLeft = prefixProd[i-1] if i-1 >= 0 else 1
            postfixRight = postfixProd[i+1] if i+1 <= len(nums) - 1 else 1
            ret.append(prefixLeft * postfixRight)
        return ret
        