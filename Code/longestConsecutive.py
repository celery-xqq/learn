# 为了找出未排序整数数组中最长连续序列的长度，我们可以利用哈希集合来高效地查询元素是否存在，从而避免排序带来的高时间复杂度。以下是具体的方法：

# 方法思路
# 哈希集合存储元素：将所有元素存入哈希集合中，以便在O(1)时间内查询元素是否存在。

# 寻找连续序列起点：遍历数组中的每个元素，检查当前元素是否为某个连续序列的起点。如果当前元素的前一个元素不在集合中，则当前元素可能是连续序列的起点。

# 扩展连续序列：对于每个可能的起点，向后扩展检查连续的元素是否存在，统计连续序列的长度，并更新最长长度。

# 这种方法确保每个元素最多被访问两次，因此时间复杂度为O(n)，空间复杂度为O(n)。

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
    
# 代码解释
# 哈希集合初始化：将输入数组转换为集合num_set，用于快速查询元素是否存在。

# 遍历集合元素：遍历集合中的每个元素，避免重复处理相同的元素。

# 检查起点：如果当前元素的前一个元素不在集合中，则视为连续序列的起点。

# 扩展序列：从起点开始，逐次检查后续元素是否存在，统计当前连续序列的长度，并更新最长长度。

# 这种方法高效地解决了问题，确保了线性的时间复杂度和空间复杂度。