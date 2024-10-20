# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list2 is None :
            return list1
        if list1 is None:
            return list2
        
        node2=ListNode()
        tail=node2
            
        while list1 is not None and list2 is not None:
                
                if list1.val>=list2.val :
                    tail.next=list2
                    list2=list2.next    
                else:
                    tail.next=list1
                    list1=list1.next

                tail=tail.next


                if list1 is not None:
                    tail.next=list1

                if list2 is not None:
                    tail.next=list2


        return node2.next # if we return just "node2" we have  extra "0" at
                            # the beginning                





                               
                
        