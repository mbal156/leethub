# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next    #slow goes to one by one 
            fast=fast.next.next# fast goes to two by two
            if slow==fast:
                return True


        return False          