from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self._check_balance(root) != -1
    
    def _check_balance(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        """
        후위 순회: 현재 노드의 높이를 계산하기 전에, 왼쪽 서브트리와 오른쪽 서브트리를 먼저 재귀적으로 호출하여 검사
        만약 왼쪽 서브트리(left_height)나 오른쪽 서브트리(right_height) 중 하나라도 $-1$을 반환했다면, 
        이는 이미 전체 트리가 균형을 잃었다는 의미
        """
        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1  # 왼쪽 서브트리가 균형이 맞지 않음
        
        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1  # 오른쪽 서브트리가 균형이 맞지 않음
        

        """
        이진 트리가 균형 잡혀있으려면, 모든 노드에 대해 왼쪽 서브트리의 높이와 오른쪽 서브트리의 높이 차이가 1 이하여야 한다.
        """
        if abs(left_height - right_height) > 1:
            return -1  # 현재 노드에서 균형이 맞지 않음
        
        """
        위의 모든 검사를 통과했다면, 현재 노드를 루트로 하는 서브트리는 균형이 잡혀있으며,
        이때 현재 노드의 높이는 왼쪽과 오른쪽 서브트리 높이 중 더 큰 값에 1 (현재 노드 자신)을 더한 값이 된다.
        """
        return max(left_height, right_height) + 1  # 현재 노드의 높이 반환