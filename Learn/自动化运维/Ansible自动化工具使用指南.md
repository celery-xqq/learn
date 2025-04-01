Ansible 是一款开源的自动化工具，用于配置管理、应用部署、任务编排等。它基于 **SSH** 协议，无需在目标主机安装客户端，通过 **YAML** 语法描述任务，简单易用。以下是 Ansible 的核心用法和常见场景：

---

### **一、核心概念**
1. **控制节点（Control Node）**  
   运行 Ansible 的主机，需安装 Ansible（仅支持 Linux/macOS）。
   
2. **被控节点（Managed Node）**  
   被管理的主机，只需支持 SSH 和 Python（通常已预装）。

3. **Inventory（清单）**  
   定义被管理主机的列表，支持分组和变量。默认文件：`/etc/ansible/hosts`。

   ```ini
   # 示例：定义主机和分组
   [web_servers]
   web1.example.com
   web2.example.com ansible_ssh_port=2222  # 指定SSH端口

   [db_servers]
   db.example.com

   [all:vars]
   ansible_user=admin  # 全局变量
   ```

4. **模块（Module）**  
   Ansible 的核心功能单元（如 `copy`, `file`, `yum`, `service`），通过模块执行任务。

5. **Playbook**  
   YAML 格式的任务剧本，定义一系列操作（如安装软件、配置服务）。

---

### **二、安装与配置**
1. **安装 Ansible**  
   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install ansible -y

   # CentOS/RHEL
   sudo yum install ansible -y

   # macOS
   brew install ansible
   ```

2. **配置 SSH 免密登录**  
   确保控制节点可以通过 SSH 密钥连接到被控节点：
   ```bash
   ssh-keygen -t rsa
   ssh-copy-id user@target_host
   ```

3. **验证连接**  
   ```bash
   ansible all -m ping  # 测试所有主机的连通性
   ```

---

### **三、Ad-Hoc 命令**
直接在命令行中执行简单任务，适合快速操作：
```bash
# 语法
ansible <主机或分组> -m <模块> -a "<参数>"

# 示例
ansible web_servers -m copy -a "src=/tmp/file.txt dest=/opt/file.txt"  # 复制文件
ansible db_servers -m yum -a "name=nginx state=present"              # 安装软件
ansible all -m shell -a "free -m"                                   # 执行Shell命令
```

---

### **四、Playbook 编写**
Playbook 是 Ansible 的核心，用于定义复杂任务流程。

#### 1. 基础示例
```yaml
# deploy_web.yml
---
- hosts: web_servers    # 目标主机分组
  become: yes           # 使用sudo权限
  tasks:
    - name: Install Nginx
      apt: 
        name: nginx
        state: present
      when: ansible_os_family == 'Debian'  # 条件判断

    - name: Start Nginx Service
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Copy Index File
      copy:
        src: files/index.html
        dest: /var/www/html/
```

#### 2. 运行 Playbook
```bash
ansible-playbook deploy_web.yml
```

#### 3. 常用模块
| 模块        | 用途                     | 示例                                                                 |
|-------------|--------------------------|----------------------------------------------------------------------|
| `copy`      | 复制文件到目标主机       | `copy: src=/local/file.txt dest=/remote/path/`                      |
| `yum`/`apt` | 包管理                   | `yum: name=httpd state=latest`                                      |
| `service`   | 管理服务                 | `service: name=nginx state=restarted`                               |
| `file`      | 管理文件/目录权限        | `file: path=/opt/data mode=0755 owner=root group=root`              |
| `template`  | 渲染模板文件（Jinja2）   | `template: src=nginx.conf.j2 dest=/etc/nginx/nginx.conf`            |
| `shell`     | 执行 Shell 命令          | `shell: echo 'Hello' > /tmp/test.txt`                               |

---

### **五、高级功能**
1. **变量（Variables）**  
   在 Playbook 或 Inventory 中定义变量：
   ```yaml
   - hosts: web_servers
     vars:
       http_port: 8080
     tasks:
       - name: Set Port
         lineinfile:
           path: /etc/nginx/nginx.conf
           regexp: '^listen '
           line: 'listen {{ http_port }};'
   ```

2. **循环（Loops）**  
   使用 `loop` 或 `with_items` 重复任务：
   ```yaml
   - name: Install Packages
     apt:
       name: "{{ item }}"
       state: present
     loop:
       - git
       - curl
       - unzip
   ```

3. **角色（Roles）**  
   将 Playbook 模块化，便于复用：
   ```bash
   ansible-galaxy init roles/nginx  # 创建角色目录结构
   ```
   目录结构：
   ```
   roles/
   └── nginx/
       ├── tasks/
       │   └── main.yml
       ├── templates/
       │   └── nginx.conf.j2
       └── vars/
           └── main.yml
   ```

4. **标签（Tags）**  
   选择性运行 Playbook 中的部分任务：
   ```yaml
   tasks:
     - name: Install Nginx
       apt: name=nginx
       tags: install

     - name: Configure Nginx
       template: src=nginx.conf.j2 dest=/etc/nginx/nginx.conf
       tags: config
   ```
   运行指定标签的任务：
   ```bash
   ansible-playbook deploy_web.yml --tags "install"
   ```

---

### **六、常用命令速查**
```bash
ansible-playbook playbook.yml --limit web_servers  # 仅针对指定主机运行
ansible-playbook playbook.yml --check              # 模拟执行（Dry Run）
ansible all -m setup                               # 收集主机信息（Facts）
ansible-doc -l                                     # 列出所有模块
ansible-doc yum                                    # 查看模块文档
```

---

### **七、学习资源**
- 官方文档：[https://docs.ansible.com](https://docs.ansible.com)
- 书籍：《Ansible for DevOps》（推荐入门）
- 社区角色：[Ansible Galaxy](https://galaxy.ansible.com)

掌握以上内容，你已经可以完成大多数自动化运维任务！