# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        
        curr = head
        values = defaultdict(int)

        while head != None:
            values[curr.val] = curr.val
            if curr.next == None:
                return False
            curr = curr.next
            if curr.next == None:
                return False
            if curr.val not in values:
                continue
            else:
                return True
        return False