# 2. 两数相加
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 为了解决这个问题，我们需要将两个逆序存储的非负整数链表相加，并返回一个同样形式的链表。我们可以通过逐位相加并处理进位来实现这一点。

# 方法思路
# 初始化：创建一个哑节点（dummy node）作为结果链表的起始点，以便于处理头节点的问题。同时，初始化进位变量carry为0。

# 遍历链表：使用循环遍历两个链表，直到两个链表都遍历完毕且进位为0为止。

# 处理每一位相加：在每次循环中，取两个链表当前节点的值（如果节点存在，否则视为0），加上进位值，计算当前位的总和。

# 更新进位和结果链表：根据当前位的总和计算新的进位值，并创建新节点存储当前位的值。

# 移动指针：移动两个链表的指针到下一个节点（如果存在的话）。


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0
        
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             total = val1 + val2 + carry
#             carry = total // 10
#             current.next = ListNode(total % 10)
#             current = current.next
            
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
        
#         return dummy.next

# 代码解释
# 初始化：创建哑节点dummy和当前指针current，初始进位carry为0。
# 循环处理每一位：只要两个链表有一个不为空或进位不为0，就继续处理。
# 取值：取当前节点的值，若节点不存在则取0。
# 计算总和和进位：计算当前位的总和和新的进位值。
# 创建新节点：将当前位的值存入新节点，并链接到结果链表。
# 移动指针：移动两个链表的指针到下一个节点（如果存在的话）。
# 返回结果：返回哑节点的下一个节点，即结果链表的头节点。
# 该方法的时间复杂度为O(max(n, m))，其中n和m是两个链表的长度，空间复杂度同样为O(max(n, m))，用于存储结果链表。

def printListNode(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        sum = 0
        cpl = 0
        while l1 and l2:
            sum = l1.val + l2.val + cpl
            cpl = int(sum / 10)
            sum = sum % 10
            cur.next = ListNode(sum)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1 :
            sum = l1.val + cpl
            cpl = int(sum / 10)
            sum = sum % 10
            cur.next = ListNode(sum)
            cur = cur.next
            l1 = l1.next
        while l2 :
            sum = l2.val + cpl
            cpl = int(sum / 10)
            sum = sum % 10
            cur.next = ListNode(sum)
            cur = cur.next
            l2 = l2.next
        if cpl > 0:
            cur.next = ListNode(cpl)
        return dummy.next

list1 = [9,9,9,9,9,9,9]
list2 = [9,9]
l1 = dummy1 = ListNode()
l2 = dummy2 = ListNode()

for i in list1:
    l1.next = ListNode(i)
    l1 = l1.next
l1 = dummy1.next

for i in list2:
    l2.next = ListNode(i)
    l2 = l2.next
l2 = dummy2.next

printListNode(l1)
printListNode(l2)
sol = Solution()
printListNode(sol.addTwoNumbers(l1,l2))


