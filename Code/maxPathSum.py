# 124. 二叉树中的最大路径和
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

# 要解决二叉树中的最大路径和问题，我们需要考虑所有可能的路径情况，并找到其中路径和的最大值。
# 路径可以是任意节点序列，只要相邻节点之间有边相连，同一个节点在路径中最多出现一次。

# ### 方法思路
# 我们可以使用递归的方法来解决这个问题。对于每个节点，我们需要计算以该节点为根的最大路径和，
# 这包括该节点本身的值、左子树的最大贡献和右子树的最大贡献。
# 递归过程中，我们维护一个全局变量来记录当前的最大路径和。

# 具体步骤如下：
# 1. 初始化一个全局变量 `max_sum`，初始值为负无穷，用于记录最大路径和。
# 2. 定义递归函数 `max_gain(node)`，计算以该节点为根的单边路径的最大贡献：
#    - 如果节点为空，返回0。
#    - 递归计算左子树和右子树的最大贡献，若贡献为负则取0（因为负数贡献会降低总和）。
#    - 计算当前节点的路径和（包括左子树、当前节点和右子树），并更新全局最大路径和。
#    - 返回当前节点加上左右子树中较大贡献的单边路径值，供父节点使用。
# 3. 调用递归函数后，返回全局变量 `max_sum`。

### 解决代码
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            # 计算左右子树的最大贡献值，若为负则取0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # 当前节点的路径和，可能成为最大路径
            current_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_sum)
            
            # 返回该节点的最大贡献值，只能选择一边
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

# ### 代码解释
# - `maxPathSum` 方法初始化全局变量 `max_sum` 并调用递归函数 `max_gain`。
# - `max_gain` 递归计算每个节点的最大贡献值：
#   - 若节点为空，返回0。
#   - 递归计算左右子树的最大贡献值，若为负则取0。
#   - 计算当前节点的路径和，并更新全局最大路径和。
#   - 返回当前节点加上左右子树中较大贡献值的单边路径值。

# 该方法通过递归遍历每个节点，时间复杂度为 O(n)，空间复杂度为 O(n)（最坏情况下树退化为链表）。