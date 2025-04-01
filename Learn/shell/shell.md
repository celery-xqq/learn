在 Shell 脚本中，`$` 符号是一个关键字符，主要用于 **变量引用、命令替换、算术运算** 等场景。以下是 `$` 的常见用法及示例：

---

### 1. **变量引用（Variable Expansion）**
- **基本语法**：`$变量名` 或 `${变量名}`
  ```bash
  name="John"
  echo $name       # 输出：John
  echo ${name}     # 推荐写法（避免歧义）
  ```

- **防止歧义**（如拼接变量和字符串）：
  ```bash
  file="data"
  echo "${file}_backup.txt"  # 输出：data_backup.txt（正确）
  echo "$file_backup.txt"    # 错误！尝试引用变量 `file_backup`
  ```

---

### 2. **特殊变量（Special Variables）**
- **脚本参数**：
  - `$0`：脚本名称
  - `$1`, `$2`, ...：第 1、2 个参数
  - `$#`：参数个数
  - `$@` 或 `$*`：所有参数（区别见下文）

- **进程和状态**：
  - `$$`：当前 Shell 的 PID（进程 ID）
  - `$?`：上一条命令的退出状态（0 表示成功，非 0 表示失败）
  - `$!`：最后一个后台进程的 PID

  ```bash
  echo "脚本名: $0"
  echo "第一个参数: $1"
  echo "参数总数: $#"
  echo "所有参数: $@"
  echo "PID: $$"
  ls /nonexistent
  echo "上一条命令的退出码: $?"  # 输出非 0（失败）
  ```

---

### 3. **命令替换（Command Substitution）**
- **语法**：`$(command)` 或 `` `command` ``
  ```bash
  current_date=$(date)     # 将命令输出赋值给变量
  echo "今天是: $current_date"

  files_count=`ls | wc -l` # 反引号（旧语法，建议用 $()）
  echo "文件数: $files_count"
  ```

---

### 4. **算术运算（Arithmetic Expansion）**
- **语法**：`$((表达式))`
  ```bash
  a=5
  b=3
  sum=$((a + b))      # 计算 5+3
  echo "和是: $sum"    # 输出：8
  ```

---

### 5. **字符串操作（String Manipulation）**
- **使用 `${}` 扩展功能**：
  - **长度**：`${#变量}`
    ```bash
    str="hello"
    echo "${#str}"   # 输出 5
    ```
  - **子字符串**：`${变量:起始位置:长度}`
    ```bash
    str="abcdef"
    echo "${str:1:3}"  # 输出 bcd（从索引 1 开始取 3 个字符）
    ```
  - **默认值**：`${变量:-默认值}`
    ```bash
    unset var
    echo "${var:-默认值}"  # 输出：默认值
    ```

---

### 6. **其他用法**
- **位置参数扩展**：
  - `$@`：所有参数，每个参数视为独立字符串（推荐使用）。
  - `$*`：所有参数合并为一个字符串。
  ```bash
  for arg in "$@"; do
    echo "参数: $arg"
  done
  ```

- **退出状态快捷操作**：
  ```bash
  command1 || echo "command1 失败"   # 若 command1 失败则执行
  command2 && echo "command2 成功"   # 若 command2 成功则执行
  ```

---

### 常见错误和注意事项
1. **变量未定义或空值**：
   ```bash
   echo "$undefined_var"  # 输出空字符串
   ```

2. **赋值时不要加 `$`**：
   ```bash
   var=value   # 正确
   var=$value  # 错误（除非 value 是另一个变量）
   ```

3. **引号的影响**：
   ```bash
   name="Alice"
   echo "$name"    # Alice
   echo '$name'    # $name（单引号禁止变量展开）
   ```

---

### 总结表格
| 语法             | 用途                          | 示例                     |
|------------------|-------------------------------|--------------------------|
| `$var`           | 引用变量                      | `echo $PATH`             |
| `${var}`         | 引用变量（避免歧义）          | `echo ${var}_suffix`     |
| `$()`            | 命令替换                      | `files=$(ls)`            |
| `$((...))`       | 算术运算                      | `sum=$((1+2))`           |
| `$0`, `$1`, `$#` | 脚本参数和状态                | `echo "参数1: $1"`       |
| `$$`, `$?`, `$!` | 进程 PID 和退出状态           | `echo "PID: $$"`         |
| `${var:-default}`| 使用默认值                    | `echo ${name:-"匿名"}`   |

