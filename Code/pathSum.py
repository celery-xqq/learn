# 437. 路径总和 III
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# 为了解决路径总和 III 的问题，我们需要找到二叉树中所有路径的和等于给定目标值的路径数目。
# 路径可以从任意节点开始，但必须向下延伸。我们可以利用前缀和的思想来高效地解决这个问题。

# ### 方法思路
# 1. **前缀和思想**：类似数组中的子数组和问题，我们使用前缀和来记录从根节点到当前节点的路径上的所有节点值的和。
# 通过维护一个哈希表来存储各个前缀和出现的次数，我们可以快速判断是否存在从某个祖先节点到当前节点的路径和等于目标值。
# 2. **递归遍历**：采用深度优先搜索（DFS）遍历每个节点，计算当前前缀和，并检查是否存在所需的前缀和差值。
# 递归处理左右子树后，回溯时更新哈希表以维护正确的状态。

### 解决代码
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # 初始前缀和为0的路径数目为1（空路径）
        
        def dfs(node, current_sum):
            if not node:
                return
            current_sum += node.val
            # 检查是否存在所需的前缀和差值
            self.count += prefix_counts.get(current_sum - targetSum, 0)
            # 更新当前前缀和的计数
            prefix_counts[current_sum] += 1
            # 递归处理左右子树
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            # 回溯，恢复前缀和计数
            prefix_counts[current_sum] -= 1
        
        dfs(root, 0)
        return self.count

# ### 代码解释
# 1. **初始化**：使用一个哈希表 `prefix_counts` 来记录各个前缀和的出现次数，初始时前缀和为0的次数设为1（表示空路径）。
# 2. **递归函数 `dfs`**：遍历每个节点，计算当前前缀和，并检查哈希表中是否存在 `current_sum - targetSum`。
# 若存在，则说明存在一个子路径的和等于目标值，更新结果。
# 3. **更新哈希表**：在处理当前节点后，更新哈希表以记录当前前缀和，然后递归处理左右子树。
# 4. **回溯**：在递归返回后，恢复哈希表的状态，确保不影响其他分支的计算。

# 这种方法的时间复杂度为 O(n)，每个节点仅访问一次，哈希表的操作均为常数时间。空间复杂度为 O(n)，用于存储前缀和和递归栈。

