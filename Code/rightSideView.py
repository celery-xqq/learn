# 199. 二叉树的右视图
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 要获取二叉树的右视图，即每一层最右侧的节点值，可以采用广度优先搜索（BFS）的层次遍历方法。具体步骤如下：

# 1. **初始化**：如果根节点为空，直接返回空列表。否则，初始化队列并将根节点加入队列。
# 2. **层次遍历**：使用队列进行层次遍历。每次处理一层节点时，记录当前层的节点数。
# 3. **记录最右节点**：在每一层中，遍历所有节点，将子节点加入队列。当处理到当前层的最后一个节点时，将其值加入结果列表。

# 这种方法确保每次处理完一层后，结果列表中保存的是该层最右侧的节点值。

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # 当前层的最后一个节点加入结果
                if i == level_size - 1:
                    result.append(node.val)
                # 将子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

# ### 解释
# - **队列初始化**：使用双端队列 `deque` 来高效处理节点的入队和出队操作。
# - **层次遍历**：每次循环处理一层节点，通过当前队列的长度确定该层的节点数。
# - **记录最右节点**：在处理每层节点时，当遍历到最后一个节点（即 `i == level_size - 1`）时，将其值加入结果列表。
# - **子节点处理**：将当前节点的左右子节点依次加入队列，确保下一层的节点顺序正确。

# 这种方法的时间复杂度为 O(n)，每个节点被访问一次。空间复杂度为 O(n)，最坏情况下队列中存储所有节点。