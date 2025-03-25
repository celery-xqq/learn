# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
# 请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]

# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]

# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]

# 为了解决在排序数组中查找目标值的第一个和最后一个位置的问题，我们可以使用两次二分查找来分别确定左边界和右边界。
# 这种方法的时间复杂度为 O(log n)，符合题目要求。

# ### 方法思路
# 1. **左边界查找**：通过二分查找，找到第一个等于目标值的位置。当中间值等于目标值时，继续向左半部分查找以找到第一个出现的位置。
# 2. **右边界查找**：同样通过二分查找，找到最后一个等于目标值的位置。当中间值等于目标值时，继续向右半部分查找以找到最后一个出现的位置。

### 解决代码
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_bound(nums, target, True)
        if left == -1:
            return [-1, -1]
        right = self.find_bound(nums, target, False)
        return [left, right]
    
    def find_bound(self, nums: List[int], target: int, is_left: bool) -> int:
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                if is_left:
                    right = mid - 1  # 继续向左找左边界
                else:
                    left = mid + 1   # 继续向右找右边界
        return res

# ### 代码解释
# 1. **searchRange 方法**：首先调用 `find_bound` 方法查找左边界。如果左边界不存在（返回 -1），则直接返回 [-1, -1]。
# 否则，继续查找右边界，并返回左右边界的数组。
# 2. **find_bound 方法**：根据 `is_left` 参数决定查找左边界还是右边界。
# 在每次中间值等于目标值时，更新结果并调整查找范围，继续向左或向右查找以确定边界位置。

# 这种方法通过两次二分查找高效地确定了目标值的起始和结束位置，确保了时间复杂度为 O(log n)。