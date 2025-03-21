# 138. 随机链表的复制
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。
# 新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。
# 复制链表中的指针都不应指向原链表中的节点 。
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
# 返回复制链表的头节点。
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。

#使用哈希表
# 为了复制带有随机指针的链表，我们可以使用哈希表来维护原节点到新节点的映射关系。
# 这种方法分为两次遍历：
# 第一次遍历创建所有新节点并存储到哈希表中；
# 第二次遍历设置新节点的next和random指针。
# 这种方法的时间复杂度为O(n)，空间复杂度为O(n)。

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        node_map = {}
        curr = head
        # 第一次遍历，创建所有新节点并存储到哈希表
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        # 第二次遍历，设置新节点的next和random指针
        curr = head
        while curr:
            new_node = node_map[curr]
            if curr.next:
                new_node.next = node_map[curr.next]
            if curr.random:
                new_node.random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]
# 方法解释
# 第一次遍历：创建每个原节点对应的新节点，并将原节点作为键、新节点作为值存入哈希表。
# 第二次遍历：根据哈希表快速查找每个原节点的next和random对应的新节点，正确设置新节点的指针关系。
# 这种方法确保每个新节点的指针都指向复制链表中的节点，而不是原链表的节点，从而实现了深拷贝。