# 19. 删除链表的倒数第 N 个结点
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]

# 示例 3：
# 输入：head = [1,2], n = 1
# 输出：[1]


from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        #关键点在于使用哑巴节点
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        #首先找到需要删除的节点
        for i in range(n):
                fast = fast.next
        while fast:
            last = slow
            slow = slow.next
            fast = fast.next
        #进行删除操作
        last.next = slow.next
        slow.next = None

        return dummy.next
    
# 要删除链表的倒数第N个节点，可以使用双指针（快慢指针）的方法，并结合哑节点（dummy node）来简化头节点的处理。以下是详细的解决方案：
# 方法思路
# 哑节点（Dummy Node）：创建一个哑节点，并将其next指针指向链表的头节点。这样，当需要删除头节点时，处理方式与删除其他节点一致。
# 双指针法：使用快慢指针，快指针先移动N+1步，然后快慢指针同时移动，直到快指针到达链表末尾。此时，慢指针的下一个节点即为要删除的节点。
# 删除节点：调整慢指针的next指针，跳过需要删除的节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         fast = slow = dummy
        
#         # 将快指针向前移动n+1步
#         for _ in range(n + 1):
#             fast = fast.next
        
#         # 同时移动快慢指针，直到快指针到达末尾
#         while fast:
#             fast = fast.next
#             slow = slow.next
        
#         # 删除倒数第n个节点
#         slow.next = slow.next.next
        
#         return dummy.next
# 代码解释
# 创建哑节点：dummy节点指向头节点，便于处理头节点删除的情况。
# 初始化快慢指针：初始时，快指针和慢指针都指向哑节点。
# 快指针移动N+1步：这样快指针和慢指针之间保持N+1的间距，使得当快指针到达末尾时，慢指针正好指向倒数第N+1个节点（即要删除节点的前驱）。
# 同步移动快慢指针：当快指针到达末尾时，慢指针的下一个节点即为要删除的节点。
# 删除节点：调整慢指针的next指针，跳过需要删除的节点，最后返回哑节点的next指针作为新的头节点。
# 这种方法的时间复杂度为O(L)，其中L是链表的长度，空间复杂度为O(1)。
# 开启新对话
