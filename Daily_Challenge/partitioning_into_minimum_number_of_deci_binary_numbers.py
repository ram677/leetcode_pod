#1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        # Find the maximum character in the string and convert it back to an integer
        return int(max(n))
    
# Time Complexity: O(m), where m is the length of the input string n, since we need to iterate through all characters to find the maximum.
# Space Complexity: O(1), as we use only a constant amount of extra space.