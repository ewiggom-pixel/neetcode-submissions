# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next 
            
        cur = head
        while cur and cur.val == stack.pop():
            cur = cur.next
            
        return not cur

