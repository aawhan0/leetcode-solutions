# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        len_ = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            len_ += 1
        
        tail.next = head # creating a circle
        k%= len_ # dealing with k> len

        for i in range(len_ - k):
            tail = tail.next
        head = tail.next
        tail.next = None
        return head
            

