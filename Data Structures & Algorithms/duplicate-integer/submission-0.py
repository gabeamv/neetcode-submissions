class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for num in nums:
            if num not in dups:
                dups.add(num)
            else:
                return True
        return False