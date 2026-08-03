# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        dummy=ListNode(0)
        dummy.next = head
        number = dummy
        while head:
            if head.val != 9:
                number = head
            head = head.next
        number.val += 1
        number = number.next

        while number:
            number.val = 0
            number = number.next
        
        return dummy if dummy.val else dummy.next
                
        
        
        
        
