# 55. 跳跃游戏
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

# 为了解决这个问题，我们需要判断是否可以从数组的第一个下标跳跃到最后一个下标。
# 每个元素代表在该位置可以跳跃的最大长度。我们可以通过跟踪当前能到达的最远位置来解决这个问题。

# ### 方法思路
# 1. **初始化最远位置**：从第一个下标开始，初始化最远能到达的位置为0。
# 2. **遍历数组**：对于每个下标，检查当前下标是否在可达范围内。
# 3. **更新最远位置**：如果当前下标可达，更新最远能到达的位置。
# 4. **提前终止**：如果在遍历过程中，最远位置已经覆盖了最后一个下标，则提前返回true。
# 5. **不可达判断**：如果遍历到某个下标时，当前下标超出了最远位置，则说明无法到达最后一个下标，返回false。

from typing import List
### 解决代码
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            current_reach = i + nums[i]
            if current_reach > max_reach:
                max_reach = current_reach
            if max_reach >= n - 1:
                return True
        return max_reach >= n - 1

### 代码解释
# - **初始化变量**：`max_reach`用于记录当前能到达的最远位置，初始化为0。
# - **遍历数组**：使用循环遍历每个元素，检查当前下标是否可达（即`i <= max_reach`）。
# - **更新最远位置**：计算当前下标能到达的最远位置`current_reach`，并更新`max_reach`。
# - **提前终止条件**：如果在遍历中`max_reach`已经覆盖了最后一个下标，直接返回true。
# - **不可达判断**：如果遍历到某个下标时发现该下标不可达，返回false。
# - **最终检查**：遍历结束后，检查是否能到达最后一个下标，确保处理边界情况。

# 这种方法的时间复杂度为O(n)，只需一次遍历数组，空间复杂度为O(1)，效率较高。