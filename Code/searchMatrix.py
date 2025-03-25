# 74. 搜索二维矩阵
# 给你一个满足下述两条属性的 m x n 整数矩阵：
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

# 为了高效地确定目标值是否存在于满足特定条件的二维矩阵中，我们可以利用二分查找算法。
# 该矩阵的每一行从左到右非严格递增，并且每一行的第一个元素大于前一行的最后一个元素，因此整个矩阵可以视为一个一维有序数组。以下是具体的解决步骤：

# ### 方法思路
# 1. **矩阵转换为一维索引**：将二维矩阵视为一个一维数组，其中元素按行优先顺序排列。例如，一个m行n列的矩阵可以视为长度为m*n的一维数组。
# 2. **二分查找**：使用二分查找来确定目标值是否存在。计算中间索引对应的行和列，比较中间元素与目标值，调整查找范围直至找到目标值或确定其不存在。

### 解决代码
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            current = matrix[row][col]
            if current == target:
                return True
            elif current < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# ### 代码解释
# 1. **边界检查**：首先检查矩阵是否为空或行是否为空，若为空则直接返回False。
# 2. **初始化变量**：获取矩阵的行数m和列数n，初始化二分查找的左右指针。
# 3. **二分查找循环**：
#    - 计算中间索引mid，并转换为对应的行和列。
#    - 比较中间元素与目标值，若相等则返回True。
#    - 根据比较结果调整查找范围，直到找到目标值或范围无效。
# 4. **返回结果**：若循环结束未找到目标值，返回False。

# 该方法的时间复杂度为O(log(mn))，空间复杂度为O(1)，能够高效地解决问题。