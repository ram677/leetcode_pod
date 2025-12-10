#3577. Count the Number of Computer Unlocking Permutations

class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        
        root_val = complexity[0]
        
        # If any computer has complexity less than or equal to the root,
        # it cannot be unlocked because the dependency chain cannot start at 0.
        for i in range(1, n):
            if complexity[i] <= root_val:
                return 0
        
        # If all computers have complexity > root, then the root (0) is a valid
        # parent for all of them. Since 0 is always processed first, any 
        # ordering of the remaining n-1 computers is valid.
        ans = 1
        for i in range(2, n):
            ans = (ans * i) % MOD
            
        return ans
    
# Time Complexity: O(n), where n is the length of the input list.
# Space Complexity: O(1), since we are using a constant amount of extra space.