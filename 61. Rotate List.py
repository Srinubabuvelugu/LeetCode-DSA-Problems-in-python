# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        n = 1
        if not head or k == 0:
            return head
        while temp.next:
            temp = temp.next
            n+=1 # length of linked list
        if n == 1:
            return head
        k = k % n
        k = n - k
        temp2 = head
        while k > 0:
            val = temp2
            temp2 = temp2.next
            val.next = None
            temp.next = val
            temp = temp.next
            k-=1
        return temp2
            




        
