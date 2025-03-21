# 148. 排序链表
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

# 为了对链表进行升序排序，我们可以使用归并排序算法。归并排序在链表结构中表现良好，因为它通过分治策略将链表分成两半，
# 递归排序后合并，且合并操作可以通过调整指针高效完成。

# 方法思路
# 分割链表：使用快慢指针找到链表的中间节点，将链表分为两部分。快指针每次移动两步，慢指针每次移动一步，当快指针到达末尾时，慢指针正好在中间位置。
# 递归排序：分别对分割后的左右两部分递归调用排序函数。
# 合并有序链表：合并两个已排序的链表，通过比较节点值逐个连接，形成新的有序链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 找到中间节点并分割链表
        mid = self.findMid(head)
        right_head = mid.next
        mid.next = None
        
        left = self.sortList(head)
        right = self.sortList(right_head)
        
        return self.merge(left, right)
    
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

# 代码解释
# sortList函数：主函数处理递归终止条件，分割链表，递归排序左右部分，然后合并。

# findMid函数：使用快慢指针找到链表的中间节点，将链表分割为两部分。

# merge函数：合并两个有序链表，通过比较节点值依次连接，处理剩余节点。

# 这种方法的时间复杂度为O(n log n)，空间复杂度为O(log n)（递归栈深度），适用于较大的链表排序。

