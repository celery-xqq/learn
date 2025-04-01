当 Redis 同时开启 **RDB** 和 **AOF** 两种持久化方式时，**重启后会优先使用 AOF 文件（`appendonly.aof`）来恢复数据**。这是 Redis 的设计逻辑，原因如下：

---

### 1. **优先级规则**
- **AOF 的优先级高于 RDB**：Redis 在启动时，如果检测到 AOF 功能已启用（`appendonly yes`），则会直接加载 AOF 文件中的数据，而忽略 RDB 文件（`dump.rdb`）。  
- **如果 AOF 文件不存在或损坏**，Redis 会尝试加载 RDB 文件作为备选方案。

---

### 2. **为什么优先用 AOF？**
- **AOF 记录更完整**：AOF 以日志形式记录每次写操作（默认每秒同步一次），理论上最多丢失 1 秒的数据，数据安全性更高。  
- **RDB 是时间点快照**：RDB 是定期生成的全量备份，可能丢失最后一次快照后的所有修改（取决于备份频率）。  

---

### 3. **验证方法**
可以通过以下方式观察 Redis 启动时的日志：
```bash
# Redis 启动日志示例
* DB loaded from append only file: 0.123 seconds  # 表示从 AOF 加载
* DB loaded from disk: 0.456 seconds             # 表示从 RDB 加载
```

---

### 4. **注意事项**
- **AOF 文件可能更大**：AOF 记录了所有写操作，文件体积通常比 RDB 大，恢复速度可能较慢（可通过 `bgrewriteaof` 重写优化）。  
- **混合持久化**：Redis 4.0+ 支持 `aof-use-rdb-preamble`，在 AOF 重写时会将数据以 RDB 格式写入，重启时结合 RDB 的快速加载和 AOF 的增量操作，进一步优化恢复效率。

---

### 总结
**开启 AOF 后，Redis 重启时优先用 AOF 恢复数据，仅在 AOF 不可用时才回退到 RDB**。这种设计在数据安全性和完整性上提供了更好的保障。