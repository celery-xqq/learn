# 215. 数组中的第K个最大元素
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 示例 1:
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 示例 2:
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4


# 要解决这个问题，我们需要找到数组中第k个最大的元素，并且要求算法的时间复杂度为O(n)。
# 快速选择算法（Quickselect）是一个合适的选择，因为它基于快速排序的分区思想，能够在平均情况下达到O(n)的时间复杂度。

# ### 方法思路
# 快速选择算法的核心思想是分而治之。通过选择一个基准值（pivot），将数组分成两部分：
# 左边的元素都大于等于基准值，右边的元素都小于基准值。然后根据基准值的位置与k的关系，决定继续在左边还是右边部分进行查找。
# 为了确保平均时间复杂度为O(n)，我们随机选择基准值以避免最坏情况下的性能退化。

### 解决代码(最后一个用例超时了，处理不了大量重复元素)
import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            # 随机选择pivot并交换到末尾
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            i = left - 1
            for j in range(left, right):
                if nums[j] >= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[right] = nums[right], nums[i + 1]
            return i + 1
        
        def quickselect(left, right, k):
            if left == right:
                return nums[left]
            p = partition(left, right)
            m = p - left + 1
            if m == k:
                return nums[p]
            elif m > k:
                return quickselect(left, p - 1, k)
            else:
                return quickselect(p + 1, right, k - m)
        
        return quickselect(0, len(nums) - 1, k)

# ### 代码解释
# 1. **partition函数**：随机选择一个基准值并将其交换到数组末尾。
# 然后遍历数组，将大于等于基准值的元素移到左边，小于基准值的元素移到右边。
# 最后将基准值放到正确的位置，并返回该位置索引。
# 2. **quickselect函数**：递归地进行分区操作。根据基准值的位置判断第k大的元素在左边还是右边部分。
# 如果基准值的位置正好是k，则直接返回；否则在相应的子数组中继续查找。

# 通过这种方法，我们能够在平均情况下以O(n)的时间复杂度找到第k个最大的元素。
# 随机选择基准值确保了算法在绝大多数情况下都能高效运行，避免了最坏情况下的性能问题。
# -----------------------------------------------------------------------

# 您的问题非常有洞察力！确实，**快速排序**的平均时间复杂度为 (O(nlogn))，但 **快速选择（Quickselect）** 算法是它的一个变种，
# 其平均时间复杂度可以达到 (O(n))。以下是详细解释：

# ### **快速选择与快速排序的核心区别**
# 1. **快速排序**：
#    - 每次选择一个基准值（pivot），将数组分为两部分（左边 ≤ pivot，右边 ≥ pivot）。
#    - **递归处理左右两部分**，直到整个数组有序。
#    - 时间复杂度：平均 (O(nlogn))，最坏 (O(n^2))。

# 2. **快速选择**：
#    - 目标不是排序，而是**找到第 k 大的元素**。
#    - 每次分区后，**只递归处理包含目标的子数组**（左边或右边），放弃另一部分。
#    - 时间复杂度：平均 (O(n))，最坏 (O(n^2))（但通过随机化 pivot 可避免）。

# ---

# ### **时间复杂度分析**
# 假设每次分区将数组分为两部分，比例为 (1:1)（理想情况）：
# 1. 第 1 次分区操作次数：(n)
# 2. 第 2 次分区操作次数：(n/2)
# 3. 第 3 次分区操作次数：(n/4)
# 4. 总操作次数：(n + n/2 + n/4 + ... <= 2n)

# 因此，**总时间复杂度为 (O(n))**。

# ---

# ### **为什么快速选择是 O(n)？数学证明**
# 每次递归的数据量是上一次的约一半，总操作次数为：
# n + n/2 + n/2 + ... = n (1 + 1/2 + 1/4 + ...) = 2n

# 这是一个等比数列求和，收敛到 (2n)，即时间复杂度为 (O(n))。

# ---

# ### **代码关键点解释**
# 1. **随机选择 pivot**：
#    pivot_index = random.randint(left, right)
#    避免最坏情况（如数组已有序时固定选末尾元素），确保平均时间复杂度。

# 2. **分区逻辑**：
#    - 将大于等于 pivot 的元素移到左侧。
#    - 最终 `p` 是 pivot 的位置，左侧有 `m = p - left + 1` 个元素。
#    - 如果 `m == k`，说明 `nums[p]` 是第 `k` 大的元素；否则递归处理左或右子数组。

