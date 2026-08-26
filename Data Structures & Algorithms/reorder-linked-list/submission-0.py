# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = []

        curr = head
        while curr:
            temp.append(curr)
            curr = curr.next
        
        front, back = 0, len(temp) - 1

        while front < back:
            temp[front].next = temp[back]
            temp[back].next = temp[front + 1]
            front += 1
            back -= 1

        temp[front].next = None