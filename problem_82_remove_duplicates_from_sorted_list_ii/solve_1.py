# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#### WRONG SOLUTION ####
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        search_node = head

        while current is not None:
            while search_node is not None and search_node.next is not None:
                if search_node.val == search_node.next.val:
                    search_node.next = search_node.next.next
            current.next = search_node
            search_node = search_node.next

        return dummy.next
