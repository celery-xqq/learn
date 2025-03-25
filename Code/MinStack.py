# 155. 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 实现 MinStack 类:
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
# 示例 1:
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

#主栈+辅助栈
# 为了实现一个支持在常数时间内检索到最小元素的栈，我们可以使用辅助栈来跟踪当前的最小值。
# 主栈用于正常的栈操作，而辅助栈的每个元素对应主栈中到该位置的最小值。这样，每次操作的时间复杂度均为O(1)，空间复杂度为O(n)。

# ### 方法思路
# 1. **主栈和辅助栈**：使用两个栈，主栈用于存储所有元素，辅助栈用于存储每个主栈状态下的最小值。
# 2. **push操作**：将元素推入主栈，同时推入当前最小值到辅助栈（当前元素与辅助栈栈顶元素的较小者）。
# 3. **pop操作**：同时弹出主栈和辅助栈的栈顶元素，确保辅助栈栈顶始终是当前主栈的最小值。
# 4. **top操作**：返回主栈的栈顶元素。
# 5. **getMin操作**：返回辅助栈的栈顶元素。

### 解决代码
class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
# ### 代码解释
# - **初始化**：`__init__`方法初始化两个栈，主栈`main_stack`和辅助栈`min_stack`。
# - **push方法**：将元素推入主栈，并根据辅助栈当前状态推入新的最小值（若辅助栈为空则直接推入当前元素，否则推入当前元素与辅助栈栈顶元素的较小者）。
# - **pop方法**：同时弹出主栈和辅助栈的栈顶元素，保持两者同步。
# - **top方法**：返回主栈栈顶元素。
# - **getMin方法**：返回辅助栈栈顶元素，即当前主栈的最小值。

# 这种方法确保了所有操作的时间复杂度为O(1)，并且代码简洁高效。