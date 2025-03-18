# 49. 字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

# 示例 1:

# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:

# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:

# 输入: strs = ["a"]
# 输出: [["a"]]

#哈希表（先排序）
# 为了解决将字母异位词分组的问题，我们可以利用排序后的字符串作为键来分组。字母异位词排序后会得到相同的字符串，因此可以将排序后的字符串作为键，
# 原字符串作为值存储在字典中。这种方法简单且有效。

# 方法思路
# 排序法：对于每个字符串，将其字符排序后生成一个标准化的键。所有字母异位词排序后的键相同。
# 哈希表：使用哈希表（字典）存储这些键及其对应的字符串列表。键是排序后的字符串，值是该键对应的所有原始字符串。
# 返回结果：将哈希表中的所有值（即分组后的列表）返回。

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

# 代码解释
# 导入模块：使用defaultdict来简化字典的初始化，处理未存在的键。

# 初始化字典：groups字典的键是排序后的字符串，值是对应的原始字符串列表。

# 遍历字符串数组：对每个字符串进行排序，生成标准化键。

# 存储到字典：将原始字符串添加到对应的键的列表中。

# 返回结果：将字典的所有值转换为列表返回，即为分组后的结果。

# 该方法的时间复杂度为O(nk logk)，其中n是字符串数组的长度，k是字符串的最大长度。空间复杂度为O(nk)，用于存储所有字符串。
# 该方法简洁高效，适用于大多数情况。
   
# 测试代码
def test_group_anagrams():
    solution = Solution()
    
    # 测试用例1：标准情况
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.groupAnagrams(strs1)
    # 对每个子列表排序，再整体按首元素排序
    processed_result1 = sorted([sorted(group) for group in result1])
    expected1 = sorted([sorted(["bat"]), sorted(["nat","tan"]), sorted(["ate","eat","tea"])])
    assert processed_result1 == expected1, f"Test case 1 failed: {processed_result1}"

    # 测试用例2：空字符串
    strs2 = [""]
    result2 = solution.groupAnagrams(strs2)
    assert result2 == [[""]], f"Test case 2 failed: {result2}"

    # 测试用例3：单个字符
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    assert result3 == [["a"]], f"Test case 3 failed: {result3}"

    # 测试用例4：全相同异位词
    strs4 = ["listen", "silent", "enlist"]
    result4 = solution.groupAnagrams(strs4)
    print(result4)
    processed_result4 = sorted([sorted(group) for group in result4])
    expected4 = sorted([sorted(["listen", "silent", "enlist"])])
    print(expected4)
    assert processed_result4 == expected4, f"Test case 4 failed: {processed_result4}"

    print("All test cases passed!")

# 执行测试
test_group_anagrams()