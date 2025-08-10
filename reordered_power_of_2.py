#869. Reordered Power of 2

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Create signature set for all powers of 2 within the range
        power_signatures = { ''.join(sorted(str(1 << i))) for i in range(31) }
        
        # Check if n's signature exists in set
        return ''.join(sorted(str(n))) in power_signatures

#Time Complexity: O(d log d) where d is the number of digits in n, due to sorting.
#Space Complexity: O(1) since the set size is constant (only 31 powers of 2).
# Note: The solution checks if the digits of n can be rearranged to form a power of two by comparing sorted digit strings.