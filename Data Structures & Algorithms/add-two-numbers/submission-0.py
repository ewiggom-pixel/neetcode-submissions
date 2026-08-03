# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or carry != 0:
            if l1:
                num1 = l1.val 
            else:
                num1 = 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0
            # the math for adding two
            value = num1 + num2 + carry
            carry = value // 10
            value = value % 10
            cur.next = ListNode(value) #how to make a new list
            
            
            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        return dummy.next
            
        

