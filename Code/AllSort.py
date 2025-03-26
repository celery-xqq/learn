# 常见的排序算法可以分为比较排序和非比较排序两大类，以下是具体的分类及简介：

# ### **1. 比较排序**
# 通过元素之间的比较来确定顺序，时间复杂度通常下限为 (O(nlogn))。

# 1. **冒泡排序 (Bubble Sort)**  
#    - **原理**：重复交换相邻元素，将最大/小元素“冒泡”到末尾。  
#    - **时间复杂度**：平均 (O(n^2))，最优 (O(n))（已排序时）。  
#    - **稳定性**：稳定。

# 2. **选择排序 (Selection Sort)**  
#    - **原理**：每次从未排序部分选择最小/大元素，放到已排序序列末尾。  
#    - **时间复杂度**：固定 (O(n^2))。  
#    - **稳定性**：不稳定（交换可能破坏顺序）。

# 3. **插入排序 (Insertion Sort)**  
#    - **原理**：逐个将未排序元素插入已排序序列的正确位置。  
#    - **时间复杂度**：平均 (O(n^2))，最优 (O(n))（已排序时）。  
#    - **稳定性**：稳定。

# 4. **希尔排序 (Shell Sort)**  
#    - **原理**：改进的插入排序，按递减间隔分组排序，最后全盘插入。  
#    - **时间复杂度**：约 (O(n^{1.3}))，取决于间隔序列。  
#    - **稳定性**：不稳定。

# 5. **归并排序 (Merge Sort)**  
#    - **原理**：分治法，将数组拆分为两半排序后合并。  
#    - **时间复杂度**：固定 (O(nlogn))。  
#    - **稳定性**：稳定。

# 6. **快速排序 (Quick Sort)**  
#    - **原理**：分治法，选取基准元素分区，递归排序左右子数组。  
#    - **时间复杂度**：平均 (O(nlogn))，最坏 (O(n^2))（如已排序）。  
#    - **稳定性**：通常不稳定（取决于分区实现）。

# 7. **堆排序 (Heap Sort)**  
#    - **原理**：构建大顶堆，反复取堆顶元素并调整堆。  
#    - **时间复杂度**：固定 (O(nlogn))。  
#    - **稳定性**：不稳定。


# ### **2. 非比较排序**
# 利用元素特性（如整数范围）进行排序，时间复杂度可突破 (O(nlogn))。

# 8. **计数排序 (Counting Sort)**  
#    - **原理**：统计元素出现次数，直接计算输出位置。  
#    - **适用场景**：整数且范围较小。  
#    - **时间复杂度**：(O(n + k))（k 为数据范围）。

# 9. **桶排序 (Bucket Sort)**  
#    - **原理**：将数据分到多个桶，各桶单独排序后合并。  
#    - **适用场景**：数据分布均匀。  
#    - **时间复杂度**：平均 (O(n + k))（k 为桶数）。

# 10. **基数排序 (Radix Sort)**  
#     - **原理**：按位排序（从低位到高位），需稳定中间排序（如计数排序）。  
#     - **适用场景**：整数或定长字符串。  
#     - **时间复杂度**：(O(n * k))（k 为最大位数）。


# ### **总结**
# - **简单但低效**：冒泡、选择、插入排序（适合小规模数据）。  
# - **高效通用**：归并、快排、堆排序（大规模数据）。  
# - **特殊场景**：计数、桶、基数排序（需满足特定条件）。  

# 每种算法有各自的优缺点，实际应用中需根据数据规模、分布和内存限制选择合适的算法。

# 以下是常见排序算法的 Python 实现代码（附注释和时间复杂度说明）：

### **1. 比较排序算法**

#### **1.1 冒泡排序**
#    - **原理**：重复交换相邻元素，将最大/小元素“冒泡”到末尾。  
#    - **时间复杂度**：平均 (O(n^2))，最优 (O(n))（已排序时）。  
#    - **稳定性**：稳定。
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # 优化：若未交换则提前终止
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# 时间复杂度：平均 O(n²)，最优 O(n)（已排序时）
# 稳定性：稳定

#### **1.2 选择排序**
#    - **原理**：每次从未排序部分选择最小/大元素，放到已排序序列末尾。  
#    - **时间复杂度**：固定 (O(n^2))。  
#    - **稳定性**：不稳定（交换可能破坏顺序）。
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 交换最小元素到已排序末尾
    return arr
