以下是 Redis 高频面试题的整理，涵盖核心知识点和实际应用场景：

---

### **一、基础概念**
1. **Redis 是什么？和 Memcached 有什么区别？**  
   - 内存数据库，支持持久化、多种数据结构、集群；Memcached 仅支持简单 KV，无持久化，多线程模型。

2. **Redis 的 5 种基本数据类型及其应用场景？**  
   - `String`（计数器）、`Hash`（对象存储）、`List`（消息队列）、`Set`（去重/标签）、`ZSet`（排行榜）。

3. **Redis 的线程模型？为什么单线程还能高性能？**  
   - 单线程处理命令（6.0+ 支持多线程网络 I/O），基于内存操作、非阻塞 I/O 复用（epoll）、避免上下文切换。

---

### **二、持久化与高可用**
4. **RDB 和 AOF 的优缺点？**  
   - RDB：快照恢复快，但可能丢数据；AOF：数据安全，但文件大、恢复慢。  
   - Redis 4.0+ 支持混合持久化（AOF + RDB 格式）。

5. **主从复制原理？**  
   - 全量同步（RDB 快照） + 增量同步（命令传播），主节点写，从节点读。

6. **哨兵（Sentinel）机制的作用？**  
   - 监控主从节点，自动故障转移（主节点宕机时选举新主）。

7. **Redis Cluster 如何实现数据分片？**  
   - 16384 个哈希槽（slot），节点分片管理，客户端路由（`CRC16(key) % 16384`）。

---

### **三、缓存问题**
8. **缓存穿透、缓存雪崩、缓存击穿的区别与解决方案？**  
   - **穿透**：查询不存在的数据 → 布隆过滤器 + 空值缓存。  
   - **雪崩**：大量缓存同时过期 → 随机过期时间 + 集群高可用。  
   - **击穿**：热点 key 过期 → 互斥锁（SETNX） + 永不过期（逻辑续期）。

9. **如何保证缓存与数据库双写一致性？**  
   - 旁路缓存（Cache Aside）：先更新数据库，再删缓存（延迟双删策略）。

---

### **四、高级特性**
10. **Redis 事务（MULTI/EXEC）的原子性？**  
    - 事务中的命令按顺序执行，但无回滚（语法错误全不执行，运行时错误继续执行）。

11. **如何用 Redis 实现分布式锁？**  
    - `SET key value NX EX timeout`（防死锁），Redlock 算法（多节点防单点故障）。

12. **Redis 的内存淘汰策略有哪些？**  
    - `noeviction`（默认不淘汰）、`LRU`、`LFU`、`random`、`TTL`（过期时间淘汰）。

---

### **五、性能优化**
13. **Redis 的慢查询如何排查？**  
    - 配置 `slowlog-log-slower-than`，通过 `SLOWLOG GET` 查看。

14. **Pipeline 和 Lua 脚本的作用？**  
    - Pipeline：批量执行命令，减少网络往返；Lua：原子性执行复杂逻辑。

15. **大 Key 和热 Key 如何处理？**  
    - 大 Key：拆分或压缩（如 Hash 分 field）；热 Key：多级缓存、读写分离、打散分布。

---

### **六、应用场景**
16. **如何用 Redis 实现延迟队列？**  
    - `ZSet` 按时间戳排序，消费者轮询 `ZRANGEBYSCORE` 获取到期任务。

17. **如何实现排行榜功能？**  
    - `ZSet` 存储用户分数，`ZREVRANGE` 按排名查询。

18. **Redis 的发布订阅（Pub/Sub）有什么缺点？**  
    - 消息不持久化，消费者离线会丢失消息（替代方案：Stream 数据结构）。

---

### **七、运维与监控**
19. **Redis 的内存碎片如何优化？**  
    - 配置 `activedefrag yes`，或重启实例（生产慎用）。

20. **Redis 的常见性能指标？**  
    - QPS、内存占用、连接数、命中率、延迟（`redis-cli --latency`）。

---

### **附：Redis 6.0/7.0 新特性**
- **多线程网络 I/O**（6.0）：提升吞吐量，但命令执行仍单线程。  
- **ACL 权限控制**（6.0）：精细化权限管理。  
- **Function API**（7.0）：替代 Lua，支持更灵活的脚本管理。

---

掌握这些问题后，建议结合实战场景（如高并发、分布式系统设计）深入理解原理，并熟悉 Redis 的配置和命令。