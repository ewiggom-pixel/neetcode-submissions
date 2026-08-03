# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        result = []
        curr = head

        if not curr:
            return 0

        while curr:
            result.append(curr.val)
            curr = curr.next

        R = len(result) - 1
        answer = 0 
        L = 0

        for i in range(len(result)//2):
            num = result[L] + result[R]
            L += 1
            R -=1
            answer = max(answer, num)

        return answer
        