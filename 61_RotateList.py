# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 0:
            return head
        end = head
        l=1
        while end.next:
            l+=1
            end = end.next
        end.next = head
        i = 0
        breaknode = end
        k = abs(l - (k%l))
        while i<k:
            breaknode = breaknode.next
            i += 1
        newHead = breaknode.next
        breaknode.next =  None

        return newHead
  
  #refe: https://leetcode.com/discuss/57940/python-solution-circle-linked-list-and-56ms-performance
