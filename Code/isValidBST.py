# 98. 验证二叉搜索树
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 有效 二叉搜索树定义如下：
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 为了验证一个二叉树是否是有效的二叉搜索树（BST），我们可以利用递归的方法来确保每个节点的值都处于正确的范围内。
# 具体来说，每个节点的值必须严格大于其左子树所有节点的最大值，并严格小于其右子树所有节点的最小值。
# 通过递归地传递并更新每个节点的值范围，我们可以高效地验证整个树的结构是否符合BST的定义。

# ### 方法思路
# 1. **递归检查范围**：对于每个节点，检查其值是否在允许的范围内。初始时，根节点的范围是负无穷到正无穷。
# 2. **更新范围**：对于左子树，最大值更新为当前节点的值，最小值保持不变；对于右子树，最小值更新为当前节点的值，最大值保持不变。
# 3. **终止条件**：如果节点为空，返回True；如果节点值不在当前范围内，返回False；否则递归检查左右子树。

### 解决代码
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            return helper(node.left, low, val) and helper(node.right, val, high)
        return helper(root, float('-inf'), float('inf'))

# ### 代码解释
# 1. **辅助函数`helper`**：该函数接受当前节点`node`、当前允许的最小值`low`和最大值`high`作为参数。
# 2. **基础情况**：如果当前节点为空，说明子树是有效的，返回True。
# 3. **范围检查**：检查当前节点的值是否超出了允许的范围。如果超出，返回False。
# 4. **递归检查子树**：递归调用`helper`函数检查左子树和右子树，更新相应的范围。
# 左子树的最大值更新为当前节点的值，右子树的最小值更新为当前节点的值。
# 5. **初始调用**：从根节点开始，初始范围为负无穷到正无穷。

# 这种方法通过递归确保每个节点都满足BST的条件，时间复杂度为O(n)，其中n是树中的节点数，每个节点仅被访问一次。
# 空间复杂度在最坏情况下（树退化为链表）为O(n)，平均情况下为O(log n)。