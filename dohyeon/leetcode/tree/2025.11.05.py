"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from 
the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 만약 리프 노드라면 깊이는 1
        if not root.left and not root.right:
            return 1
        # 한쪽 자식이 없다면, 없는 쪽은 깊이에 포함하지 않음
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # 양쪽 자식이 모두 있는 경우 최소 깊이 계산
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # 양쪽 깊이 중 작은 값에 1을 더함
        return 1 + min(left_depth, right_depth)

# example test case
input_root = TreeNode(3)
input_root.left = TreeNode(9)
input_root.right = TreeNode(20)
input_root.right.left = TreeNode(15)
input_root.right.right = TreeNode(7)
solution = Solution()
print(solution.minDepth(input_root))  # Output: 2


        