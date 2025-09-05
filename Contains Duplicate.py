
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present = {}
        for n in nums:
            if present.get(n, 0) == 1:
                return True
            present[n] = 1
        
        return False
