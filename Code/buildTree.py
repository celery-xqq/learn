# 105. 从前序与中序遍历序列构造二叉树
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

# 要根据前序遍历和中序遍历的结果构造二叉树，可以按照以下步骤进行：

# 1. **确定根节点**：前序遍历的第一个元素即为当前子树的根节点。
# 2. **分割中序数组**：在中序遍历中找到根节点的位置，将中序数组分割为左子树和右子树。
# 3. **递归构造子树**：根据左子树和右子树的节点数量，递归处理前序和中序数组的对应部分。

# ### 方法思路
# - **前序遍历**的顺序是根节点、左子树、右子树，因此前序数组的第一个元素即为当前子树的根节点。
# - **中序遍历**的顺序是左子树、根节点、右子树，因此可以通过根节点将中序数组分割为左右两部分，分别对应左子树和右子树。
# - 使用哈希表存储中序数组的值到索引的映射，以快速查找根节点的位置。
# - 递归处理左子树和右子树，构造整棵二叉树。

### 解决代码
# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 构建中序哈希映射，用于快速查找根节点位置
        index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_left: int, pre_right: int, in_left: int, in_right: int) -> TreeNode:
            if pre_left > pre_right:
                return None
            # 前序遍历的第一个节点是当前子树的根节点
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            # 找到根节点在中序中的位置
            in_root_idx = index_map[root_val]
            # 左子树的节点数目
            left_subtree_size = in_root_idx - in_left
            
            # 递归构造左子树
            root.left = helper(
                pre_left + 1, 
                pre_left + left_subtree_size, 
                in_left, 
                in_root_idx - 1
            )
            # 递归构造右子树
            root.right = helper(
                pre_left + left_subtree_size + 1, 
                pre_right, 
                in_root_idx + 1, 
                in_right
            )
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

### 代码解释
# 1. **哈希表构建**：首先构建中序数组的值到索引的映射，以便快速查找根节点位置。
# 2. **递归函数helper**：该函数接收前序和中序数组的当前处理范围，返回构造的子树根节点。
#    - **终止条件**：当前序范围无效时（`pre_left > pre_right`），返回`None`。
#    - **根节点构造**：前序范围的第一个元素作为根节点。
#    - **分割中序数组**：找到根节点在中序中的位置，计算左子树节点数目。
#    - **递归构造左右子树**：根据左子树节点数目，确定前序和中序数组的处理范围，递归构造左右子树。

# 该方法的时间复杂度为O(n)，空间复杂度为O(n)，能够高效地构造二叉树。