掌握 `$` 的用法是 Shell 脚本编程的核心基础！

Shell脚本是自动化任务和系统管理的强大工具。以下是其基本语法的简明指南：

---

### 1. 脚本基础
- **Shebang**：首行指定解释器
  ```bash
  #!/bin/bash
  ```
- **执行脚本**
  ```bash
  chmod +x script.sh  # 添加执行权限
  ./script.sh         # 直接运行
  bash script.sh      # 指定解释器运行
  ```

---

### 2. 变量
- **定义变量**（等号两侧无空格）
  ```bash
  name="value"
  ```
- **使用变量**（推荐用`${}`避免歧义）
  ```bash
  echo $name
  echo "${name}123"
  ```
- **环境变量**
  ```bash
  export PATH="/usr/local/bin:$PATH"
  ```

---

### 3. 字符串
- **单引号**（原样输出） vs **双引号**（支持变量）
  ```bash
  str1='Hello $USER'  # 输出 Hello $USER
  str2="Hello $USER"  # 输出 Hello alice
  ```
- **拼接字符串**
  ```bash
  full_str="${str1}${str2}"
  ```

---

### 4. 数组
- **定义与访问**
  ```bash
  array=("apple" "banana" "cherry")
  echo ${array[1]}    # 输出 banana
  echo ${array[@]}    # 输出所有元素
  echo ${#array[@]}   # 数组长度
  ```

---

### 5. 控制结构
- **条件判断**
  ```bash
  if [ $a -eq $b ]; then
    echo "a等于b"
  elif [ $a -gt $b ]; then
    echo "a大于b"
  else
    echo "其他情况"
  fi
  ```
  - 数值比较：`-eq`（等于）、`-ne`（不等于）、`-lt`（小于）
  - 字符串比较：`=`（相等）、`!=`（不等）
  - 文件测试：`-e`（存在）、`-f`（是文件）、`-d`（是目录）

- **循环**
  - **for循环**
    ```bash
    for fruit in "${array[@]}"; do
      echo "$fruit"
    done
    ```
  - **while循环**
    ```bash
    count=0
    while [ $count -lt 5 ]; do
      echo $count
      ((count++))
    done
    ```

---

### 6. 函数
- **定义与调用**
  ```bash
  greet() {
    local name=$1  # 局部变量
    echo "Hello, $name"
    return 0       # 返回值（0-255）
  }
  greet "Alice"
  ```
- **获取返回值**
  ```bash
  greet "Bob"
  echo "返回值: $?"  # $? 获取上一条命令的退出状态
  ```

---

### 7. 输入输出
- **读取输入**
  ```bash
  read -p "请输入名字: " username
  ```
- **重定向**
  ```bash
  echo "内容" > file.txt    # 覆盖写入
  echo "追加" >> file.txt  # 追加写入
  cat file.txt | grep "关键字"
  ```

---

### 8. 特殊变量
- `$0`：脚本名称
- `$1`-`$9`：第1-9个参数
- `$#`：参数个数
- `$@`：所有参数（视为独立元素）
- `$*`：所有参数（视为单个字符串）
- `$?`：上一条命令的退出状态
- `$$`：当前进程的PID

---

### 9. 算术运算
- **使用 `$(( ))`**
  ```bash
  sum=$((3 + 5))
  ```
- **自增操作**
  ```bash
  ((count++))
  ```

---

### 10. 调试与错误处理
- **调试模式**
  ```bash
  bash -x script.sh  # 显示执行过程
  ```
- **立即退出（遇到错误）**
  ```bash
  set -e
  ```

---

### 示例脚本
```bash
#!/bin/bash
# 计算1到N的和

read -p "输入数字: " n
sum=0

for ((i=1; i<=n; i++)); do
  sum=$((sum + i))
done

echo "1到$n的和为: $sum"
```

---

**常见问题提醒**：
- 条件判断中的空格必不可少，如 `[ $a == $b ]`。
- 变量赋值时等号两侧不能有空格。
- 使用双引号包裹变量，避免含空格的字符串解析错误。

