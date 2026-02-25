#1356. Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort the array using a custom key
        # The key is a tuple: (number of 1 bits, the integer value itself)
        # Python sorts tuples element by element, satisfying both conditions natively
        arr.sort(key=lambda x: (x.bit_count(), x))
        
        return arr

# Time Complexity: O(n log n) due to the sorting step, where n is the length of the input array.
# Space Complexity: O(1) if we ignore the space used by the sorting algorithm, otherwise O(n) due to the space used by the sorting algorithm.