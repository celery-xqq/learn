# 240. 搜索二维矩阵 II
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例 1：
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# 输出：true
# 示例 2：
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# 输出：false

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #从第一行的最后一个元素（matrix[0][n-1]）来开始遍历：如果target大于该元素，就向下搜索；如果小于，就向左搜索。等于就返回True
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        
        bottom = m - 1
        left = 0
        i, j = 0, n - 1
        while i <= bottom and j >= left:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False
    
# 要高效地在具有行列升序特性的二维矩阵中搜索目标值，可以采用从右上角（或左下角）开始的逐步缩小范围的方法。
# 该方法利用矩阵的行列有序特性，每次排除一行或一列，从而在O(m + n)的时间复杂度内完成搜索。

# ### 方法思路
# 1. **初始位置**：选择矩阵的右上角作为起始点（也可以选择左下角，逻辑类似）。
# 2. **比较与移动**：
#    - 如果当前元素等于目标值，找到目标，返回`True`。
#    - 如果当前元素大于目标值，由于列是升序排列的，当前列的所有元素都大于目标值，因此向左移动一列。
#    - 如果当前元素小于目标值，由于行是升序排列的，当前行的所有元素都小于目标值，因此向下移动一行。
# 3. **终止条件**：当行或列超出矩阵边界时，说明目标值不存在，返回`False`。

### 解决代码
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1
    while row < m and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1
        else:
            row += 1
    return False

# ### 代码解释
# - **边界处理**：首先检查矩阵是否为空或矩阵的行是否为空，若为空则直接返回`False`。
# - **初始化变量**：`m`和`n`分别表示矩阵的行数和列数，`row`和`col`初始化为右上角的位置（即第0行，最后一列）。
# - **循环搜索**：在行索引`row`小于行数`m`且列索引`col`非负的情况下循环：
#   - 若当前元素等于目标值，返回`True`。
#   - 若当前元素大于目标值，向左移动一列（`col -= 1`）。
#   - 否则，向下移动一行（`row += 1`）。
# - **越界判断**：若循环结束仍未找到目标值，返回`False`。

# 该方法高效地利用矩阵的行列升序特性，逐步缩小搜索范围，确保了在O(m + n)的时间复杂度内完成搜索，适用于中等规模的矩阵数据。