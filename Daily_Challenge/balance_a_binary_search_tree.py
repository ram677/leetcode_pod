#1382. Balance a Binary Search Tree

class Solution:
  def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
    nums = []

    def inorder(root: TreeNode | None) -> None:
      if not root:
        return
      inorder(root.left)
      nums.append(root.val)
      inorder(root.right)

    inorder(root)

    # Same as 108. Convert Sorted Array to Binary Search Tree
    def build(l: int, r: int) -> TreeNode | None:
      if l > r:
        return None
      m = (l + r) // 2
      return TreeNode(nums[m],
                      build(l, m - 1),
                      build(m + 1, r))

    return build(0, len(nums) - 1)

# Time Complexity: O(n) - We traverse the tree once to get the sorted values and then build a balanced BST in O(n).
# Space Complexity: O(n) - We store the values of the nodes in a list, and the recursive call stack can go up to O(n) in the worst case (if the tree is skewed).