# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        dummy = ListNode(0)
        c = dummy
        while head1 and head2:
            if(head1.val<=head2.val):
                c.next = head1
                head1 = head1.next
            else:
                c.next = head2
                head2 = head2.next
            c = c.next
        if head1:
            c.next = head1
        if head2:
            c.next = head2
        return dummy.next
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head==None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge(head1, head2)
