Linux 系统中常用的命令可以分为以下几类，以下是常见命令的总结：

---

### **1. 文件和目录操作**
- `ls`：列出目录内容（`-l` 显示详细信息，`-a` 显示隐藏文件）。
- `cd`：切换目录（`cd ~` 进入家目录，`cd ..` 返回上级）。
- `pwd`：显示当前工作目录的路径。
- `mkdir`：创建目录（`-p` 创建多级目录，如 `mkdir -p dir1/dir2`）。
- `rmdir`：删除空目录。
- `touch`：创建空文件或更新文件时间戳。
- `cp`：复制文件或目录（`-r` 递归复制目录）。
- `mv`：移动或重命名文件/目录。
- `rm`：删除文件或目录（`-r` 递归删除，`-f` 强制删除，慎用 `rm -rf /`！）。
- `file`：查看文件类型。

---

### **2. 文件内容查看与编辑**
- `cat`：显示文件内容（适合小文件）。
- `more` / `less`：分页查看文件内容（`less` 支持上下翻页）。
- `head`：显示文件头部内容（默认前10行，`-n 20` 指定行数）。
- `tail`：显示文件尾部内容（`-f` 实时追踪文件变化，常用于日志）。
- `nano` / `vim`：文本编辑器（`vim` 功能更强大）。

---

### **3. 权限管理**
- `chmod`：修改文件权限（如 `chmod 755 file` 或 `chmod u+x file`）。
- `chown`：修改文件所有者（如 `chown user:group file`）。
- `chgrp`：修改文件所属组。

---

### **4. 系统信息与监控**
- `top` / `htop`：实时查看系统进程和资源占用。
- `df`：查看磁盘空间（`-h` 以易读格式显示，如 `df -h`）。
- `du`：查看目录占用空间（`-sh *` 查看当前目录各子项大小）。
- `free`：查看内存使用情况（`-h` 显示单位）。
- `uname`：查看系统信息（`-a` 显示全部信息）。
- `uptime`：查看系统运行时间和负载。

---

### **5. 进程管理**
- `ps`：查看进程状态（常用 `ps aux` 或 `ps -ef`）。
- `kill`：终止进程（`kill -9 PID` 强制终止）。
- `pkill` / `killall`：按进程名终止进程（如 `killall nginx`）。
- `bg` / `fg`：切换进程到后台/前台运行。
- `jobs`：查看后台任务。

---

### **6. 网络操作**
- `ping`：测试网络连通性（如 `ping google.com`）。
- `curl` / `wget`：下载文件或测试 HTTP 请求。
- `netstat` / `ss`：查看网络连接和端口状态（如 `netstat -tulnp`）。
- `ifconfig` / `ip`：查看或配置网络接口（新版推荐 `ip addr`）。
- `ssh`：远程登录（`ssh user@host`）。
- `scp`：安全复制文件到远程主机（`scp file user@host:/path`）。
- `traceroute`：追踪数据包路径。

---

### **7. 压缩与解压**
- `tar`：打包和解包文件（常用组合）：
  - 打包：`tar -czvf archive.tar.gz dir/`
  - 解压：`tar -xzvf archive.tar.gz`
- `gzip` / `gunzip`：压缩或解压 `.gz` 文件。
- `zip` / `unzip`：处理 `.zip` 文件。

---

### **8. 查找与搜索**
- `find`：按条件查找文件（如 `find / -name "*.log"`）。
- `grep`：文本搜索工具（如 `grep "error" file.log`）。
- `locate`：快速查找文件（需先更新数据库 `updatedb`）。

---

### **9. 用户管理**
- `useradd` / `userdel`：添加或删除用户。
- `passwd`：修改用户密码。
- `su`：切换用户（如 `su - username`）。
- `sudo`：以管理员权限执行命令。
- `id`：查看用户信息。

---

### **10. 软件包管理**
- **Debian/Ubuntu (APT)**：
  - `apt update`：更新软件源。
  - `apt install package`：安装软件。
  - `apt remove package`：卸载软件。
- **Red Hat/CentOS (YUM/DNF)**：
  - `yum install package` 或 `dnf install package`。
  - `yum remove package`。

---

### **11. 其他实用命令**
- `history`：查看命令历史记录。
- `alias`：设置命令别名（如 `alias ll='ls -l'`）。
- `echo`：输出文本（常用于脚本或变量）。
- `date`：显示或设置系统时间。
- `reboot` / `shutdown`：重启或关机（`shutdown -h now` 立即关机）。
- `man`：查看命令手册（如 `man ls`）。

---

### **注意事项**
- **谨慎使用 `rm -rf`**：删除前务必确认路径，避免误删系统文件。
- **善用 Tab 补全**：提高命令输入效率。
- **查看命令帮助**：大多数命令支持 `--help` 参数（如 `ls --help`）。

掌握这些命令后，可以高效完成 Linux 系统的日常操作和管理任务！