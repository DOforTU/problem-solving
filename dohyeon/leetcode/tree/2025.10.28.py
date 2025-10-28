"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Input: root = []
Output: []
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """중위 순회(Inorder Traversal)"""
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]):
        if node:
            self._inorder_helper(node.left, result) # 왼쪽 서브트리 방문
            result.append(node.val) # 왼쪽 노드가 모두 방문된 후(왼쪽 노드가 없으면) 현재 노드 방문
            self._inorder_helper(node.right, result) # 오른쪽 서브트리 방문

# example usage:
tree = TreeNode(1)
tree.right = TreeNode(3)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
print(tree.val)
solution = Solution()
print(solution.inorderTraversal(tree))  # Output: [4, 2, 5, 1, 3]