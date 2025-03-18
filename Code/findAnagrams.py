# 438. 找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 示例 1:

# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  示例 2:

# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

#滑动窗口
# 为了解决这个问题，我们需要找到字符串 s 中所有包含字符串 p 的字母异位词的子串，并返回这些子串的起始索引。
# 字母异位词是指由相同字母重排列形成的子串。

# 方法思路
# 我们可以使用滑动窗口的方法来解决这个问题。具体步骤如下：

# 统计字符频率：首先统计字符串 p 中每个字符的出现次数。

# 初始化滑动窗口：在字符串 s 中维护一个长度等于 p 的滑动窗口，统计初始窗口内每个字符的出现次数。

# 滑动窗口遍历：每次向右移动窗口时，移除左边字符并添加右边字符，同时更新字符频率统计数组。
# 比较当前窗口的字符频率统计与 p 的字符频率统计，如果一致，则记录当前窗口的起始索引。

# 这种方法的时间复杂度为 O(n)，其中 n 是字符串 s 的长度。由于我们使用固定长度的数组来统计字符频率，空间复杂度为 O(1)。

from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return res
        
        p_count = [0] * 26
        window_count = [0] * 26
        
        # 统计p的字符频率
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        
        # 初始化滑动窗口
        for i in range(len_p):
            window_count[ord(s[i]) - ord('a')] += 1
        
        if window_count == p_count:
            res.append(0)
        
        # 滑动窗口
        for i in range(1, len_s - len_p + 1):
            # 移出左边字符
            left_char = s[i - 1]
            window_count[ord(left_char) - ord('a')] -= 1
            # 移入右边字符
            right_char = s[i + len_p - 1]
            window_count[ord(right_char) - ord('a')] += 1
            
            if window_count == p_count:
                res.append(i)
        
        return res
    
# 代码解释
# 初始化字符频率数组：使用两个长度为 26 的数组 p_count 和 window_count 分别统计 p 和滑动窗口内的字符频率。

# 初始窗口统计：遍历 s 的前 len_p 个字符，初始化滑动窗口的字符频率。

# 滑动窗口遍历：从索引 1 开始，每次移动窗口时调整字符频率数组，并比较当前窗口的字符频率是否与 p 的字符频率一致，一致则记录起始索引。

# 这种方法通过滑动窗口和字符频率统计，高效地解决了寻找字母异位词的问题。