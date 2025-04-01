Python 支持多种内置数据类型，主要分为 **可变类型** 和 **不可变类型**。以下是常见的数据类型分类及示例：

---

### 一、不可变类型（创建后不可修改）
1. **数字类型 (Numeric Types)**
   - **`int`**：整数（如 `5`, `-3`, `1000`）
   - **`float`**：浮点数（如 `3.14`, `-2.5`）
   - **`complex`**：复数（如 `1+2j`）
   - **`bool`**：布尔值（`True` 或 `False`，是 `int` 的子类）

2. **字符串 (`str`)**
   - 文本数据，用单引号或双引号定义（如 `"hello"`, `'Python'`）。

3. **元组 (`tuple`)**
   - 有序不可变序列，用圆括号定义（如 `(1, "a", 3.14)`）。
   - 单元素元组需加逗号：`(1,)`。

4. **冻结集合 (`frozenset`)**
   - 不可变的集合（如 `frozenset([1, 2, 3])`）。

---

### 二、可变类型（创建后可修改）
1. **列表 (`list`)**
   - 有序可变序列，用方括号定义（如 `[1, "a", True]`）。
   - 支持增删改操作。

2. **字典 (`dict`)**
   - 键值对集合，用花括号定义（如 `{"name": "Alice", "age": 25}`）。
   - **键必须是不可变类型**（如字符串、数字、元组）。

3. **集合 (`set`)**
   - 无序唯一元素集合，用花括号或 `set()` 创建（如 `{1, 2, 3}`）。
   - 常用于去重和集合运算。

4. **字节数组 (`bytearray`)**
   - 可变的字节序列（如 `bytearray(b"hello")`）。

---

### 三、其他类型
1. **空值 (`NoneType`)**
   - 只有一个值 `None`，表示空或无返回值。

2. **二进制数据 (`bytes`)**
   - 不可变的字节序列（如 `b"hello"`）。

3. **自定义类型**
   - 通过类（`class`）自定义对象类型。

---

### 四、类型示例及特点
| 类型       | 示例               | 可变性   | 特点                           |
|------------|--------------------|----------|--------------------------------|
| `int`      | `42`              | 不可变   | 整数运算                       |
| `str`      | `"Python"`        | 不可变   | 支持切片、拼接                |
| `list`     | `[1, 2, 3]`       | 可变     | 灵活增删改                   |
| `tuple`    | `(1, "a")`        | 不可变   | 轻量级，适合固定数据          |
| `dict`     | `{"key": "value"}`| 可变     | 快速键值查找                  |
| `set`      | `{1, 2, 3}`       | 可变     | 元素唯一，无序                |
| `NoneType` | `None`            | -        | 表示空值                      |

---

### 五、类型检查与转换
- **检查类型**：用 `type()` 或 `isinstance()` 函数。
  ```python
  print(type(5))          # <class 'int'>
  print(isinstance(5, int))  # True
  ```

- **类型转换**：
  ```python
  str(3)     # "3"
  int("42")  # 42
  list("abc") # ['a', 'b', 'c']
  ```

---

### 六、关键区别
- **可变 vs 不可变**：  
  不可变类型（如字符串、元组）在修改时会创建新对象，而可变类型（如列表、字典）直接修改原对象。
- **哈希性**：  
  不可变类型可哈希（可用作字典键），可变类型不可哈希。

掌握这些类型及其特性，能帮助你更高效地处理数据！


在 Python 中，函数使用 **`def`** 关键字定义，基本语法如下：

```python
def 函数名(参数列表):
    """函数文档字符串（可选）"""
    函数体代码
    return 返回值  # 可选（无return则返回None）
```

---

### 一、基础函数定义示例

#### 1. 无参数、无返回值的函数
```python
def greet():
    print("Hello, World!")

greet()  # 调用函数，输出：Hello, World!
```

#### 2. 带参数的函数
```python
def add(a, b):
    return a + b

result = add(3, 5)  # 调用并接收返回值
print(result)       # 输出：8
```

#### 3. 带默认参数的函数
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 输出：9（默认 exponent=2）
print(power(2, 3))  # 输出：8
```

---

### 二、高级用法

#### 1. 可变参数（*args 和 **kwargs）
```python
# *args 接收任意数量的位置参数（元组）
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))  # 输出：6

# **kwargs 接收任意数量的关键字参数（字典）
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  # 输出：name: Alice \n age: 25
```

#### 2. 类型提示（Type Hints，Python 3.5+）
```python
def multiply(a: int, b: int) -> int:
    """返回两个整数的乘积"""
    return a * b

