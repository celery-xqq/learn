# 206. 反转链表
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# 迭代法
# 思路：
# 使用三个指针：newH（新的头节点）、current（当前节点）、temp（临时保存下一个节点）。
# 遍历链表，每次将当前节点的next指向新的头节点，然后更新指针位置。
# 当遍历完成时，newH即为反转后的头节点

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newH = None
        current = head
        while current:
            temp = current.next
            current.next=newH
            newH = current
            current = temp
        return newH

import unittest
class TestReverseList(unittest.TestCase):

    def test_reverseList(self):
        # 测试空链表
        head = None
        solution = Solution()
        reversed_head = solution.reverseList(head)
        self.assertIsNone(reversed_head)

        # 测试单个节点的链表
        head = ListNode(1)
        reversed_head = solution.reverseList(head)
        self.assertEqual(reversed_head.val, 1)

        # 测试多个节点的链表
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        reversed_head = solution.reverseList(head)
        self.assertEqual(reversed_head.val, 5)
        self.assertEqual(reversed_head.next.val, 4)
        self.assertEqual(reversed_head.next.next.val, 3)
        self.assertEqual(reversed_head.next.next.next.val, 2)
        self.assertEqual(reversed_head.next.next.next.next.val, 1)

if __name__ == '__main__':
    unittest.main()