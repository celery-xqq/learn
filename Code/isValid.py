# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

# 示例 1：
# 输入：s = "()"
# 输出：true
# 示例 2：
# 输入：s = "()[]{}"
# 输出：true
# 示例 3：
# 输入：s = "(]"
# 输出：false
# 示例 4：
# 输入：s = "([])"
# 输出：true

class Solution:
    def isValid(self, s: str) -> bool:
        #使用栈来解决此类问题
        stack = []
        for a in s:
            if a == '(' or a == '[' or a == '{' :
                stack.append(a)
            if a == ')' or a == ']' or a == '}' :
                if stack :
                    b = stack.pop()
                    if (b == '(' and a == ')') or (b == '[' and a == ']') or (b == '{' and a == '}'):
                        continue
                    else:
                        return False
                else :
                    return False
        #如果stack不为空，说明里面还有元素，代表不是有效的括号；只有stack为空，说明才是有效的括号
        return False if stack else True
    
# ds
# 为了解决判断字符串中的括号是否有效的问题，我们可以利用栈这一数据结构来跟踪左括号，并确保右括号以正确的顺序闭合。具体方法如下：

# ### 方法思路
# 1. **栈的使用**：遍历字符串时，遇到左括号则压入栈中；遇到右括号则检查栈顶的左括号是否与之匹配。
# 2. **映射关系**：通过字典建立右括号到左括号的映射，方便快速查找对应的左括号。
# 3. **边界处理**：处理空字符串时直接返回有效；遇到右括号时若栈为空则直接返回无效。

# ### 解决代码
# def isValid(s: str) -> bool:
#     stack = []
#     mapping = {')': '(', ']': '[', '}': '{'}
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             top = stack.pop()
#             if mapping[char] != top:
#                 return False
#     return not stack

# ### 代码解释
# 1. **初始化栈和映射字典**：`stack`用于存储左括号，`mapping`字典保存右括号到左括号的映射。
# 2. **遍历字符串**：逐个字符处理：
#    - 遇到左括号（在`mapping`的值中），压入栈。
#    - 遇到右括号，检查栈是否为空，若空则无效；否则弹出栈顶元素，检查是否匹配当前右括号。
# 3. **最终检查**：遍历结束后，若栈为空则所有括号正确闭合，返回`True`；否则返回`False`。

# 该方法的时间复杂度为O(n)，空间复杂度为O(n)，其中n为字符串长度。该算法高效且清晰，能够正确处理所有有效括号的边界情况。