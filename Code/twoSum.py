# -*- coding: utf-8 -*-
#两数之和：
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