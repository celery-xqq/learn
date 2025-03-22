# 101. 对称二叉树
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

# 要判断一个二叉树是否对称，可以通过比较其左右子树是否为镜像对称。
# 镜像对称的条件是：对应的节点值相等，且每个树的左子树与另一个树的右子树对称。

# ### 方法一：递归
# **思路**：
# 1. 如果根节点为空，直接返回 `true`。
# 2. 定义一个辅助函数 `isMirror`，用于递归判断两个节点是否为镜像对称：
#    - 如果两个节点都为空，返回 `true`。
#    - 如果其中一个为空另一个不为空，返回 `false`。
#    - 检查当前节点的值是否相等，并递归检查左节点的左子树与右节点的右子树，以及左节点的右子树与右节点的左子树。

# **代码实现**：

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                self.isMirror(left.left, right.right) and 
                self.isMirror(left.right, right.left))

# ### 方法二：迭代
# **思路**：
# 1. 使用队列来存储需要比较的节点对。
# 2. 初始时，将根节点的左右子节点入队。
# 3. 每次从队列中取出两个节点进行比较：
#    - 如果都为空，继续下一轮循环。
#    - 如果其中一个为空，返回 `false`。
#    - 如果值不相等，返回 `false`。
# 4. 将当前节点的左子节点与对应节点的右子节点，以及当前节点的右子节点与对应节点的左子节点依次入队。

# **代码实现**：
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        
        while queue:
            left_node = queue.popleft()
            right_node = queue.popleft()
            
            if not left_node and not right_node:
                continue
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            
            queue.append(left_node.left)
            queue.append(right_node.right)
            queue.append(left_node.right)
            queue.append(right_node.left)
        
        return True

# ### 复杂度分析
# - **时间复杂度**：两种方法均为 O(n)，其中 n 为树中的节点数，每个节点恰好被访问一次。
# - **空间复杂度**：
#   - **递归方法**：O(h)，其中 h 为树的高度。最坏情况下（树退化为链表），空间复杂度为 O(n)。
#   - **迭代方法**：O(n)，队列中最多需要存储 n 个节点。