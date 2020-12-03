# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # output = []
        # while list1:
        #     if list1.val != a:
        #         output.append(list1.val)
        #     elif list1.val == a:
        #         while list2:
        #             output.append(list2.val)
        #             list2 = list2.next
        #         for i in range(b-a+1):
        #             list1 = list1.next
        #         output.append(list1.val)
        #     list1 = list1.next
        # # print(output)
        # output result is ok, but this is list, not listnode.
        # the below is not working
        # l3
        # for i in output:
        #     l3 = ListNode(i)
        #     l3 = l3.next
        # return l3

        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        pre = ptr
        for _ in range(b - a + 1):
            pre = pre.next
        l2, p2 = list2, list2
        while p2.next:
            p2 = p2.next
        p2.next = pre.next
        pre.next = None
        ptr.next = l2

        l3 = list1
        while l3:
            print(l3.val)
            l3 = l3.next
        return list1

s = Solution()

list1 = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))))))
list2 = ListNode(val=1000000, next=ListNode(val=1000001, next=ListNode(val=1000002, next=None)))
a = 3
b = 4

print(s.mergeInBetween(list1, a, b, list2))