# 时间复杂度：O(n²)
# 稳定性：不稳定（交换可能破坏顺序）

#### **1.3 插入排序**
#    - **原理**：逐个将未排序元素插入已排序序列的正确位置。  
#    - **时间复杂度**：平均 (O(n^2))，最优 (O(n))（已排序时）。  
#    - **稳定性**：稳定。
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 待插入元素
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]  # 后移元素
            j -= 1
        arr[j+1] = key  # 插入到正确位置
    return arr
# 时间复杂度：平均 O(n²)，最优 O(n)（已排序时）
# 稳定性：稳定

#### **1.4 希尔排序**
#    - **原理**：改进的插入排序，按递减间隔分组排序，最后全盘插入。  
#    - **时间复杂度**：约 (O(n^{1.3}))，取决于间隔序列。  
#    - **稳定性**：不稳定。
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初始间隔为长度的一半
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # 缩小间隔
    return arr
# 时间复杂度：约 O(n^(1.3))，取决于间隔序列
# 稳定性：不稳定

#### **1.5 归并排序**
#    - **原理**：分治法，将数组拆分为两半排序后合并。  
#    - **时间复杂度**：固定 (O(nlogn))。  
#    - **稳定性**：稳定。
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# 时间复杂度：O(n log n)
# 稳定性：稳定

#### **1.6 快速排序**
#    - **原理**：分治法，选取基准元素分区，递归排序左右子数组。  
#    - **时间复杂度**：平均 (O(nlogn))，最坏 (O(n^2))（如已排序）。  
#    - **稳定性**：通常不稳定（取决于分区实现）。
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择中间元素为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# 时间复杂度：平均 O(n log n)，最坏 O(n²)
# 稳定性：不稳定

#### **1.7 堆排序**
#    - **原理**：构建大顶堆，反复取堆顶元素并调整堆。  
#    - **时间复杂度**：固定 (O(nlogn))。  
#    - **稳定性**：不稳定。
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    # 建堆
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    # 逐个提取堆顶元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
# 时间复杂度：O(n log n)
# 稳定性：不稳定

### **2. 非比较排序算法**

#### **2.1 计数排序**
#    - **原理**：统计元素出现次数，直接计算输出位置。  
#    - **适用场景**：整数且范围较小。  
#    - **时间复杂度**：(O(n + k))（k 为数据范围）。
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    return result
# 时间复杂度：O(n + k)（k 是数据范围）
# 适用场景：整数且范围较小

#### **2.2 桶排序**
#    - **原理**：将数据分到多个桶，各桶单独排序后合并。  
#    - **适用场景**：数据分布均匀。  
#    - **时间复杂度**：平均 (O(n + k))（k 为桶数）。
def bucket_sort(arr, bucket_size=5):
    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    # 分桶
    for num in arr:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)
    # 各桶排序后合并
    result = []
    for bucket in buckets:
        insertion_sort(bucket)  # 使用插入排序或其他简单排序
        result.extend(bucket)
    return result
# 时间复杂度：平均 O(n + k)（k 为桶数）
# 适用场景：数据分布均匀

#### **2.3 基数排序**
#     - **原理**：按位排序（从低位到高位），需稳定中间排序（如计数排序）。  
#     - **适用场景**：整数或定长字符串。  
#     - **时间复杂度**：(O(n * k))（k 为最大位数）。
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting = [0] * 10  # 0-9 十进制
        output = [0] * len(arr)
        # 统计频次
        for num in arr:
            digit = (num // exp) % 10
            counting[digit] += 1
        # 计算累积位置
        for i in range(1, 10):
            counting[i] += counting[i-1]
        # 反向填充保证稳定性
        for i in range(len(arr)-1, -1, -1):
            digit = (arr[i] // exp) % 10
            output[counting[digit] - 1] = arr[i]
            counting[digit] -= 1
        arr = output
        exp *= 10
    return arr
# 时间复杂度：O(n * k)（k 为最大位数）
# 适用场景：整数或定长字符串


# ### **代码说明**
# 1. **稳定性**：归并、插入、冒泡、计数、基数排序是稳定的；其他如快排、堆排序等不稳定。
# 2. **适用场景**：
#    - 小规模数据：插入排序（已接近有序时性能好）。
#    - 大规模通用数据：快排、归并、堆排序。
#    - 特殊场景：计数、桶、基数排序需要满足特定条件。