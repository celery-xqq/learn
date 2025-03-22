# 94. 二叉树的中序遍历
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from typing import List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root,res)
        return res

    def traversal(self , cur: Optional[TreeNode],res: List[int]):
        if not cur:
            return
        self.traversal(cur.left,res)
        res.append(cur.val)
        self.traversal(cur.right,res)

# 为了对给定的二叉树进行中序遍历，我们可以使用迭代的方法来模拟递归过程。
# 这种方法利用栈来显式地跟踪需要访问的节点，确保按照左子树、根节点、右子树的顺序进行遍历。

# 方法思路
# 中序遍历的顺序是左子树 -> 根节点 -> 右子树。使用迭代方法时，我们维护一个栈来保存待处理的节点。具体步骤如下：
# 从根节点开始，将所有左子节点依次压入栈中，直到最左端的叶子节点。
# 弹出栈顶节点，将其值加入结果列表。
# 处理该节点的右子树，重复上述过程。
# 这种方法确保每个节点在处理完左子树后才会被访问，然后处理右子树，符合中序遍历的要求。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = []
#         curr = root
#         while curr or stack:
#             # 将当前节点的所有左子节点压入栈
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             # 弹出栈顶节点并处理
#             curr = stack.pop()
#             res.append(curr.val)
#             # 转向右子节点
#             curr = curr.right
#         return res
# 代码解释
# 初始化：res 列表用于存储遍历结果，stack 作为辅助栈，curr 初始指向根节点。
# 外层循环：只要当前节点不为空或栈不为空，继续处理。
# 内层循环：将当前节点的所有左子节点依次压入栈中，直到左子节点为空。
# 处理节点：弹出栈顶节点，将其值添加到结果列表，然后转向右子节点。
# 循环结束：当所有节点处理完毕，返回结果列表 res。
# 这种方法的时间复杂度为 O(n)，每个节点恰好被访问一次。空间复杂度为 O(n)，最坏情况下栈中存储所有节点。
