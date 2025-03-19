# 41. 缺失的第一个正数
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 
# 示例 1：
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。

# 示例 2：
# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。

# 示例 3：
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。

#使用哈希表的暴力解法（c++版本）

# class Solution {
# public:
#     int firstMissingPositive(vector<int>& nums) {
#         unordered_map<int,bool> map;
#         for(int num : nums){
#             map[num]= true;
#         }
#         for(int i = 1; i <= nums.size(); i++){
#             if(map.find(i) == map.end()){
#                 return i;
#             }
#         }
#         return nums.size() + 1;
#     }
# };

# 方法思路
# 为了在O(n)时间复杂度和O(1)空间复杂度内找到缺失的第一个正整数，可以利用数组本身的索引来标记存在的数。具体步骤如下：

# 原地交换：遍历数组，将每个正整数nums[i]交换到其正确的位置nums[nums[i] - 1]。这样，所有在1到n之间的数都会被放置在正确的位置。

# 查找缺失值：再次遍历数组，第一个不满足nums[i] == i + 1的位置即为缺失的最小正整数。如果所有位置都正确，则缺失的是n + 1。

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 将 nums[i] 放到正确的位置，直到无法交换为止
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_pos = nums[i] - 1  # 计算正确的位置
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]  # 交换
        
        # 寻找第一个不符合 nums[i] == i+1 的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1  # 所有位置都正确，返回 n+1
    
# 代码解释
# 遍历交换：通过遍历数组，将每个在1到n范围内的数交换到其正确的位置。这里使用while循环确保交换后的元素也被正确处理。

# 查找缺失值：再次遍历数组，找到第一个索引与值不匹配的位置，返回该索引对应的数。如果所有数都在正确位置，则返回n + 1。

# 这种方法确保了时间复杂度为O(n)，每个元素最多被交换一次，空间复杂度为O(1)，仅使用常数级别的额外空间。