# 3. **递归终止条件**：
#    if left == right:
#        return nums[left]
#    当子数组长度为 1 时直接返回。

# ---

# ### **示例验证**
# 以示例 1 `[3,2,1,5,6,4], k=2` 为例：
# 1. 排序后的数组为 `[6,5,4,3,2,1]`，第 2 大元素是 `5`。
# 2. 代码通过快速选择找到 `5`，验证正确。

# ---

# ### **总结**
# - **快速选择**通过每次舍弃一半数据，将平均时间复杂度优化到 (O(n))。
# - **随机化 pivot** 是关键，避免最坏情况。
# - 您的质疑非常合理，但快速选择与快速排序的本质差异在于**只处理单边递归**，因此时间复杂度更低。

#===========================================================================
#下面代码可以通过leetcode，请你分析下:
# 这段代码使用改进的快速选择算法（Quickselect）来高效地找到数组中第 k 大的元素。
# 其核心思路是通过随机选择基准值（pivot），将数组划分为三个部分（大于、等于、小于 pivot），
# 并根据这三部分的长度与 k 的关系递归缩小搜索范围。以下是详细分析：

# # ---

# ### **算法步骤**
# 1. **随机选择基准值**  
#    每次递归时，从当前数组中随机选择一个元素作为 `pivot`，避免固定选择导致的最坏时间复杂度。

# 2. **三向分区**  
#    遍历数组，将元素分为三类：
#    - `big`：所有大于 `pivot` 的元素。
#    - `equal`：所有等于 `pivot` 的元素。
#    - `small`：所有小于 `pivot` 的元素。

# 3. **递归逻辑**  
#    - 如果 `k <= len(big)`：第 k 大元素在 `big` 中，递归处理 `big`。
#    - 如果 `k > len(big) + len(equal)`：第 k 大元素在 `small` 中，调整 `k` 后递归处理 `small`。
#    - 否则：第 k 大元素在 `equal` 中，直接返回 `pivot`。

# ---

# ### **时间复杂度**
# - **平均情况**：每次分区将数据规模减少约一半，时间复杂度为 (O(n))。  
#   数学期望为 (n + n/2 + n/4 + ... <= 2n)。
# - **最坏情况**：理论上可能退化到 (O(n^2))，但随机选择基准值使得概率极低。

# ---

# ### **空间复杂度**
# - **额外空间**：每次递归需创建 `big`、`equal`、`small` 三个列表，最坏情况下空间复杂度为 (O(n))。  
#   但在实际运行中，每次递归仅处理一个子数组，其他部分会被释放，实际占用空间接近 (O(n))。

# ---

# ### **代码正确性验证**
# #### **示例 1**
# 输入：`nums = [3,2,1,5,6,4], k = 2`  
# 1. 假设选中 `pivot=5`，分区为 `big=[6]`，`equal=[5]`，`small=[3,2,1,4]`。
# 2. 由于 `k=2`，且 `len(big)=1 < 2`，检查 `len(nums)-len(small)=6-4=2`，此时 `k <= 2`，返回 `pivot=5`。

# #### **示例 2**
# 输入：`nums = [3,2,3,1,2,4,5,5,6], k=4`  
# 1. 第一次递归可能选中 `pivot=3`，分区为 `big=[5,5,6,4]`，`equal=[3,3]`，`small=[2,1,2]`。
# 2. `k=4 <= len(big)=4`，递归处理 `big`。
# 3. 在 `big=[5,5,6,4]` 中，可能选中 `pivot=5`，分区为 `big=[6]`，`equal=[5,5]`，`small=[4]`。
# 4. 此时 `k=4`，`len(big)=1 < 4`，但 `len(nums)-len(small)=4-1=3 < 4`，进入 `small` 处理，调整 `k=4-3=1`。
# 5. 在 `small=[4]` 中直接返回 `4`。

# ---

# ### **优点**
# 1. **随机化避免最坏情况**  
#    通过 `random.choice(nums)` 选择基准值，避免有序数组导致的分区失衡。
# 2. **三向分区处理重复元素**  
#    直接跳过等于 `pivot` 的元素，减少递归深度。
# 3. **逻辑简洁清晰**  
#    通过分治思想逐步缩小搜索范围，代码直观易理解。

# ---

# ### **潜在改进点**
# 1. **空间优化**  
#    当前实现需要额外存储三个列表，可改为原地分区（如三指针法），将空间复杂度优化至 (O(1))。
# 2. **尾递归优化**  
#    将递归改为迭代形式，避免栈溢出风险。

