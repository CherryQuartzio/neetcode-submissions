# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy

        for i in range(n + 1):
            if right:
                right = right.next
        
        # shift two pointers until right is at None
        while right:
            left = left.next
            right = right.next
        
        # delete
        left.next = left.next.next

        return dummy.next