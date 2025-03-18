# 15. 三数之和
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：

# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：

# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。

#双指针
# 为了解决这个问题，我们需要找到所有和为0的三元组，并且确保这些三元组不重复。我们可以通过排序数组和使用双指针的方法来高效地解决这个问题。

# 方法思路
# 排序数组：首先对数组进行排序，这样可以方便后续使用双指针的方法，并且容易跳过重复的元素。

# 遍历固定一个元素：遍历数组中的每个元素作为三元组的第一个元素。

# 双指针寻找另外两个元素：对于每个固定的第一个元素，使用双指针在其后的子数组中寻找另外两个元素，使得三数之和为0。

# 跳过重复元素：在遍历和寻找过程中，跳过重复的元素以避免重复的三元组。
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

# 代码解释
# 排序数组：首先对输入数组进行排序，以便后续处理。

# 遍历固定元素：外层循环遍历每个元素作为三元组的第一个元素，跳过重复的元素以避免重复三元组。

# 双指针寻找另外两个元素：使用左右指针分别指向当前固定元素之后的子数组的两端，计算三数之和并根据和的大小调整指针位置。

# 处理重复元素：当找到满足条件的三元组时，跳过左右指针指向的重复元素，避免重复记录。

# 这种方法的时间复杂度为O(n^2)，其中排序的时间复杂度为O(n log n)，双指针遍历的时间复杂度为O(n^2)，总体满足题目要求的效率。
# 空间复杂度为O(1)（不考虑排序所需的额外空间）。