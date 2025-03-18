# 3. 无重复字符的最长子串
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

# 示例 1:

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

#滑动窗口
# 为了找出字符串中不含重复字符的最长子串的长度，我们可以使用滑动窗口的方法。
# 该方法通过维护一个窗口，窗口内的字符都是唯一的，并通过调整窗口的起始位置来确保这一点。

# 方法思路
# 滑动窗口：使用两个指针（左指针和右指针）来表示当前窗口的起始和结束位置。

# 哈希表：记录每个字符最近一次出现的位置，以便快速判断当前字符是否在窗口内重复。

# 调整窗口：当发现重复字符时，移动左指针到重复字符的下一个位置，确保窗口内字符唯一。

# 计算最大长度：每次调整窗口后，计算当前窗口的长度并更新最大长度。



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            current_char = s[right]
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            char_map[current_char] = right
            current_length = right - left + 1
            if current_length > max_len:
                max_len = current_length
        return max_len
    
# 代码解释
# 初始化：char_map 用于记录字符的最近位置，max_len 记录最大子串长度，left 表示窗口的左指针。

# 遍历字符串：右指针 right 从0开始遍历字符串。

# 检查重复字符：如果当前字符在 char_map 中存在且其位置在窗口内（即大于等于 left），则将左指针移动到该字符上次出现位置的下一个位置。

# 更新字符位置：将当前字符的位置记录到 char_map 中。

# 计算窗口长度：每次更新窗口后，计算当前窗口的长度并更新最大长度。

# 这种方法的时间复杂度为 O(n)，其中 n 是字符串的长度，每个字符最多被访问两次（左右指针各一次）。
# 空间复杂度为 O(min(m, n))，其中 m 是字符集的大小。