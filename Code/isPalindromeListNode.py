# 234. 回文链表
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printListNode(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #空链表的情况需要处理吗？
        if head == None:
            return False
        #先处理链表个数为1的情况
        if head.next == None :
            return True

        slow = head
        fast = head
        #反转前半段链表，与后半段链表进行对比
        halfL = None
        halfR = None
        temp = None
        while fast and fast.next:
            fast=fast.next.next
            #反转链表
            temp = slow.next
            slow.next = halfL
            halfL = slow
            slow = temp
        #长度为偶数
        if fast == None:
            halfR=slow
        #长度为奇数
        else:
            halfR=slow.next
        #对比两个链表的值是不是一样，全部都相等，就是回文链表
        while halfR :
            if halfL.val != halfR.val:
                return False
            halfL=halfL.next
            halfR=halfR.next
        return True
            
        
import unittest

# 测试类
class TestSolution(unittest.TestCase):

    def test_isPalindrome_empty_list(self):
        # 空链表
        head = None
        solution = Solution()
        self.assertFalse(solution.isPalindrome(head))

    def test_isPalindrome_single_node(self):
        # 单个节点的链表
        head = ListNode(1)
        solution = Solution()
        self.assertTrue(solution.isPalindrome(head))

    def test_isPalindrome_two_nodes_same(self):
        # 两个节点值相同的链表
        head = ListNode(1, ListNode(1))
        solution = Solution()
        self.assertTrue(solution.isPalindrome(head))

    def test_isPalindrome_two_nodes_different(self):
        # 两个节点值不同的链表
        head = ListNode(1, ListNode(2))
        solution = Solution()
        self.assertFalse(solution.isPalindrome(head))

    def test_isPalindrome_even_length_palindrome(self):
        # 偶数长度的回文链表
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        solution = Solution()
        self.assertTrue(solution.isPalindrome(head))

    def test_isPalindrome_odd_length_palindrome(self):
        # 奇数长度的回文链表
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
        solution = Solution()
        self.assertTrue(solution.isPalindrome(head))

    def test_isPalindrome_not_palindrome(self):
        # 非回文链表
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        solution = Solution()
        self.assertFalse(solution.isPalindrome(head))

if __name__ == '__main__':
    unittest.main() 