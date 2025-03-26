# 347. 前 K 个高频元素
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]

# 为了解决这个问题，我们需要找到整数数组中出现频率前k高的元素。可以使用哈希表统计频率，然后利用堆结构来高效地找到前k高的元素。

# ### 方法思路
# 1. **统计频率**：使用哈希表（字典）统计每个元素的出现次数。
# 2. **维护最小堆**：使用最小堆来维护频率最高的k个元素。
# 每次将元素压入堆中，当堆的大小超过k时，弹出堆顶的最小元素。
# 这样，堆中剩下的元素即为频率最高的k个元素。

### 解决代码
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计元素的频率
        count = Counter(nums)
        # 使用最小堆来维护前k高频率的元素
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        # 提取堆中的元素
        return [num for freq, num in heap]

# ### 代码解释
# 1. **统计频率**：使用`Counter`统计每个元素的出现次数。
# 2. **维护最小堆**：遍历每个元素及其频率，将其压入堆中。当堆的大小超过k时，弹出堆顶元素，确保堆的大小始终不超过k。
# 3. **提取结果**：最后，堆中剩下的元素即为频率最高的k个元素，提取这些元素的数值返回。

# 该方法的时间复杂度为O(n log k)，其中n是数组的长度，k是要返回的元素个数。使用最小堆确保了在处理大规模数据时的高效性。