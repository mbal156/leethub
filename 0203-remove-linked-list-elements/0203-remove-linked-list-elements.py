# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        while head and head.val == val:     
            head = head.next                
        temp=head               
        prev=None
        while temp:           
            if temp.val == val:
                prev.next = temp.next
                  # pyhton için gerekli değil çünkü garbage collector var 
            else:
                prev = temp
            temp = temp.next
        
        return head

        
