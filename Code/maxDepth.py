# 104. 二叉树的最大深度
# 给定一个二叉树 root ，返回其最大深度。
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

# 要解决二叉树的最大深度问题，可以使用递归或迭代的层序遍历方法。以下是两种方法的详细说明和代码实现：
# 方法一：递归法
# 递归法的核心思想是，对于每个节点，其最大深度等于其左右子树的最大深度加一。递归的终止条件是当前节点为空时返回0。
# 步骤分析：
# 终止条件：如果当前节点为空，返回深度0。
# 递归计算左右子树的深度：分别递归计算左子树和右子树的最大深度。
# 合并结果：返回左右子树深度中的较大值加一，即为当前节点的最大深度。

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth,right_depth) + 1

# 方法二：层序遍历（迭代法）
# 层序遍历使用队列来遍历每一层的节点，每遍历完一层，深度加一。当队列为空时，遍历结束，此时的深度即为最大深度。
# 步骤分析：
# 初始化队列：将根节点加入队列。
# 遍历队列：每次处理一层的所有节点，将下一层的节点加入队列。
# 更新深度：每处理完一层，深度加一。
# 代码实现：
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth

# 复杂度分析
# 时间复杂度：两种方法的时间复杂度均为O(n)，其中n为二叉树的节点数，每个节点均被访问一次。
# 空间复杂度：
# 递归法：最坏情况下（树退化为链表）空间复杂度为O(n)，平均情况下为O(logn)。
# 迭代法：最坏情况下（完全平衡二叉树）队列中存储的节点数为O(n)，因此空间复杂度为O(n)。
# 两种方法均能高效解决问题，递归法代码简洁，而迭代法则通过显式队列避免了递归的系统栈开销，适用于深度较大的树结构。根据具体场景选择合适的方法即可。