# 53. 最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。

# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

# 示例 2：
# 输入：nums = [1]
# 输出：1

# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23

# 要解决这个问题，我们需要找到一个整数数组中具有最大和的连续子数组。
# 这个问题可以通过动态规划或Kadane算法高效地解决，时间复杂度为O(n)，空间复杂度为O(1)。

# 方法思路
# 算法的核心思想是维护两个变量：current_max和max_sum。current_max表示以当前元素结尾的最大子数组和，
# 而max_sum用于记录遍历过程中遇到的最大子数组和。对于每个元素，我们有两种选择：
# 要么将其作为新子数组的起点，要么将其加入前面的子数组。通过比较这两种选择的结果，我们可以逐步更新current_max和max_sum。

# 具体步骤如下：

# 初始化current_max和max_sum为数组的第一个元素。

# 从数组的第二个元素开始遍历，对于每个元素，更新current_max为当前元素值和当前元素值加上之前的current_max的较大者。

# 每次更新后，检查是否需要更新max_sum。

# 遍历结束后，max_sum即为所求的最大子数组和。
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = max_sum = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
        return max_sum
    
# 代码解释
# 初始化：将current_max和max_sum初始化为数组的第一个元素，因为初始时最大子数组只能是第一个元素本身。

# 遍历数组：从第二个元素开始遍历数组，对于每个元素，计算以该元素结尾的最大子数组和，并更新current_max。
# 这一步通过比较当前元素值与前一个current_max加上当前元素值的和来实现。

# 更新最大值：每次更新current_max后，检查是否需要更新全局最大值max_sum。

# 返回结果：遍历结束后，max_sum即为整个数组中的最大子数组和。

# 这种方法高效且简洁，能够在O(n)的时间复杂度内解决问题，适用于处理大规模数组。