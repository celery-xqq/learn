# 114. 二叉树展开为链表
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

# 要将二叉树展开为单链表，使其顺序与先序遍历相同，并且只使用右指针连接，可以按照以下步骤进行：

# ### 方法思路
# 我们可以使用一种类似Morris遍历的方法，在原树上直接修改指针，不需要额外的空间。具体步骤如下：
# 1. 从根节点开始，遍历每个节点。
# 2. 如果当前节点有左子树，找到左子树的最右节点（即左子树先序遍历的最后一个节点）。
# 3. 将左子树的最右节点的右指针指向当前节点的右子树。
# 4. 将当前节点的右指针指向左子树，并将左指针置空。
# 5. 继续处理下一个节点（即当前节点的右子节点）。

# 这种方法的时间复杂度为O(n)，每个节点最多被访问两次，空间复杂度为O(1)。

### 解决代码
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # 找到左子树的最右节点
                pre = curr.left
                while pre.right:
                    pre = pre.right
                # 将最右节点的右指针指向当前节点的右子树
                pre.right = curr.right
                # 将当前节点的右指针指向左子树，左指针置空
                curr.right = curr.left
                curr.left = None
            # 处理下一个节点
            curr = curr.right

# ### 代码解释
# 1. **初始化当前节点**：从根节点开始遍历。
# 2. **处理左子树**：如果当前节点存在左子树，找到左子树的最右节点。
# 3. **调整指针**：将最右节点的右指针指向当前节点的右子树，然后将当前节点的右指针指向左子树，左指针置空。
# 4. **移动到下一个节点**：处理完成后，移动到当前节点的右子节点继续处理，直到所有节点处理完毕。

# 这种方法保证了在遍历过程中逐步将左子树展开到右子树，形成先序遍历的单链表结构。