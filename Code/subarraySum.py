# 560. 和为 K 的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

# 子数组是数组中元素的连续非空序列。

# 示例 1：

# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：

# 输入：nums = [1,2,3], k = 3
# 输出：2

#前缀和+哈希表

# 为了解决统计和为 K 的子数组个数的问题，我们可以利用前缀和和哈希表的方法来高效地解决这个问题。
# 这种方法的时间复杂度为 O(n)，空间复杂度为 O(n)，适用于处理较大的数据量。

# 方法思路
# 前缀和：计算到当前元素为止的前缀和，用于快速计算任意子数组的和。

# 哈希表存储前缀和出现次数：使用哈希表记录每个前缀和出现的次数，这样可以快速查找是否存在满足条件的前缀和。

# 具体步骤如下：

# 初始化一个哈希表 prefix_counts，用于记录前缀和出现的次数。初始时，前缀和为 0 出现一次，这样可以处理从数组开头开始的子数组。

# 遍历数组，累加当前元素到前缀和 current_sum。

# 计算目标前缀和 target = current_sum - k，检查哈希表中是否存在该目标前缀和，如果存在，则将其出现次数累加到结果中。

# 更新哈希表，将当前前缀和的出现次数加一。

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # 初始时前缀和为0出现一次，处理从第一个元素开始的子数组
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            # 检查哈希表中是否存在目标前缀和，存在则累加次数
            count += prefix_counts.get(target, 0)
            # 更新当前前缀和的出现次数
            prefix_counts[current_sum] += 1
        #print(prefix_counts)
        return count

# 代码解释
# 初始化：使用 defaultdict 来初始化哈希表 prefix_counts，并设置初始前缀和 0 出现一次。

# 遍历数组：逐个累加元素到 current_sum，计算当前前缀和。

# 目标前缀和检查：计算 target，检查哈希表中是否存在该值，若存在则累加到结果 count。

# 更新哈希表：将当前前缀和的出现次数记录到哈希表中，以便后续查询。

# 这种方法通过一次遍历数组，高效地统计了所有满足条件的子数组个数，避免了暴力枚举带来的高时间复杂度。
#----------------------------------------------------------------------------------

#升级：找出所有和为 k 的子数组

# 要找出所有和为 k 的子数组，可以通过调整前缀和与哈希表的方法，记录每个前缀和出现的所有位置索引。以下是详细步骤和代码实现：
# 方法思路
# 前缀和与哈希表：维护一个哈希表，键为前缀和，值为该前缀和出现的所有索引列表。
# 动态计算前缀和：遍历数组时，计算当前前缀和，并查找是否存在 target = current_sum - k 的前缀和。
# 收集子数组：若存在 target，则遍历其对应的所有起始索引，记录从这些索引到当前位置的子数组。


def find_subarrays(nums: List[int], k: int) -> List[List[int]]:
    prefix_map = defaultdict(list)
    prefix_map[0].append(-1)  # 初始前缀和为0，位置索引为-1（虚拟位置）
    current_sum = 0
    result = []
    
    for i, num in enumerate(nums):
        current_sum += num
        target = current_sum - k
        # 检查是否存在目标前缀和，并获取所有起始索引
        if target in prefix_map:
            for start_index in prefix_map[target]:
                # 子数组范围：[start_index + 1 ... i]
                subarray = nums[start_index + 1 : i + 1]
                result.append(subarray)
        # 将当前前缀和的索引加入哈希表
        prefix_map[current_sum].append(i)
    #print(prefix_map)
    return result

# 代码解释
# 初始化哈希表：prefix_map 初始时记录前缀和 0 出现在虚拟位置 -1，用于处理从数组开头开始的子数组。
# 遍历数组：逐个元素累加计算当前前缀和 current_sum。
# 查找目标前缀和：计算 target = current_sum - k，若存在，则遍历所有起始索引，生成子数组。
# 记录子数组：根据起始索引和当前位置，切片获取子数组并添加到结果列表。
# 更新哈希表：将当前前缀和的位置索引存入哈希表，供后续查找。

# 示例分析
# 以 nums = [1, 1, 1], k = 2 为例：
# 初始状态：prefix_map = {0: [-1]}, current_sum = 0。
# 处理第一个元素（索引0）：
# current_sum = 1
# target = 1 - 2 = -1（不存在于 prefix_map）
# 更新 prefix_map[1] = [0]

# 处理第二个元素（索引1）：
# current_sum = 2
# target = 2 - 2 = 0（存在，起始索引为 -1）
# 子数组 nums[-1+1 : 1+1] → nums[0:2] = [1, 1]
# 更新 prefix_map[2] = [1]

# 处理第三个元素（索引2）：
# current_sum = 3
# target = 3 - 2 = 1（存在，起始索引为 0）
# 子数组 nums[0+1 : 2+1] → nums[1:3] = [1, 1]
# 更新 prefix_map[3] = [2]
# 最终结果：[[1, 1], [1, 1]]，符合预期。

# 复杂度
# 时间复杂度：O(n) 至 O(n^2)，最坏情况（如全零数组）需要遍历所有可能的起始索引。
# 空间复杂度：O(n)，存储所有前缀和的索引。
# 该方法高效地收集了所有符合条件的子数组，适用于包含正数、负数和零的数组。


#测试
nums = [1,2,3,-1,3,0]
k = 3
solution = Solution()
print(solution.subarraySum(nums,k))

print(find_subarrays(nums,k))