# 73. 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

# 示例 1：
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 示例 2：
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# ### 方法思路
# 为了在不使用额外空间的情况下原地修改矩阵，我们可以利用矩阵的第一行和第一列来记录需要置零的行和列。具体步骤如下：
# 1. **检查首行和首列是否有零**：使用两个变量分别记录首行和首列是否需要置零。
# 2. **遍历矩阵，标记需要置零的行和列**：从第二行和第二列开始遍历，如果发现某个元素为零，则将该行的第一个元素和该列的第一个元素置零。
# 3. **根据标记置零其他元素**：再次遍历矩阵（从第二行和第二列开始），如果该行的第一个元素或该列的第一个元素为零，则将当前元素置零。
# 4. **处理首行和首列**：根据之前记录的变量，决定是否将首行和首列全部置零。

### 解决代码
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        
        # 检查第一行和第一列是否有0
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # 使用第一行和第一列来标记其他行列是否需要置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 根据标记置零其他元素
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 处理第一行
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # 处理第一列
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

# ### 代码解释
# 1. **初始化检查**：首先检查第一行和第一列是否存在零，分别用`first_row_has_zero`和`first_col_has_zero`记录。
# 2. **标记行和列**：从第二行和第二列开始遍历矩阵，如果发现零，就将对应的行首和列首元素置零。
# 3. **应用标记**：再次遍历矩阵，根据行首和列首的标记将相应元素置零。
# 4. **处理首行和首列**：最后根据初始检查的结果，决定是否将首行或首列全部置零。

# 这种方法确保了空间复杂度为O(1)，同时完成了原地修改矩阵的任务。


### 方法思路
# 当允许空间复杂度为O(m+n)时，可以使用两个数组分别记录需要置零的行和列。这种方法更加直观和易于实现：
# 1. **初始化标记数组**：使用一个长度为m的数组`rows`记录需要置零的行，一个长度为n的数组`cols`记录需要置零的列。
# 2. **遍历矩阵标记行列**：遍历矩阵中的每个元素，若元素为0，则标记对应的行和列。
# 3. **根据标记置零**：再次遍历矩阵，若当前行或列被标记，则将元素置零。

### 解决代码
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        rows = [False] * m  # 标记需要置零的行
        cols = [False] * n  # 标记需要置零的列
        
        # 第一次遍历：标记所有包含0的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        # 第二次遍历：根据标记将元素置零
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

# ### 代码解释
# 1. **初始化标记数组**：`rows`和`cols`分别用于记录需要置零的行和列，初始值均为`False`。
# 2. **首次遍历标记**：遍历整个矩阵，当遇到元素为0时，将对应的行和列标记为`True`。
# 3. **二次遍历置零**：再次遍历矩阵，若当前行或列被标记，则将该位置的元素设为0。

# 这种方法通过两次遍历矩阵，时间复杂度为O(m×n)，空间复杂度为O(m+n)，逻辑清晰且易于理解。