# ---

# ### **总结**
# 该代码通过随机选择基准值和三向分区的策略，巧妙地解决了快速选择算法在处理重复元素和有序数组时的效率问题。
# 尽管在空间复杂度上有优化空间，但其时间复杂度在工程实践中已足够高效，能够通过 LeetCode 的所有测试用例。
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot
        
        return quick_select(nums, k)

# 作者：Krahets
# 链接：https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/2361969/215-shu-zu-zhong-de-di-k-ge-zui-da-yuan-d786p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
#==========================================================================================
### **算法实现**
# 以下是结合快速选择和三向切分（荷兰国旗算法）的优化实现，时间复杂度严格为 (O(n))，空间复杂度 (O(1))：

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        
        while True:
            if left == right:
                return nums[left]
            
            # 随机选择pivot，并交换到末尾
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot = nums[right]
            
            # 三向切分（荷兰国旗算法）
            i, j, m = left, left, right - 1  # i:左边界，j:当前指针，m:右边界
            while j <= m:
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] < pivot:
                    nums[j], nums[m] = nums[m], nums[j]
                    m -= 1
                else:
                    j += 1
            
            # 将pivot放回正确位置
            nums[j], nums[right] = nums[right], nums[j]
            
            # 计算各区域长度
            left_len = i - left          # 大于pivot的元素数量
            mid_len = j - i + 1          # 等于pivot的元素数量
            
            if k <= left_len:            # 目标在左区
                right = i - 1
            elif k <= left_len + mid_len: # 目标在中区
                return pivot
            else:                        # 目标在右区
                k -= (left_len + mid_len)
                left = j + 1

# ### **核心优化解析**
# 1. **随机选择基准值（Pivot）**  
#    pivot_idx = random.randint(left, right)
#    避免固定选择中间元素或首尾元素，防止有序数组下的最坏时间复杂度。

# 2. **三向切分（Dutch National Flag）**  
#    while j <= m:
#        if nums[j] > pivot:
#            nums[i], nums[j] = nums[j], nums[i]
#            i += 1
#            j += 1
#        elif nums[j] < pivot:
#            nums[j], nums[m] = nums[m], nums[j]
#            m -= 1
#        else:
#            j += 1
#    - 将数组分为三部分：  
#      - `[left, i-1]`：**大于** pivot 的元素  
#      - `[i, m]`：**等于** pivot 的元素  
#      - `[m+1, right]`：**小于** pivot 的元素  
#    - 时间复杂度从 (O(n^2)) 优化到 (O(n))（尤其适用于重复元素多的场景）。

# 3. **原地分区与空间优化**  
#    - 所有操作直接在原数组上进行，无需额外空间，空间复杂度为 (O(1))。

# 4. **动态调整搜索范围**  
#    if k <= left_len:
#        right = i - 1
#    elif k <= left_len + mid_len:
#        return pivot
#    else:
#        k -= (left_len + mid_len)
#        left = j + 1
#    - 根据左区长度 `left_len` 和中区长度 `mid_len` 动态调整 `k` 和搜索范围。

# ---

# ### **时间复杂度分析**
# | 场景               | 时间复杂度 | 原因                     |
# |--------------------|------------|--------------------------|
# | 平均情况           | (O(n))   | 每次分区减少约一半数据量  |
# | 全相同元素         | (O(n))   | 三向切分直接定位到中区    |
# | 完全有序数组       | (O(n))   | 随机选择 pivot 避免劣化   |
# | 大量重复元素       | (O(n))   | 三向切分跳过重复元素      |

# ---

# ### **极端用例验证**
# 1. **全相同元素**  
#    nums = [5] * 10^6, k = 1
#    - 一次分区即定位到中区，直接返回 `5`，时间复杂度 (O(n))。

# 2. **完全逆序数组**  
#    nums = list(range(10^6, 0, -1)), k = 500000
#    - 随机选择 pivot 确保平均分割，时间复杂度稳定在 (O(n))。

# 3. **大量重复元素**  
#    nums = [3,2,3,1,2,4,5,5,6], k=4
#    - 通过三向切分跳过重复的 `3` 和 `5`，直接定位到目标区域。

# ---

# ### **总结**
# 该算法通过 **随机化基准值选择** 和 **三向切分优化**，确保了在各类极端场景下的高效性，
# 严格满足时间复杂度 (O(n)) 和空间复杂度 (O(1)) 的要求。
        