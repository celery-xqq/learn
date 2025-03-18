# -*- coding: utf-8 -*-

# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

# 你可以按任意顺序返回答案。

 

# 示例 1：

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：

# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：

# 输入：nums = [3,3], target = 6
# 输出：[0,1]

#哈希
# 要解决这个问题，我们需要在一个整数数组中找到两个数，使得它们的和等于给定的目标值，并返回它们的数组下标。
# 我们可以通过使用哈希表来优化查找过程，从而实现高效的时间复杂度。

# 方法思路
# 问题分析：我们需要找到两个不同的元素，它们的和等于目标值。直接暴力解法的时间复杂度为O(n²)，不够高效。使用哈希表可以将时间复杂度优化到O(n)。

# 哈希表使用：遍历数组，对于每个元素，计算其补数（即目标值减去当前元素值）。检查补数是否存在于哈希表中。如果存在，则返回补数的下标和当前元素的下标；
# 如果不存在，则将当前元素的值及其下标存入哈希表。

# 避免重复使用元素：通过先检查补数是否存在再将当前元素存入哈希表，确保不会重复使用同一个元素。
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []

# 代码解释
# 初始化哈希表：使用字典hash_map存储元素值和对应的下标。

# 遍历数组：使用enumerate遍历数组，同时获取元素值和下标。

# 计算补数：对于当前元素num，计算其补数complement。

# 检查补数存在性：若补数存在于哈希表中，直接返回结果；否则将当前元素存入哈希表。

# 返回结果：由于题目保证有解，无需处理无解情况。

# 该方法通过一次遍历和哈希表的O(1)查找，确保时间复杂度为O(n)，空间复杂度为O(n)，高效地解决了问题。

test_cases = [
    (([2,7,11,15], 9), [0,1]),
    (([3,3], 6), [0,1]),
    (([3,2,4], 6), [1,2]),
    (([-1,0,2,4], -1), [0,1]),
    (([1000000, -1000000], 0), [0,1]),
    (([1,2,3,4], 5), [[0,3], [1,2]]),  # 允许两种答案
    (([3,2,4], 6), [1,2]),
    (([i for i in range(1,10001)], 19999), [9998,9999]),
    (([0,4,3,0], 0), [0,3]),
    (([10,15,5,2,7], 9), [3,4])
]

solution = Solution()
for (nums, target), expected in test_cases:
    result = solution.twoSum(nums, target)
    if isinstance(expected[0], list):  # 处理多解情况
        assert result in expected, f"Failed: {nums}, {target} -> {result}"
    else:
        assert result == expected, f"Failed: {nums}, {target} -> {result}"
print("All tests passed!")