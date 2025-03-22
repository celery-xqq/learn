# 543. 二叉树的直径
# 给你一棵二叉树的根节点，返回该树的 直径 。
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
# 两节点之间路径的 长度 由它们之间边数表示。

# 要解决二叉树直径的问题，我们需要找到树中最长的路径长度，这条路径可能经过根节点，也可能不经过。路径的长度由边数表示。

# ### 方法思路
# 二叉树的直径可以看作是每个节点的左右子树高度之和的最大值。这里的高度是指从当前节点到其最深叶子节点的边数。
# 我们可以使用递归的方法来计算每个节点的高度，并在递归过程中更新最大直径值。

# 具体步骤如下：
# 1. **递归计算子树高度**：对于每个节点，递归计算其左右子树的高度。
# 2. **更新最大直径**：当前节点的直径候选值为左右子树高度之和加2（因为左右子树的高度是从子节点开始计算的边数，所以需要加2）。
# 将候选值与全局最大值比较，更新最大值。
# 3. **返回当前节点高度**：当前节点的高度为左右子树高度的最大值加1。

### 解决代码
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0  # 初始化最大直径为0
        
        def depth(node):
            if not node:
                return -1  # 空节点的高度为-1
            left_depth = depth(node.left)  # 递归计算左子树的高度
            right_depth = depth(node.right)  # 递归计算右子树的高度
            # 当前节点的直径候选为左右子树高度之和加2，并更新最大直径
            self.max_diameter = max(self.max_diameter, left_depth + right_depth + 2)
            # 返回当前节点的高度
            return max(left_depth, right_depth) + 1
        
        depth(root)  # 从根节点开始递归计算
        return self.max_diameter
# ### 代码解释
# 1. **初始化最大直径**：使用实例变量`max_diameter`来记录当前找到的最大直径。
# 2. **递归函数`depth`**：该函数计算并返回以当前节点为根的子树的高度，同时更新最大直径。
# 3. **处理空节点**：空节点的高度定义为-1，因为叶子节点到空子树的边数为0，但叶子节点本身的高度为0。
# 4. **计算子树高度**：递归计算左右子树的高度，并计算当前节点的候选直径（左右子树高度之和加2），更新最大直径。
# 5. **返回当前节点高度**：当前节点的高度为左右子树高度的最大值加1。

# 该方法通过一次后序遍历即可完成所有计算，时间复杂度为O(n)，空间复杂度为O(h)（其中h为树的高度）。