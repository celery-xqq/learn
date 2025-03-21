# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 要将两个升序链表合并为一个新的升序链表，可以使用类似归并排序中的合并方法。具体步骤如下：

# 初始化哑结点：创建一个哑结点（dummy node）作为合并后链表的起始点，以便简化头节点的处理。维护一个当前指针 cur 初始指向哑结点。

# 比较并合并：同时遍历两个链表，比较当前节点的值，将较小值的节点连接到 cur 的后面，并移动对应的链表指针和 cur 指针。

# 处理剩余节点：当其中一个链表遍历完成后，将另一个链表的剩余节点直接连接到当前链表的末尾。

# 返回结果：哑结点的下一个节点即为合并后的链表头。

# 这种方法的时间复杂度为 O(n + m)，空间复杂度为 O(1)。

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val <=list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2

        return dummy.next

# 边界情况处理：

# 当其中一个链表为空时，直接返回另一个链表。

# 当两个链表均为空时，返回空链表。

# 该算法通过逐个比较节点值并调整指针，高效地合并两个有序链表，保证了升序顺序。