# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def getNum(l: Optional[ListNode]) -> Optional[List]:
        str_l = ''
        while l != None:
            str_l = str_l.__add__(str(l.val))
            l = l.next
        return int(str_l[::-1])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_l1 = ListNode.getNum(l1)
        num_l2 = ListNode.getNum(l2)
        result_num = str(num_l1 + num_l2)
        SumTwoNum = ListNode(val=int(result_num[0]), next=None)
        for num in result_num[1:]:
            SumTwoNum = ListNode(val=int(num), next=SumTwoNum)
        return SumTwoNum


