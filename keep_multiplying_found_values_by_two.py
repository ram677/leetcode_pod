#2154. Keep Multiplying Found Values by Two

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        
        while original in num_set:
            original *= 2
            
        return original
    
# Time Complexity: O(n), where n is the number of elements in nums.
# Space Complexity: O(n), due to the storage of elements in the set.