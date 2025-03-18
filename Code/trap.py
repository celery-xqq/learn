# 42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9

#双指针

# 要解决接雨水的问题，可以采用双指针法来高效地计算储水量。该方法通过左右指针向中间移动，动态维护左右两侧的最大高度，
# 从而在一次遍历内完成计算，时间复杂度为O(n)，空间复杂度为O(1)。

# 方法思路
# 初始化指针和变量：使用左右指针分别指向数组的起始和末尾，并维护左右两侧的最大高度。
# 比较指针处的高度：每次移动较小高度的指针，因为较小高度的一侧决定了当前的储水潜力。
# 更新最大高度和储水量：如果当前指针处的高度大于等于对应侧的最大高度，则更新最大高度；否则计算当前储水量并累加。
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = right_max = res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res
    
# 代码解释
# 初始化：左右指针分别指向数组头和尾，left_max和right_max初始化为0，用于记录左右两侧的最大高度，res用于累计储水量。
# 循环移动指针：当左指针小于右指针时，比较两指针处的高度，移动较小高度的指针。
# 更新和计算储水量：
# 如果当前指针处的高度大于等于对应侧的最大高度，则更新该侧的最大高度。
# 否则，计算当前指针处的储水量（最大高度减去当前高度）并累加到结果中。
# 返回结果：循环结束后返回累计的储水量。
# 该方法高效且节省空间，能够快速解决问题。