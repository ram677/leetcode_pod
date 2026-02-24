#1022. Sum of Root To Leaf Binary Numbers

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        # Helper function to perform DFS and keep track of the current path's value
        def dfs(node, current_val):
            # Base case: if we reach a null node, it contributes 0 to the sum
            if not node:
                return 0
            
            # Shift the current value left by 1 (multiply by 2) and add the node's bit
            current_val = (current_val << 1) | node.val
            
            # If this is a leaf node, return the fully constructed binary number's value
            if not node.left and not node.right:
                return current_val
            
            # Otherwise, recursively sum the values from the left and right subtrees
            return dfs(node.left, current_val) + dfs(node.right, current_val)
            
        # Start the DFS from the root with an initial value of 0
        return dfs(root, 0)
    
# Time Complexity: O(n) where n is the number of nodes in the tree, since we visit each node once.
# Space Complexity: O(h) where h is the height of the tree, due to the recursive call stack. In the worst case (skewed tree), this could be O(n).