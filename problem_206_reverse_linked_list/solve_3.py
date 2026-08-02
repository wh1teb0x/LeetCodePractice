# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        return self.reverseListHelper(head)

    def reverseListHelper(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if node is None or node.next is None:
            return node

        reversed_head = self.reverseListHelper(node.next)

        next_node = node.next
        next_node.next = node
        node.next = None

        return reversed_head
