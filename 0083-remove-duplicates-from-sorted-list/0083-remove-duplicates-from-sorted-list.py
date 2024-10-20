# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current is not None and current.next is not None:
            if current.val==current.next.val: # if current.next will be none we can not access to
                current.next=current.next.next # value so we take control at loop
            else:
                current=current.next

        return head

                
                
        
                 




