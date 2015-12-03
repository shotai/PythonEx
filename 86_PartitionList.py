# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1, head2 = ListNode(0), ListNode(0)
        tmp1, tmp2 = head1, head2
        tmp = head
        while tmp:
            if tmp.val<x:
                tmp1.next = ListNode(tmp.val)
                tmp1 = tmp1.next
            else:
                tmp2.next = ListNode(tmp.val)
                tmp2 = tmp2.next
            tmp = tmp.next
        tmp1.next = head2.next
        return head1.next
