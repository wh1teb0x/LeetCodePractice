# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        previous, current = dummy, head

        while current is not None:
            if current.next is not None and current.val == current.next.val:
                duplicate_value = current.val

                while current is not None and current.val == duplicate_value:
                    current = current.next

                previous.next = current

            else:
                previous = current
                current = current.next

        return dummy.next
