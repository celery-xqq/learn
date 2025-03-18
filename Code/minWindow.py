# 76. 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 
# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。

# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

#滑动窗口
# 为了解决在字符串 s 中找到涵盖字符串 t 所有字符的最小子串的问题，我们可以使用滑动窗口（双指针）的方法。
# 该方法通过维护两个指针（左右指针）来扩展和收缩窗口，从而高效地找到满足条件的最小窗口。

# 方法思路
# 统计字符需求：首先统计字符串 t 中每个字符的出现次数，存储在字典 need 中。

# 滑动窗口初始化：使用两个指针 left 和 right 分别表示窗口的左右边界，初始化在字符串的起始位置。
# 使用字典 window 来记录当前窗口中各字符的出现次数。

# 扩展窗口：移动右指针 right 扩展窗口，直到窗口包含了 t 的所有字符。

# 收缩窗口：一旦窗口包含了所有字符，尝试移动左指针 left 收缩窗口，同时更新最小窗口的起始位置和长度。

# 验证条件：通过变量 valid 来跟踪当前窗口中满足 t 中字符需求的种类数，当 valid 等于 need 的键的数量时，窗口满足条件。

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        required = len(need)
        
        window = defaultdict(int)
        left = 0
        valid = 0
        min_len = float('inf')
        start = 0
        
        for right in range(len(s)):
            c = s[right]
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == required:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    start = left
                
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return s[start:start + min_len] if min_len != float('inf') else "" 
    
# 代码解释
# 初始化处理：首先检查 t 是否为空字符串，如果是则直接返回空结果。

# 统计字符需求：使用 defaultdict 统计 t 中每个字符的出现次数，并记录需要满足的字符种类数 required。

# 滑动窗口扩展：遍历字符串 s，扩展右指针 right，并更新当前窗口中的字符计数。当某个字符的计数达到 t 中的需求时，增加 valid。

# 滑动窗口收缩：当 valid 等于 required 时，表示当前窗口满足条件，尝试收缩左指针 left 以找到更小的窗口。每次收缩时更新最小窗口的起始位置和长度。

# 结果处理：根据记录的最小窗口起始位置和长度返回结果，如果没有找到符合条件的窗口则返回空字符串。

# 该方法通过滑动窗口高效地在 O(n) 时间复杂度内解决问题，确保每个字符最多被访问两次（一次被右指针扩展，一次被左指针收缩）。