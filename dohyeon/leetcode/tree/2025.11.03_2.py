"""
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        root.left = self.sortedArrayToBST(nums[:mid])
        return root
    
# example usage:
nums = [-10, -3, 0, 5, 9]
solution = Solution()
bst_root = solution.sortedArrayToBST(nums)
def print_tree(node):
    """bfs traversal to print tree nodes in level order"""
    if not node:
        return []
    result = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

print(print_tree(bst_root))  # Output: [0,-3,9,-10,null,5]