print(multiply(3, 4))  # 输出：12
```

---

### 三、注意事项
1. **缩进必须一致**：函数体代码必须缩进（通常用4个空格）。
2. **函数名规范**：遵循小写下划线命名（如 `calculate_sum`）。
3. **默认参数陷阱**：默认参数如果是可变对象（如列表、字典），需谨慎使用！
   ```python
   # 错误示例（默认参数为列表）
   def append_to_list(value, lst=[]):
       lst.append(value)
       return lst

   print(append_to_list(1))  # [1]
   print(append_to_list(2))  # [1, 2]（默认列表会被重复使用！）

   # 正确写法：用 None 替代
   def append_to_list(value, lst=None):
       if lst is None:
           lst = []
       lst.append(value)
       return lst
   ```

---

### 四、匿名函数（Lambda）
适用于简单操作，语法：`lambda 参数: 表达式`
```python
square = lambda x: x ** 2
print(square(5))  # 输出：25

# 常用于排序、过滤等场景
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)  # 输出：[4, 3, 2, 1]
```

---

### 五、函数文档
使用三引号 `"""` 添加文档字符串（可通过 `help(函数名)` 查看）：
```python
def factorial(n):
    """计算一个数的阶乘

    Args:
        n (int): 非负整数

    Returns:
        int: n的阶乘
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

help(factorial)  # 显示函数的文档说明
```

---

掌握这些方法后，你可以灵活地通过函数封装代码逻辑，提升代码的复用性和可读性！


在 Python 中，类中的函数被称为 **方法（Method）**，分为 **实例方法**、**类方法** 和 **静态方法**。以下是定义和使用的详细说明：

---

### 一、类中的函数类型及定义

#### 1. **实例方法 (Instance Method)**  
- 最常见的类型，**必须将 `self` 作为第一个参数**（表示类的实例）。  
- 通过实例调用，可访问实例属性和其他方法。  

```python
class MyClass:
    def instance_method(self, param1, param2):
        """实例方法"""
        print("调用实例方法")
        self.value = param1 + param2  # 访问实例属性
        return self.value
```

#### 2. **类方法 (Class Method)**  
- 使用 `@classmethod` 装饰器，**第一个参数为 `cls`**（表示类本身）。  
- 通过类或实例调用，可访问类属性，但不能访问实例属性。  

```python
class MyClass:
    class_attribute = "类属性"

    @classmethod
    def class_method(cls):
        """类方法"""
        print("调用类方法")
        print("访问类属性:", cls.class_attribute)
        # 无法访问实例属性（如 cls.value）
```

#### 3. **静态方法 (Static Method)**  
- 使用 `@staticmethod` 装饰器，**无需 `self` 或 `cls` 参数**。  
- 通过类或实例调用，**不能访问类属性或实例属性**，仅作为工具函数。  

```python
class MyClass:
    @staticmethod
    def static_method(a, b):
        """静态方法"""
        print("调用静态方法")
        return a + b
```

---

### 二、使用示例

#### 1. 创建对象并调用方法
```python
obj = MyClass()

# 调用实例方法
result = obj.instance_method(3, 5)  # 输出：调用实例方法
print(result)  # 8

# 调用类方法
MyClass.class_method()  # 输出：调用类方法 \n 访问类属性: 类属性

# 调用静态方法
print(MyClass.static_method(2, 3))  # 输出：调用静态方法 \n 5
```

#### 2. 初始化方法 `__init__`
- 特殊实例方法，用于初始化对象属性。  

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age

    def say_hello(self):
        print(f"Hello, I'm {self.name}!")

# 创建对象
p = Person("Alice", 25)
p.say_hello()  # 输出：Hello, I'm Alice!
```

---

### 三、方法对比

| 方法类型   | 装饰器          | 第一个参数 | 可访问实例属性 | 可访问类属性 | 调用方式            |
|------------|-----------------|------------|----------------|--------------|---------------------|
| 实例方法   | 无              | `self`     | 是             | 是（通过类名） | 实例调用 `obj.method()` |
| 类方法     | `@classmethod`  | `cls`      | 否             | 是           | 类或实例调用 `Class.method()` |
| 静态方法   | `@staticmethod` | 无         | 否             | 否           | 类或实例调用 `Class.method()` |

---

### 四、关键注意事项
1. **`self` 和 `cls` 是约定命名**，可替换但强烈建议保留。  
2. **类方法常用于工厂模式**（创建类的不同实例）。  
3. **静态方法适合工具函数**（如数据格式转换）。  
4. **不要滥用静态方法**，优先考虑是否需要与类相关。  

---

### 五、完整示例代码
```python
class Calculator:
    PI = 3.14159  # 类属性

    def __init__(self, model):
        self.model = model  # 实例属性

    @classmethod
    def get_pi(cls):
        return cls.PI

    @staticmethod
    def add(a, b):
        return a + b

    def multiply(self, x, y):
        return x * y

# 使用
calc = Calculator("科学计算器")
print(calc.model)          # 科学计算器
print(Calculator.get_pi()) # 3.14159
print(calc.add(2, 3))      # 5
print(calc.multiply(4, 5)) # 20
```

掌握这些方法后，可以更灵活地设计面向对象的 Python 程序！