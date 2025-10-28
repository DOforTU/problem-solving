"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self._is_same_helper(p, q)
    
    def _is_same_helper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘 다 None인 경우 동일한 트리
        if not p and not q:
            return True
        # 하나만 None인 경우 동일하지 않은 트리
        if not p or not q:
            return False
        # 현재 노드의 값이 다른 경우 동일하지 않은 트리
        if p.val != q.val:
            return False
        # 왼쪽과 오른쪽 서브트리를 재귀적으로 비교
        return (self._is_same_helper(p.left, q.left) and
                self._is_same_helper(p.right, q.right))