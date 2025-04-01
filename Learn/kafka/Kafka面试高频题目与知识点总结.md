以下是关于Kafka的高频面试题目及其核心知识点总结，帮助快速掌握核心概念和面试要点：

---

### **一、基础概念**
1. **Kafka是什么？适用场景有哪些？**  
   - 分布式流处理平台，用于高吞吐、低延迟的实时数据管道和流处理。  
   - 场景：日志聚合、事件溯源、消息队列、流处理（如用户行为跟踪）。

2. **Kafka与RabbitMQ等传统消息队列的区别？**  
   - 持久化：Kafka数据持久化到磁盘，支持批量消费；RabbitMQ基于内存。  
   - 吞吐量：Kafka支持百万级TPS；RabbitMQ适合中小规模。  
   - 消息模型：Kafka基于发布-订阅，RabbitMQ支持多种模型（点对点、Pub/Sub）。

---

### **二、架构设计**
3. **Kafka核心组件及作用**  
   - **Producer**：发布消息到Topic。  
   - **Consumer**：订阅Topic消费消息。  
   - **Broker**：Kafka服务器，存储消息。  
   - **Topic**：逻辑消息分类，分为多个Partition。  
   - **ZooKeeper**：管理集群元数据（新版本逐步用KRaft替代）。

4. **Partition的作用及设计意义？**  
   - 分区实现水平扩展，每个分区独立存储和读写，提升并发能力。  
   - 分区内消息有序，分区间无序。

5. **副本机制（Replication）如何保证高可用？**  
   - 每个分区有Leader和多个Follower副本。  
   - Leader处理读写，Follower异步/同步同步数据。  
   - Leader故障时，Controller从ISR（In-Sync Replicas）选举新Leader。

---

### **三、生产者（Producer）**
6. **Producer的ACK机制有哪些？**  
   - `acks=0`：不等待确认，可能丢失数据。  
   - `acks=1`：Leader确认后返回，可能丢失未同步的副本数据。  
   - `acks=all`：所有ISR副本确认，可靠性最高。

7. **如何保证消息顺序性？**  
   - 单个分区内消息有序，需确保同一业务键（Key）的消息发送到同一分区。

8. **Producer如何选择分区策略？**  
   - 默认策略：轮询、按Key哈希、自定义分区器。

---

### **四、消费者（Consumer）**
9. **消费者组（Consumer Group）的作用？**  
   - 组内消费者协同消费Topic，每个分区仅被组内一个消费者消费，实现负载均衡。

10. **Rebalance的触发条件及影响？**  
    - 触发条件：消费者加入/离开、分区数变化。  
    - 影响：消费暂停，需重新分配分区。

11. **如何提交Offset？**  
    - 自动提交：`enable.auto.commit=true`，可能重复消费。  
    - 手动提交：`commitSync()`（同步）或`commitAsync()`（异步）。

---

### **五、数据存储与性能**
12. **Kafka如何实现高吞吐量？**  
    - 顺序读写磁盘、页缓存优化、零拷贝（Zero-Copy）技术、批量发送/压缩。

13. **零拷贝（Zero-Copy）原理？**  
    - 通过`sendfile()`系统调用，数据直接从磁盘→网卡，绕过用户态，减少CPU复制开销。

14. **日志存储结构**  
    - 分区日志分为多个Segment文件（`.log`存储数据，`.index`存储偏移量索引）。

---

### **六、可靠性保障**
15. **消息丢失的场景及解决方案**  
    - **Producer端**：使用`acks=all`，重试机制。  
    - **Broker端**：确保ISR副本数≥2，禁用unclean leader选举。  
    - **Consumer端**：关闭自动提交，处理完业务再提交Offset。

16. **Exactly-Once语义如何实现？**  
    - 启用幂等Producer（`enable.idempotence=true`）和事务（跨分区原子性）。

---

### **七、高级特性**
17. **Controller的作用及选举流程**  
    - 负责分区Leader选举、集群状态管理。  
    - 通过ZooKeeper选举（旧版本），KRaft模式下内置Raft协议。

18. **日志压缩（Log Compaction）的作用？**  
    - 保留Key的最新Value，适用于状态更新场景（如数据库变更日志）。

---

### **八、运维与监控**
19. **关键监控指标**  
    - 集群：Broker存活、分区副本同步延迟。  
    - 生产/消费：吞吐量、延迟、Offset滞后。

20. **常用性能调优参数**  
    - `num.io.threads`（IO线程数）、`log.flush.interval.messages`（刷盘策略）、`replica.lag.time.max.ms`（ISR同步超时）。

---

### **九、实际应用**
21. **Kafka Streams与Flink的区别？**  
    - Kafka Streams轻量级库，适合简单流处理；Flink功能更复杂，支持状态计算、窗口等。

22. **如何设计一个高可用Kafka集群？**  
    - 跨机房部署、分区副本分散在不同机架、监控ISR状态、合理设置`min.insync.replicas`。

---

掌握这些问题，能覆盖80%以上的Kafka面试考点。建议结合实践场景（如消息顺序性保障、故障恢复）深入理解原理。