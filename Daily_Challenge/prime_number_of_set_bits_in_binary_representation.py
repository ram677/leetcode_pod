#762. Prime Number of Set Bits in Binary Representation

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Define the set of prime numbers up to the maximum possible set bits (19)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        # Generator expression to count numbers matching the condition
        # n.bit_count() returns the number of 1s in the binary representation
        return sum(n.bit_count() in primes for n in range(left, right + 1))
    
# Time Complexity: O(N) where N is the number of integers between left and right.
# Space Complexity: O(1) since we are using a constant amount of space for the set of prime numbers.