# -*- coding: utf-8 -*-s
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: ListNode) -> bool:
#def has_cycle(head):
    """
    判断链表是否有环的快慢指针法
    :param head: 链表头节点
    :return: True 表示有环，False 表示无环
    """
    if not head:
        return False  # 空链表直接返回无环
    
    slow = head  # 慢指针，每次移动一步
    fast = head  # 快指针，每次移动两步
    
    # 只需检查 fast 及其 next 是否非空
    # （因为 fast 移动更快，如果无环，它会先到达末尾）
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # 快慢指针相遇，存在环
    
    return False  # 快指针走到末尾，无环


# --------------- 测试用例 ---------------
if __name__ == "__main__":
    # 构造一个带环的链表：1 -> 2 -> 3 -> 2（环）
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node2  # 成环
    
    print(has_cycle(node1))  # 输出 True

    # 构造一个无环的链表：4 -> 5 -> 6
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6
    
    print(has_cycle(node4))  # 输出 False