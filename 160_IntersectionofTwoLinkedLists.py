# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur1, cur2 = headA, headB
        l1, l2 = 0, 0
        while cur1:
            l1+=1
            cur1 = cur1.next
        while cur2:
            l2+=1
            cur2 = cur2.next
        cur1, cur2 = headA, headB
        if l1>l2:
            for i in range(l1-l2):
                cur1 = cur1.next
        elif l1<l2:
            for i in range(l2-l1):
                cur2 = cur2.next
        while cur2 != cur1:
            cur2 = cur2.next
            cur1 = cur1.next
        return cur1
