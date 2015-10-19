# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        head = ListNode(0)
        dummy = head
        carry = 0
        while l1 and l2:
            tmp = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val+l2.val+carry)/10
            dummy.next = tmp
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            tmp = ListNode((l1.val+carry)%10)
            carry = (l1.val+carry)/10
            dummy.next = tmp
            dummy = dummy.next
            l1 = l1.next
        while l2:
            tmp = ListNode((l2.val+carry)%10)
            carry = (l2.val+carry)/10
            dummy.next = tmp
            dummy = dummy.next
            l2 = l2.next
        if carry>0:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        return head.next
