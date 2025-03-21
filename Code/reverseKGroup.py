# 25. K 个一组翻转链表
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]

# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]

# 为了解决这个问题，我们需要将链表中的每k个节点一组进行翻转，如果剩余的节点不足k个，则保持原样。
# 我们可以通过迭代的方法来实现这一目标，具体步骤如下：

# 方法思路
# 使用虚拟头节点：为了方便处理头节点可能被翻转的情况，我们引入一个虚拟头节点（dummy node）。
# 分组处理：通过两个指针pre和end来确定每一组的起始和结束位置。
# pre指针始终指向当前待翻转组的前一个节点，end指针用于找到当前组的最后一个节点。
# 判断是否翻转：每次移动end指针k次，如果在移动过程中遇到null，说明剩余节点不足k个，直接结束处理。
# 翻转当前组：断开当前组与后续节点的连接，翻转当前组的子链表，然后将翻转后的子链表重新连接到原链表中。
# 更新指针：将pre指针移动到下一组的前一个节点，继续处理下一组，直到所有可能的组都被处理完毕。

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        end = dummy
        
        while end.next:
            # Move end k steps ahead
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            # Record the start and next group's start
            start = pre.next
            next_start = end.next
            # Disconnect the current group
            end.next = None
            # Reverse the current group
            reversed_head = reverse(start)
            # Link the reversed group back
            pre.next = reversed_head
            start.next = next_start
            # Move pre and end to the end of the reversed group
            pre = start
            end = pre
        
        return dummy.next
    
# 代码解释
# reverse函数：用于翻转一个子链表，返回翻转后的头节点。
# 虚拟头节点dummy：简化链表操作，避免处理头节点翻转的特殊情况。
# pre和end指针：pre指针始终指向当前待翻转组的前一个节点，end指针用于找到当前组的最后一个节点。
# 循环处理每一组：通过移动end指针k次来确定当前组的结束位置，如果中途遇到null，说明剩余节点不足k个，直接返回结果。
# 断开和翻转当前组：断开当前组与后续节点的连接，翻转当前组，再将翻转后的子链表重新连接到原链表中。
# 更新指针：将pre指针移动到下一组的前一个节点，继续处理后续节点，直到所有可能的组都被处理完毕。
# 这种方法确保了每k个节点一组进行翻转，同时处理了剩余节点不足k个的情况，保证了时间复杂度为O(n)，空间复杂度为O(1)。