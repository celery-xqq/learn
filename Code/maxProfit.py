# 121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 示例 1：
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2：
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #记录今天之前的最小值，遍历一次就可以
        profit = 0
        cur_min = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit,prices[i]-cur_min)
            cur_min = min(cur_min,prices[i])
        return profit

# 为了解决这个问题，我们需要找到股票买卖的最佳时机，即在某一天买入并在未来的某一天卖出，以获得最大利润。
# 我们可以通过一次遍历数组来高效地解决这个问题。

# ### 方法思路
# 我们可以维护两个变量：`min_price` 和 `max_profit`。
# `min_price` 表示遍历到当前位置时的最低价格，而 `max_profit` 表示当前的最大利润。
# 遍历数组时，对于每一个价格，我们计算当前价格与 `min_price` 的差值，
# 如果这个差值大于 `max_profit`，则更新 `max_profit`。同时，如果当前价格比 `min_price` 更低，
# 则更新 `min_price`。这样只需一次遍历即可解决问题。

### 解决代码
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit

# ### 代码解释
# 1. **边界条件处理**：如果数组长度小于等于1，直接返回0，因为无法进行交易。
# 2. **初始化变量**：`min_price` 初始化为第一个元素的价格，`max_profit` 初始化为0。
# 3. **遍历数组**：从第二个元素开始遍历，计算当前价格与 `min_price` 的差值，更新 `max_profit`。
# 同时，如果当前价格比 `min_price` 低，则更新 `min_price`。
# 4. **返回结果**：遍历结束后，返回 `max_profit`，即最大利润。

# 这种方法的时间复杂度为 O(n)，空间复杂度为 O(1)，能够高效地解决问题。