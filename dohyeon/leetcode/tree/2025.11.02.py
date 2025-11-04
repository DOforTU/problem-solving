"""
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. 
Return the answer in any order."""

from typing import Deque, List, Optional

from pyparsing import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 입력 n이 0이면 빈 리스트 반환
        if n == 0:
            return []
        
        # 1부터 n까지의 노드를 사용하여 트리를 생성하는 헬퍼 함수 호출
        print(self._serialize_trees(self._generate_bst(1, n)))  # 디버깅용 출력
        return self._generate_bst(1, n)

    def _generate_bst(self, start: int, end: int) -> List[Optional[TreeNode]]:
        all_trees = []
        
        # 1. 기저 사례 (Base Case): 서브트리 범위가 유효하지 않을 때
        # start > end: 노드가 없는 빈 서브트리를 의미하며, 이를 None으로 표현하여 반환합니다.
        if start > end:
            all_trees.append(None)
            return all_trees
        
        # 2. 재귀 단계 (Recursive Step): start부터 end까지의 각 숫자를 루트로 시도
        for i in range(start, end + 1):
            # 현재 숫자 i를 루트 노드 값으로 설정
            
            # 왼쪽 서브트리 생성 (값 범위: start ~ i-1)
            left_trees = self._generate_bst(start, i - 1)
            
            # 오른쪽 서브트리 생성 (값 범위: i+1 ~ end)
            right_trees = self._generate_bst(i + 1, end)
            
            # 3. 조합 (Combination): 모든 왼쪽 서브트리와 오른쪽 서브트리의 조합을 현재 루트에 연결
            for left in left_trees:
                for right in right_trees:
                    # 새로운 루트 노드 생성
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    all_trees.append(root)
        
        return all_trees
    
    def _serialize_trees(self, trees: List[Optional[TreeNode]]) -> List[List[Optional[int]]]:
        """모든 트리를 직렬화하여 리스트의 리스트로 반환(디버깅용)"""
        serialized_results: List[List[Optional[int]]] = []
        
        # trees 리스트의 각 트리를 직렬화합니다.
        for root in trees:
            if not root:
                continue
                
            queue: Deque[Optional[TreeNode]] = deque([root])
            serialized_list: List[Optional[int]] = []
            
            while queue:
                node = queue.popleft()
                
                if node:
                    serialized_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    serialized_list.append(None)

            # 트리의 맨 뒤에 있는 불필요한 None 제거 (꼬리 정리)
            while serialized_list and serialized_list[-1] is None:
                serialized_list.pop()
                
            serialized_results.append(serialized_list)
            
        return serialized_results


# Example usage:
solution = Solution()
result = solution.generateTrees(3)