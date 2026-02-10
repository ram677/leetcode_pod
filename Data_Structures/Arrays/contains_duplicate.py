#217. Contains Duplicate
from typing import List

#----------------------------------------------------------------------------------------------------
#APPROACH 1: Using a Set
#-----------------------------------------------------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result=set(nums)
        if len(result)<len(nums):
            return True
        else:
            return False
        
# Time Complexity: O(n) - We iterate through the array once to create the set.
# Space Complexity: O(n) - In the worst case, all elements are distinct and we store them in the set.

#----------------------------------------------------------------------------------------------------
#APPROACH 2: Iterative Approach (Using seen set)
#-----------------------------------------------------------------------------------------------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# Time Complexity: O(n) - We iterate through the array once.
# Space Complexity: O(n) - In the worst case, all elements are distinct and we store them in the set.

#----------------------------------------------------------------------------------------------------
#APPROACH 3: One-Liner (Length Comparison)
#-----------------------------------------------------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
# Time Complexity: O(n) - We iterate through the array once to create the set.
# Space Complexity: O(n) - In the worst case, all elements are distinct and we store them in the set.