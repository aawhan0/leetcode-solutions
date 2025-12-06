# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr = []
        current = head

        while current:
            arr.append(current.val)
            current = current.next
        arr.sort()
        current = head
        i= 0
        while current:
            current.val = arr[i]
            i += 1
            current = current.next
        return head