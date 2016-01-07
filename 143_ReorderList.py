# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        def splitlist(node):
            fast = node
            slow = node
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head2 = slow.next
            slow.next = None
            return node, head2
            
        def reverselist(node):
            last = None
            while node:
                tmp = node.next
                node.next = last
                last = node
                node = tmp
            return last
        
        def reverselist1(a, last=None):
            if not a:
                return last
            tmp = a.next
            a.next = last
            return reverselist(tmp, a)
        
        def mergelist(a, b):
            tail = a
            head = b
            a = a.next
            while b:
                tail.next = b
                tail = tail.next
                b = b.next
                if a:
                    a,b = b,a
            return head
        
        if not head or not head.next:
            return
        a, b = splitlist(head)
        b = reverselist(b)
        head = mergelist(a, b)
