# 239. 滑动窗口最大值
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。

# 示例 1：

# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 示例 2：

# 输入：nums = [1], k = 1
# 输出：[1]

#单调队列
# 为了解决滑动窗口最大值的问题，我们可以使用双端队列（deque）来高效地维护当前窗口中的最大值。
# 这种方法的时间复杂度为O(n)，每个元素最多被处理两次（入队和出队各一次），从而保证了高效的性能。

# 方法思路
# 双端队列维护窗口最大值：使用双端队列存储数组元素的索引，队列中的索引对应的元素值单调递减。队列的第一个元素始终是当前窗口的最大值。

# 移除窗口外元素：每次移动窗口时，检查队列中的第一个元素是否还在当前窗口范围内，如果不在则将其移除。

# 维护单调队列：当新元素进入窗口时，从队列尾部开始移除所有比当前元素小的元素，因为这些元素不可能是当前或后续窗口的最大值。

# 记录结果：当窗口形成后（即遍历到第k个元素及以后），将队列首元素对应的值作为当前窗口的最大值。
from collections import deque
from collections import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        for i in range(len(nums)):
            # 移除不在当前窗口内的队首元素
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            # 移除队尾所有小于当前元素的索引
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            # 当窗口形成后，记录结果
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
    
# 代码解释
# 初始化双端队列和结果数组：使用deque来维护当前窗口中的最大值索引，result存储每个窗口的最大值。

# 遍历数组：逐个处理数组中的每个元素。

# 移除窗口外元素：检查队列首元素是否在当前窗口的范围内，不在则移除。

# 维护单调队列：确保队列中的元素对应的值是单调递减的，新元素若比队尾元素大，则移除队尾元素，直到队列重新满足单调递减条件。

# 记录窗口最大值：当窗口形成后（即遍历到第k个元素及以后），队列首元素即为当前窗口的最大值，将其加入结果数组。

# 这种方法通过高效的双端队列操作，确保了线性时间复杂度，适用于处理大规模数据。