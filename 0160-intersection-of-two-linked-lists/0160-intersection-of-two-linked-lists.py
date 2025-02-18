# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lA,lB=headA,headB
        
        while lA!=lB:  # la ve lb eşit olana kadar devam eder ayrıca ikisi none olduğunda da döngü biter(When Both la and lb is equal ,the lap ends .Also both of them will be None then it ends  )

            if lA:
                lA=lA.next  # iki liste aynı uzunlukta olmadığı için la none olduğunda headb yani listB nin başı olur.lb içinde aynı şekilde  
            else:
                lA=headB        
            if lB:
                lB=lB.next    
            else:
                lB=headA

        return lA        


        