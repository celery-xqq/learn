# 189. 轮转数组
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

# 示例 1:
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]

# 示例 2:
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]

#自己的解法：使用stack的解法，就是空间复杂度O(n)
from typing import List
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         len_nums = len(nums)
#         k = k % len_nums
#         if k != 0 and len_nums > 1 :
#             stack = []
#             i = len_nums - k -1
#             while i >= 0 :
#                 stack.append(nums[i])
#                 i-=1
#             i = len_nums - 1
#             while i >= (len_nums - k):
#                 stack.append(nums[i])
#                 i-=1
#             for i in range(len_nums):
#                 nums[i] = stack.pop()

# 为了解决轮转数组的问题，我们可以使用三次反转的方法来实现原地修改数组，从而满足空间复杂度为O(1)的要求。

# 方法思路
# 处理k的值：由于轮转数组k次相当于轮转k % n次（其中n是数组长度），因此首先将k取模以减少不必要的轮转。

# 反转整个数组：将整个数组反转，这样原来的后k个元素会被移动到数组的前面，但顺序是相反的。

# 反转前k个元素：将前k个元素反转，恢复其原来的顺序。

# 反转剩余元素：将剩下的n-k个元素反转，恢复其原来的顺序。

# 这种方法通过三次反转操作，能够高效地完成数组的轮转，时间复杂度为O(n)，空间复杂度为O(1)。

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if n == 0 or k == 0:
            return
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# 代码解释
# 处理k的值：通过取模运算k %= n，将k限制在0到n-1的范围内，避免不必要的轮转。

# 反转整个数组：调用reverse方法，将数组从索引0到n-1的部分反转。

# 反转前k个元素：将前k个元素（索引0到k-1）再次反转，以恢复原来的顺序。

# 反转剩余元素：将剩下的n-k个元素（索引k到n-1）反转，恢复原来的顺序。

# 这种方法通过三次反转操作，高效地实现了数组的原地轮转。