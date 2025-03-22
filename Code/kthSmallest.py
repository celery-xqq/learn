# 230. 二叉搜索树中第 K 小的元素
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

# Definition for a binary tree node.
# 递归的核心思路仍然是中序遍历，但需要通过提前终止递归来优化效率。以下是实现代码和详细解释：
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k      # 用成员变量保存当前要找的k值
        self.result = 0  # 保存最终结果
        
        def inorder(node):
            #if not node or self.k == 0:  # 保留条件以提前终止递归
            if not node:
                return
            # 先递归左子树（中序遍历）
            inorder(node.left)
            # 处理当前节点
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return    # 找到结果后提前终止递归
            inorder(node.right)
        
        inorder(root)
        return self.result


             