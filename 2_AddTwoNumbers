# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Convert l1 and l2 to numbers
        num1, num2 = "", ""
        
        while (l1):
            num1 += str(l1.val)
            l1 = l1.next
            
        while (l2):
            num2 += str(l2.val)
            l2 = l2.next
        
        # Add the numbers
        res = int(num1[::-1]) + int(num2[::-1])
        res = list(str(res))
        res.reverse()
        
        # Convert num3 to a linked list
        head = ListNode()
        cur = head
        
        for i in range(len(res)):
            digit = res[i]
            cur.val = int(digit)
            if (i+1 >= len(res)):
                break
            cur.next = ListNode(-1)
            cur = cur.next
        
        return head
            