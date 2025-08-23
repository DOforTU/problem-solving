# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 이전 노드를 저장하는 포인터. 초기값은 None
        prev = None
        # 현재 노드를 가리키는 포인터. 초기값은 head
        current = head

        # 현재 노드가 None이 될 때까지 반복
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        return prev


print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))