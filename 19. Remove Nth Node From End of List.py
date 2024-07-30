class Solution:
    def removeNthFromEnd(self, head, n): 
        first = second = ListNode(0, head)
        for i in range(n):
            second = second.next
        curr = first
        while  second and second.next:
            first = first.next
            second = second.next
        first.next = first.next.next
        return curr.next