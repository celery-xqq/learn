# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

# 为了解决螺旋矩阵的问题，我们需要按照顺时针螺旋顺序遍历矩阵中的所有元素。
# 这个问题的关键在于分层处理矩阵，逐层从外到内遍历，并确保在每个方向遍历时不会重复访问元素。

# ### 方法思路
# 1. **分层处理**：将矩阵分为若干层，每一层按照顺时针方向遍历。
# 2. **边界控制**：使用四个变量`top`、`bottom`、`left`和`right`分别表示当前层的上下左右边界。
# 3. **方向遍历**：依次处理上边、右边、下边和左边，每次处理完一个方向后调整相应的边界，并检查是否需要提前终止循环以避免重复遍历。

### 解决代码
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        res = []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # 上边，从左到右
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            
            # 右边，从上到下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            
            # 下边，从右到左
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            
            # 左边，从下到上
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res


# ### 代码解释
# 1. **初始化边界**：`top`、`bottom`、`left`和`right`分别初始化为矩阵的上下左右边界。
# 2. **顺时针遍历**：
#    - **上边**：从左到右遍历`top`行的所有元素，遍历完成后`top`下移一行。
#    - **右边**：从上到下遍历`right`列的所有元素，遍历完成后`right`左移一列。
#    - **下边**：从右到左遍历`bottom`行的所有元素，遍历完成后`bottom`上移一行。
#    - **左边**：从下到上遍历`left`列的所有元素，遍历完成后`left`右移一列。
# 3. **边界检查**：每次处理完一个方向后，检查边界是否重叠，若重叠则提前终止循环，避免重复遍历。

# 这种方法通过逐层缩小边界并确保每个方向遍历的条件，能够高效且正确地按顺时针螺旋顺序遍历矩阵中的所有元素。
