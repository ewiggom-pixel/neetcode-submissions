# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        pali = ""

        while head:
            pali += str(head.val)
            head = head.next

        reverse = pali[::-1]

        return reverse == pali

