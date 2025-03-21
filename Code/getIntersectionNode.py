# 160. 相交链表
# 相关企业
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
# 如果两个链表不存在相交节点，返回 null 。

#链表
# 要找到两个链表的第一个公共节点，可以使用双指针法，无需额外空间，时间复杂度为O(m + n)。以下是具体步骤：

# 方法思路
# 双指针遍历：使用两个指针pA和pB分别从链表A和链表B的头节点出发。

# 交叉遍历：当pA遍历完链表A后，继续从链表B的头开始遍历；同样，当pB遍历完链表B后，继续从链表A的头开始遍历。

# 相遇点：由于两个指针分别遍历两个链表的总长度（A+B和B+A），若有公共节点，它们会在第一个公共节点相遇；若没有，最终同时到达null。

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA != pB:
            #pA = pA.next if pA else headB
            #pB = pB.next if pB else headA
            if pA:
                pA = pA.next
            else:
                pA = headB
            if pB:
                pB = pB.next
            else:
                pB = headA
        return pA
    
# 代码解释
# 初始化指针：pA和pB分别指向两个链表的头节点。

# 循环遍历：当pA和pB不相遇时，继续移动指针。若指针到达链表末尾，则转向另一链表的头节点。

# 返回结果：当两指针相遇时即为第一个公共节点；若遍历结束未相遇，返回None。

# 这种方法高效且节省空间，适用于寻找两个链表的第一个公共节点。

import unittest

class TestGetIntersectionNode(unittest.TestCase):

    def test_get_intersection_node(self):
        # 创建两个链表，有交点
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        node6 = ListNode(6)
        node6.next = node3

        # 测试有交点的情况
        solution = Solution()
        intersection_node = solution.getIntersectionNode(node1, node6)
        self.assertEqual(intersection_node, node3)

    def test_no_intersection_node(self):
        # 创建两个链表，没有交点
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)

        node4 = ListNode(4)
        node5 = ListNode(5)

        node1.next = node2
        node2.next = node3

        node4.next = node5

        # 测试没有交点的情况
        solution = Solution()
        intersection_node = solution.getIntersectionNode(node1, node4)
        self.assertIsNone(intersection_node)

if __name__ == '__main__':
    unittest.main()