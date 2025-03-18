# 141. 环形链表
# 给你一个链表的头节点 head ，判断链表中是否有环。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。


# 要判断链表是否有环，可以使用快慢指针法（Floyd判圈算法），步骤如下：
# 初始化指针：设置两个指针 slow 和 fast，初始时均指向链表头节点。
# 遍历链表：
# slow 每次移动一步。
# fast 每次移动两步。
# 终止条件：
# 若 fast 或 fast.next 为 null，说明链表无环，返回 false。
# 若 slow 和 fast 相遇，说明存在环，返回 true。

# 原理：
# 若无环，快指针会先到达末尾；若有环，快指针最终会追上慢指针（每次循环，快指针比慢指针多走一步，最终在环内相遇）。
# 时间复杂度：O(n)，空间复杂度：O(1)。
# 示例代码（Python）：

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

# 关键点解释
# 链表节点定义：
# ListNode 类定义了链表节点的结构，包含值 val 和指向下一个节点的指针 next。
# 快慢指针逻辑：
# 初始化：快指针 fast 和慢指针 slow 均从链表头节点开始。
# 移动规则：
# 慢指针每次移动一步：slow = slow.next
# 快指针每次移动两步：fast = fast.next.next
# 终止条件：
# 若 fast 或 fast.next 为 None，说明链表无环。
# 若 slow == fast，说明存在环。
# 时间复杂度：O(n)
# 无环时，快指针走到末尾的时间复杂度为 O(n/2) → O(n)。
# 有环时，快慢指针会在最多 O(n) 步内相遇。
# 空间复杂度：O(1)
# 仅使用两个指针的额外空间。

# 142. 环形链表 II
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 不允许修改 链表。

# 关键步骤与数学原理
# 快慢指针相遇：

# 使用快慢指针（快指针每次走2步，慢指针每次走1步）确定链表有环，并找到它们的相遇点。

# 设链表头到环入口的距离为 a，环入口到相遇点的距离为 b，相遇点再到环入口的距离为 c，则环的总长度为 b + c。

# 推导路程关系：

# 慢指针走过的路程：a + b。

# 快指针走过的路程：a + n(b + c) + b（n 为快指针在环内多绕的圈数，n ≥ 1）。

# 由于快指针速度是慢指针的2倍，因此路程满足：
# 2(a + b) = a + n(b + c) + b
# 化简得：
# a = (n-1)(b + c) + c

# 结论：

# 从链表头到环入口的距离 a 等于从相遇点走到环入口的距离 c 加上 (n-1) 圈环的长度。

# 若此时将一个指针重置到链表头，另一个留在相遇点，同步移动（每次各走1步），最终它们会在环入口相遇。

def detectCycle(head):
    # 步骤1：确认链表有环，并找到快慢指针的相遇点
    slow = fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    if not has_cycle:
        return None  # 无环
    
    # 步骤2：重置一个指针到链表头，同步移动找到入口
    ptr1 = head
    ptr2 = slow  # 相遇点
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1  # 入口节点


# 代码说明
# 确认环的存在：
# 使用快慢指针法找到相遇点（若没有环，直接返回 None）。
# 定位环入口：
# 将 ptr1 重置到链表头，ptr2 保留在相遇点。
# 同步移动 ptr1 和 ptr2，每次各走1步，直到它们相遇，相遇点即为环入口。

# 复杂度分析
# 时间复杂度：O(n)
# 找相遇点最多遍历链表一次，找入口最多再遍历一次，总体为线性时间。

# 空间复杂度：O(1)
# 仅使用固定数量的指针变量。

# 数学证明补充
# 公式 a = c + (n-1)(b + c) 表明，从链表头到入口的距离 a 等于从相遇点到入口的距离 c 加上若干圈环的长度。
# 无论快指针绕环多少圈，最终 ptr1 和 ptr2 会在入口点相遇。

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

    # 构造带环链表：1 -> 2 -> 3 -> 4 -> 2（环入口为2）
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 成环
    
    entry = detectCycle(node1)
    print("环入口节点的值:", entry.val)  # 输出 2

# 扩展问题
# 如何求环的长度？
# 在找到环入口后，可以固定一个指针，让另一个指针遍历环直到回到入口，计数步数即为环长。

