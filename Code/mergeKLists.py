# 23. 合并 K 个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 示例 1：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6

# 示例 2：
# 输入：lists = []
# 输出：[]

# 示例 3：
# 输入：lists = [[]]
# 输出：[]

#相邻的链表两两合并

from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None
        #两两合并
        n = len(lists)
        l1 = lists[0]
        for i in range(1,n):
            l2 = lists[i]
            l1 = self.mergeTwoLists(l1,l2)
        return l1

    #两个链表合并的方法
    def mergeTwoLists(self , l1 ,l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2 :
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next