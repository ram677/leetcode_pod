#1339. Maximum Product of Splitted Binary Tree

from typing import Optional

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum product of sums of two subtrees formed by removing one edge.
        The result is returned modulo 10^9 + 7.
        """
      
        def calculate_total_sum(node: Optional[TreeNode]) -> int:
            """
            Calculate the sum of all node values in the tree.
          
            Args:
                node: The root of the tree/subtree
              
            Returns:
                The sum of all node values in the tree rooted at 'node'
            """
            if node is None:
                return 0
          
            # Recursively sum current node value with left and right subtree sums
            return node.val + calculate_total_sum(node.left) + calculate_total_sum(node.right)
      
        def find_max_product(node: Optional[TreeNode]) -> int:
            """
            Traverse the tree and find the maximum product by trying each possible edge removal.
          
            Args:
                node: The current node being processed
              
            Returns:
                The sum of the subtree rooted at 'node'
            """
            if node is None:
                return 0
          
            # Calculate the sum of the current subtree
            subtree_sum = node.val + find_max_product(node.left) + find_max_product(node.right)
          
            # Update the maximum product if we remove the edge above this node
            # One part has sum 'subtree_sum', the other has sum 'total_sum - subtree_sum'
            nonlocal max_product, total_sum
            if subtree_sum < total_sum:  # Ensure we don't count the entire tree
                max_product = max(max_product, subtree_sum * (total_sum - subtree_sum))
          
            return subtree_sum
      
        # Constants and initialization
        MOD = 10**9 + 7
      
        # First pass: calculate the total sum of all nodes
        total_sum = calculate_total_sum(root)
      
        # Initialize the maximum product
        max_product = 0
      
        # Second pass: find the maximum product by trying each edge removal
        find_max_product(root)
      
        # Return the result modulo MOD
        return max_product % MOD

# Time Complexity: O(N), where N is the number of nodes in the tree.
# Space Complexity: O(H), where H is the height of the tree due to recursion stack.