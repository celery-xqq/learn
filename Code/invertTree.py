# 226. 翻转二叉树
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

# 要翻转一棵二叉树，我们可以通过交换每个节点的左右子节点，并递归地处理其子树来实现。以下是具体的解决方案：

# ### 方法一：递归（前序遍历）
# 我们使用递归的方式，先交换当前节点的左右子节点，然后递归地处理其左右子树。

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # 交换当前节点的左右子节点
        root.left, root.right = root.right, root.left
        # 递归处理左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# ### 方法二：迭代（层序遍历）
# 我们使用队列进行层序遍历，每次处理一个节点时交换其左右子节点，并将子节点加入队列以便后续处理。

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # 交换当前节点的左右子节点
            node.left, node.right = node.right, node.left
            # 将子节点加入队列继续处理
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

# ### 方法三：递归（后序遍历）
# 另一种递归方式，先递归处理左右子树，再交换当前节点的左右子节点。

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # 递归处理左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # 交换当前节点的左右子节点
        root.left, root.right = right, left
        return root

# ### 思路解释
# 1. **递归（前序遍历）**：在每个节点处，先交换其左右子节点，然后递归处理左子树和右子树。
# 2. **迭代（层序遍历）**：使用队列进行广度优先遍历，每次处理节点时交换其左右子节点，并将子节点加入队列以便后续处理。
# 3. **递归（后序遍历）**：先递归处理左右子树至最底层，然后从底向上交换每个节点的左右子节点。

# 所有方法的时间复杂度均为 O(n)，其中 n 是树中的节点数，因为每个节点都被访问一次。空间复杂度最坏情况下为 O(n)，取决于树的结构。