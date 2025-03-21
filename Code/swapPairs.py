# 24. 两两交换链表中的节点
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

# 示例 1：
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]

# 示例 2：
# 输入：head = []
# 输出：[]

# 示例 3：
# 输入：head = [1]
# 输出：[1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 步骤解释：
# 初始化哑结点：创建一个哑结点dummy，其next指向原链表的头节点head。这样可以统一处理头节点的交换情况，避免特殊处理。
# 使用前驱指针pre：pre初始指向dummy，用于跟踪当前要交换的两个节点的前驱节点。
# 循环交换相邻节点：
# 检查是否可交换：当pre.next和pre.next.next均存在时，说明还有至少两个节点可以交换。
# 确定当前节点a和b：a为pre.next，b为a.next。
# 保存后续节点：记录b的下一个节点next_node，以便后续连接。
# 执行交换：
# pre.next指向b，将前驱节点的next指向第二个节点。
# b.next指向a，完成b和a的交换。
# a.next指向next_node，将交换后的a连接到后续链表。
# 更新前驱指针：将pre移动到交换后的a节点（即下一组的前驱）。
# 返回结果：最终dummy.next即为交换后的链表头节点。
# 时间复杂度：O(n)，遍历链表一次，每个节点处理一次。
# 空间复杂度：O(1)，仅使用常数级别的额外空间。
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            next_node = b.next
            
            # 交换节点
            pre.next = b
            b.next = a
            a.next = next_node
            
            # 移动pre到下一组的前驱
            pre = a
        
        return dummy.next