掌握这些基础后，可通过实践逐步深入Shell脚本的复杂用法！

在 Shell 脚本中，`''`、`""`、`` ` ` `` 和 `$` 是四个关键符号，它们的用途和行为有显著区别。以下是对它们的详细解析：

---

### **1. 单引号 `''`**
- **行为**：完全保留字面值，**不执行任何替换**（变量替换、命令替换、转义字符均无效）。
- **示例**：
  ```bash
  echo '$USER `date`'  # 输出：$USER `date`
  ```
- **用途**：确保字符串内容原样输出，避免特殊字符被解析。

---

### **2. 双引号 `""`**
- **行为**：允许**变量替换**和**命令替换**，但保留字符串的完整性（防止单词拆分）。
- **示例**：
  ```bash
  name="Alice"
  echo "Hello $name, today is $(date)"  
  # 输出：Hello Alice, today is Mon Sep 20 12:34:56 UTC 2023
  ```
- **注意事项**：
  - 支持转义字符（如 `\n`、`\t`），但需配合 `echo -e`。
  - 通配符（如 `*`）不会展开为文件名。
  - 变量名需用 `${}` 明确边界（如 `${var}_file`）。

---

### **3. 反引号 `` ` ` ``**
- **行为**：**命令替换**，执行内部命令并替换为输出结果（与 `$()` 等效，但 `` ` ` `` 嵌套时需转义）。
- **示例**：
  ```bash
  echo "当前时间是 `date`"      # 输出：当前时间是 Mon Sep 20 12:34:56 UTC 2023
  echo "当前时间是 $(date)"    # 等效写法（推荐）
  ```
- **推荐使用 `$()`**：语法更清晰，支持嵌套，例如：
  ```bash
  echo "嵌套示例：$(echo $(date))"
  ```

---

### **4. 美元符号 `$`**
- **行为**：触发**变量替换**或**命令替换**。
- **常见用法**：
  - **变量替换**：
    ```bash
    name="Bob"
    echo $name        # 输出：Bob
    echo "${name}!"   # 输出：Bob!
    ```
  - **命令替换**（需配合 `$()`）：
    ```bash
    echo "当前路径：$(pwd)"
    ```
  - **特殊变量**：
    ```bash
    echo "脚本参数个数：$#"    # 输出参数总数
    echo "第一个参数：$1"      # 输出第一个参数
    ```

---

### **对比总结**
| 符号         | 变量替换 | 命令替换 | 转义字符 | 防止单词拆分 | 示例                 |
|--------------|----------|----------|----------|--------------|----------------------|
| `''` (单引号)| ❌       | ❌       | ❌       | ✔️           | `echo '$USER'`       |
| `""` (双引号)| ✔️       | ✔️       | ✔️       | ✔️           | `echo "$USER"`       |
| `` ` ` ``    | ❌       | ✔️       | ❌       | ❌           | ``echo `date` ``     |
| `$`          | ✔️       | ✔️       | ✔️       | 依赖上下文   | `echo $USER`         |

---

### **常见误区**
1. **单引号中无法转义**：
   ```bash
   echo 'It\'s a trap'   # 错误！单引号内不能转义单引号。
   echo "It's a trap"    # 正确：改用双引号。
   ```

2. **变量边界问题**：
   ```bash
   num=1
   echo "$num_apple"     # 错误！实际解析为变量 `num_apple`。
   echo "${num}_apple"   # 正确：输出 `1_apple`。
   ```

3. **命令替换的嵌套**：
   ```bash
   echo `echo \`date\``  # 需转义（复杂）
   echo $(echo $(date))  # 更简洁（推荐）
   ```

---

### **示例脚本**
```bash
#!/bin/bash
user="Alice"
echo '单引号: $user `date`'      # 输出：$user `date`
echo "双引号: $user $(date)"     # 输出：Alice Mon Sep 20 12:34:56 UTC 2023
echo "反引号: `date`"            # 输出：Mon Sep 20 12:34:56 UTC 2023
echo "命令替换: $(echo ${user})" # 输出：Alice
```

掌握这些符号的差异，能显著提升 Shell 脚本编写的准确性和效率！