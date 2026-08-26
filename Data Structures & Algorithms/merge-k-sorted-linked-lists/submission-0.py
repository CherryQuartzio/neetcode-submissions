# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(list1, list2) -> Optional[ListNode]:
            dummy = ListNode()
            curr = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                
                curr = curr.next
            
            # append remaining nodes
            if list1:
                curr.next = list1
            else:
                curr.next = list2
            
            return dummy.next

        # edge case testing
        if not lists or len(lists) == 0:
            return None
        
        # we want to divide and conquer all until ended up with only one sorted list
        while len(lists) > 1:
            merged = [] # next layer

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                merged.append(mergeLists(list1, list2))

            lists = merged # replace with the next iteration layer of divide and conquer

        return lists[0]