# 102. 二叉树的层序遍历
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

# 要解决二叉树的层序遍历问题，我们可以使用广度优先搜索（BFS）算法，利用队列来逐层处理节点。具体步骤如下：

# ### 方法思路
# 1. **初始化队列和结果列表**：首先检查根节点是否为空，若为空则直接返回空列表。否则，将根节点加入队列，并初始化结果列表。
# 2. **逐层处理节点**：当队列不为空时，循环处理每一层的节点。每次处理当前层的所有节点，记录这些节点的值，并将它们的子节点加入队列。
# 3. **保存当前层的结果**：在处理完当前层的所有节点后，将当前层的节点值列表添加到结果列表中。

# 这种方法确保每一层的节点按从左到右的顺序处理，并正确保存每一层的节点值。

### 解决代码
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        
        return result

# ### 代码解释
# 1. **初始化队列和结果列表**：使用`deque`来高效处理节点的入队和出队操作。如果根节点为空，直接返回空列表。
# 2. **逐层处理**：外层循环处理每一层的节点，内层循环处理当前层的所有节点。每次处理当前层节点时，记录节点值，并将子节点加入队列。
# 3. **保存当前层结果**：每处理完一层节点后，将该层的节点值列表添加到结果列表中。

# 这种方法的时间复杂度为O(n)，其中n是二叉树的节点数，每个节点被访问一次。空间复杂度为O(n)，最坏情况下队列中存储的节点数最多为n。