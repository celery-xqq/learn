# 11. 盛最多水的容器
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 返回容器可以储存的最大水量。

# 说明：你不能倾斜容器


# 要解决这个问题，我们需要找到两个垂线，使得它们与 x 轴共同构成的容器可以容纳最多的水。容器的储水量由两个因素决定：两个垂线之间的距离（宽度）和两个垂线中较短的那个的高度。储水量即为宽度乘以高度。

# 方法思路
# 我们可以使用双指针方法来高效地解决这个问题。具体步骤如下：

# 初始化指针：使用两个指针 left 和 right，分别指向数组的起始位置和末尾位置。

# 计算当前面积：在每次循环中，计算当前指针所指的两个垂线构成的容器的面积，并更新最大面积。

# 移动指针：比较两个指针所指的高度，移动高度较小的那个指针，以期望找到更高的高度，从而可能在后续步骤中得到更大的面积。

# 通过这种方法，我们可以在 O(n) 的时间复杂度内找到最大储水量，其中 n 是数组的长度。这种方法避免了暴力法中的重复计算，显著提高了效率。
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])
            current_area = current_width * current_height
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        