# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        curr = head
        prev = curr
        
        
        while curr:
            for i in range(m-1):
                if not curr:
                    return head 
                curr = curr.next
            prev = curr

            if not curr:
                break 

            for i in range(n+1):
                if not curr:
                    break
                curr = curr.next

            prev.next = curr
        return head

            
