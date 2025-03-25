# 4. 寻找两个正序数组的中位数
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。

# 示例 1：
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2

# 示例 2：
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5


# 为了找到两个正序数组的中位数并满足时间复杂度要求，我们可以使用二分查找的方法。
# 关键在于找到两个数组的分割点，使得分割后的左右两部分满足特定条件，从而快速确定中位数。

# ### 方法思路
# 1. **确保数组长度关系**：将较短的数组作为第一个数组，以减少二分查找的次数。
# 2. **二分查找分割点**：在较短的数组中进行二分查找，确定分割点i，使得两个数组的左半部分总长度等于总长度的一半或一半加一。
# 3. **处理边界条件**：检查分割点附近的元素是否满足条件，即左半部分的最大值小于等于右半部分的最小值。
# 4. **计算中位数**：根据总长度的奇偶性，返回相应的中位数。

### 解决代码

def findMedianSortedArrays(nums1, nums2):
    # 确保nums1是较短的数组
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    total_half = (m + n + 1) // 2
    
    while left <= right:
        i = (left + right) // 2
        j = total_half - i
        
        # 处理j可能的越界情况
        if j < 0:
            right = i - 1
            continue
        if j > n:
            left = i + 1
            continue
        
        # 处理分割点左右的元素
        a_left_max = nums1[i-1] if i > 0 else -float('inf')
        a_right_min = nums1[i] if i < m else float('inf')
        b_left_max = nums2[j-1] if j > 0 else -float('inf')
        b_right_min = nums2[j] if j < n else float('inf')
        
        if a_left_max <= b_right_min and b_left_max <= a_right_min:
            if (m + n) % 2 == 1:
                return max(a_left_max, b_left_max)
            else:
                return (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2
        elif a_left_max > b_right_min:
            right = i - 1
        else:
            left = i + 1
    
    return 0.0  # 根据题目约束，此处不会执行

# ### 代码解释
# 1. **确保数组长度关系**：通过交换数组，确保`nums1`是较短的数组，以减少二分查找的次数。
# 2. **二分查找分割点**：使用二分查找确定分割点`i`，并计算对应的`j`，使得左右两部分的长度满足条件。
# 3. **处理边界条件**：检查分割点的左右元素，处理可能的越界情况，确保比较时不会出现无效索引。
# 4. **计算中位数**：根据总长度的奇偶性，返回左半部分的最大值或左右部分最小值的平均数。
# 该方法通过二分查找将时间复杂度控制在O(log(min(m, n))，满足题目要求。