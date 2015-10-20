# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next
        while curr.next:
            if curr.val>curr.next.val:
                pre = dummy
                while pre.next.val<curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next=tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next
