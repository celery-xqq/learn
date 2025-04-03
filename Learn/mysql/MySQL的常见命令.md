以下是MySQL的常用命令分类整理，涵盖数据库管理、表操作、查询、用户权限等核心操作，方便快速查阅：

---

### **一、数据库操作**
1. **查看所有数据库**  
   ```sql
   SHOW DATABASES;
   ```

2. **创建数据库**  
   ```sql
   CREATE DATABASE dbname;
   ```

3. **选择数据库**  
   ```sql
   USE dbname;
   ```

4. **删除数据库**  
   ```sql
   DROP DATABASE dbname;
   ```

---

### **二、表操作**
1. **查看所有表**  
   ```sql
   SHOW TABLES;
   ```

2. **创建表**  
   ```sql
   CREATE TABLE tablename (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(50) NOT NULL,
     age INT,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. **查看表结构**  
   ```sql
   DESC tablename;
   -- 或
   SHOW CREATE TABLE tablename;
   ```

4. **删除表**  
   ```sql
   DROP TABLE tablename;
   ```

5. **修改表结构**  
   ```sql
   -- 添加列
   ALTER TABLE tablename ADD COLUMN email VARCHAR(100);
   
   -- 修改列类型
   ALTER TABLE tablename MODIFY COLUMN age TINYINT;
   
   -- 删除列
   ALTER TABLE tablename DROP COLUMN email;
   
   -- 重命名表
   ALTER TABLE tablename RENAME TO new_tablename;
   ```

---

### **三、数据操作（CRUD）**
1. **插入数据**  
   ```sql
   INSERT INTO tablename (name, age) VALUES ('Alice', 25);
   -- 插入多条
   INSERT INTO tablename (name, age) VALUES ('Bob', 30), ('Charlie', 28);
   ```

2. **查询数据**  
   ```sql
   -- 查询所有列
   SELECT * FROM tablename;
   
   -- 条件查询
   SELECT name, age FROM tablename WHERE age > 25;
   
   -- 排序
   SELECT * FROM tablename ORDER BY age DESC;
   
   -- 分页
   SELECT * FROM tablename LIMIT 10 OFFSET 0;
   
   -- 聚合函数
   SELECT COUNT(*) AS total, AVG(age) AS avg_age FROM tablename;
   
   -- 分组
   SELECT age, COUNT(*) FROM tablename GROUP BY age;
   
   -- 多表JOIN
   SELECT u.name, o.order_id 
   FROM users u 
   JOIN orders o ON u.id = o.user_id;
   ```

3. **更新数据**  
   ```sql
   UPDATE tablename SET age = 26 WHERE name = 'Alice';
   ```

4. **删除数据**  
   ```sql
   DELETE FROM tablename WHERE id = 1;
   -- 清空表（不可恢复）
   TRUNCATE TABLE tablename;
   ```

---

### **四、用户与权限管理**
1. **创建用户**  
   ```sql
   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
   ```

2. **授予权限**  
   ```sql
   -- 授予所有权限
   GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';
   
   -- 授予特定权限
   GRANT SELECT, INSERT, UPDATE ON dbname.* TO 'username'@'localhost';
   
   -- 刷新权限
   FLUSH PRIVILEGES;
   ```

3. **撤销权限**  
   ```sql
   REVOKE ALL PRIVILEGES ON dbname.* FROM 'username'@'localhost';
   ```

4. **删除用户**  
   ```sql
   DROP USER 'username'@'localhost';
   ```

5. **查看用户权限**  
   ```sql
   SHOW GRANTS FOR 'username'@'localhost';
   ```

---

### **五、备份与恢复**
1. **导出整个数据库（命令行）**  
   ```bash
   mysqldump -u root -p dbname > backup.sql
   ```

2. **导出单张表**  
   ```bash
   mysqldump -u root -p dbname tablename > table_backup.sql
   ```

3. **导入数据（命令行）**  
   ```bash
   mysql -u root -p dbname < backup.sql
   ```

---

### **六、事务与锁**
1. **开启事务**  
   ```sql
   START TRANSACTION;
   -- 执行操作...
   COMMIT; -- 提交
   -- 或
   ROLLBACK; -- 回滚
   ```

2. **设置隔离级别**  
   ```sql
   SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
   ```

3. **手动加锁**  
   ```sql
   SELECT * FROM tablename WHERE id = 1 FOR UPDATE;
   ```

---

### **七、系统信息**
1. **查看MySQL版本**  
   ```sql
   SELECT VERSION();
   ```

2. **查看当前用户**  
   ```sql
   SELECT USER();
   ```

3. **查看运行状态**  
   ```sql
   SHOW STATUS;
   ```

4. **查看进程列表**  
   ```sql
   SHOW PROCESSLIST;
   ```

---

### **八、索引优化**
1. **创建索引**  
   ```sql
   CREATE INDEX idx_name ON tablename (name);
   ```

2. **查看索引**  
   ```sql
   SHOW INDEX FROM tablename;
   ```

3. **删除索引**  
   ```sql
   DROP INDEX idx_name ON tablename;
   ```

---

### **九、其他实用命令**
1. **重置root密码（命令行）**  
   ```bash
   # 停止MySQL服务
   sudo systemctl stop mysql
   # 启动无密码模式
   mysqld_safe --skip-grant-tables &
   # 登录并修改密码
   mysql -u root
   FLUSH PRIVILEGES;
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
   ```

2. **查看字符集**  
   ```sql
   SHOW VARIABLES LIKE 'character_set%';
   ```

3. **查看存储引擎**  
   ```sql
   SHOW ENGINES;
   ```

---

### **十、注意事项**
1. **生产环境慎用**：`DROP`、`TRUNCATE` 和 `DELETE` 命令需谨慎操作。
2. **权限最小化原则**：避免赋予用户不必要的权限。
3. **备份先行**：修改重要数据前先备份。

如果需要更详细的命令解释，可以通过 `HELP 命令名;`（如 `HELP SELECT;`）查看MySQL官方文档。