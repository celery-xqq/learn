# 295. 数据流的中位数
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
# MedianFinder() 初始化 MedianFinder 对象。
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
# 示例 1：
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0


# 为了实现数据流的中位数功能，我们可以使用两个堆来高效地维护数据的有序性。
# 具体来说，使用一个大顶堆来保存较小的一半元素，一个小顶堆来保存较大的一半元素。这样可以快速获取中位数。

# ### 方法思路
# 1. **数据结构选择**：使用两个堆，`max_heap` 和 `min_heap`。
# `max_heap` 保存较小的一半元素，`min_heap` 保存较大的一半元素。`max_heap` 中的元素以负数形式存储，以模拟大顶堆。
# 2. **元素插入**：每次插入元素时，先将元素插入 `max_heap`，然后将 `max_heap` 的最大元素移到 `min_heap`。
# 如果 `min_heap` 的大小超过 `max_heap`，则将 `min_heap` 的最小元素移回 `max_heap`，以保持平衡。
# 3. **中位数计算**：根据两个堆的大小关系，中位数可以是两个堆顶的平均值（偶数个元素）或 `max_heap` 的堆顶元素（奇数个元素）。

### 解决代码
import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []  # 保存较小的一半，大顶堆（实际存储负数）
        self.min_heap = []  # 保存较大的一半，小顶堆

    def addNum(self, num: int) -> None:
        # 先将元素插入max_heap
        heapq.heappush(self.max_heap, -num)
        # 将max_heap的最大元素移到min_heap
        max_val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_val)
        # 如果min_heap的大小超过max_heap，调整
        if len(self.min_heap) > len(self.max_heap):
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_val)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

# ### 代码解释
# - **初始化**：创建两个堆 `max_heap` 和 `min_heap`。
# - **添加元素**：每次将元素插入 `max_heap` 后，调整堆的结构，确保 `max_heap` 和 `min_heap` 的大小差不超过1。
# - **计算中位数**：根据两个堆的大小关系返回中位数。若大小相等，返回两堆顶的平均值；否则返回 `max_heap` 的堆顶元素。

# 这种方法确保每次插入操作的时间复杂度为 O(log n)，查询中位数的时间复杂度为 O(1)，能够高效处理动态数据流的中位数问题。