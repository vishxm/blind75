# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        prev = None
        while itr is not None:
            temp = itr.next
            itr.next = prev
            prev = itr
            itr = temp
        
        return prev
