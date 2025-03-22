# 108. 将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

# 要将有序数组转换为平衡的二叉搜索树，可以采用递归分治的方法。每次选择数组中间的元素作为根节点，确保左右子树的节点数接近，从而保证树的平衡。

# **步骤解析：**
# 1. **确定根节点：** 每次递归中，选择当前子数组的中间元素作为根节点。中间位置可以通过计算 `mid = (left + right) // 2` 得到。
# 2. **递归构建子树：** 左子树由中间元素左侧的子数组构建，右子树由右侧的子数组构建。
# 3. **终止条件：** 当子数组的左边界超过右边界时，返回空节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List,Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
    
        return helper(0, len(nums) - 1)

# **复杂度分析：**
# - **时间复杂度：** O(n)，每个节点恰好被访问一次。
# - **空间复杂度：** O(log n)，递归调用栈的深度由树的高度决定，平衡二叉树的高度为 log n。

# **示例说明：**
# 对于数组 `[-10, -3, 0, 5, 9]`，构建过程如下：
# 1. 选择中间元素 `0` 作为根节点。
# 2. 左子数组 `[-10, -3]` 选择中间元素 `-10` 作为左子树的根。
# 3. 右子数组 `[5, 9]` 选择中间元素 `5` 作为右子树的根。
# 4. 递归处理各子数组，最终形成平衡二叉搜索树。

# 此方法确保每次分割后的左右子树节点数差不超过1，从而保证树的平衡。