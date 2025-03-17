# -*- coding: utf-8 -*-
# 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

# 示例 1:

# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:

# 输入: nums = [0]
# 输出: [0]

# 为了将数组中的所有零移动到末尾并保持非零元素的相对顺序，可以使用双指针方法。我们维护一个指针 j 来指向当前应放置非零元素的位置。
# 遍历数组时，遇到非零元素就将其交换到 j 的位置，并递增 j。这样可以确保所有非零元素按顺序移动到数组前端，而零元素自然被挤到后面。

# 方法思路
# 初始化指针 j：从数组的起始位置开始。
# 遍历数组：使用指针 i 遍历每个元素。
# 处理非零元素：当遇到非零元素时，如果 i 和 j 不同，则交换 nums[i] 和 nums[j]，然后递增 j。
# 保持顺序：通过交换操作，所有非零元素被依次移动到数组前端，零元素被移动到后面。

def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != j:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums=nums))
