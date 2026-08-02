# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        reversed_head, current_node = None, head

        while current_node:
            node_next = current_node.next
            current_node.next = reversed_head
            reversed_head = current_node
            current_node = node_next

        return reversed_head
