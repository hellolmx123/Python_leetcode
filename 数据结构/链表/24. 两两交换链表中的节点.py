# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.cnt = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.cnt:
            return -1
        # 非法情况
        cur = self.dummy.next

        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        New = ListNode(val = val,next = self.dummy.next)
        self.dummy.next = New
        self.cnt += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.cnt, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.cnt:
            return
        pre = self.dummy
        for _ in range(index):
            pre = pre.next
        pre.next = ListNode(val, pre.next)
        self.cnt += 1

    def deleteAtIndex(self, index: int) -> ListNode:
        if index >= self.cnt:
            return self.dummy
        pre = self.dummy
        for _ in range(index):
            pre = pre.next
        t = pre.next
        pre.next = t.next
        t.next = None
        self.cnt -= 1
        return self.dummy.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        dummy = ListNode(next=head)
        tag = dummy
        pre = head.next
        cur = head
        while pre:
            cur.next = pre.next
            pre.next = cur
            tag.next = pre

            tag = cur
            cur = tag.next
            if cur:
                pre = cur.next
            else:
                break

        return dummy.next

LinkList = MyLinkedList()
for i in range(1, 6):
    LinkList.addAtTail(i)
obj = Solution()
obj.swapPairs(LinkList.dummy.next)