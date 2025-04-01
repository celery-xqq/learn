以下是关于 Nginx 的高频面试题目及简要解析，帮助你快速掌握核心知识点：

---

### **一、基础概念**
1. **Nginx 是什么？有什么特点？**  
   - 轻量级、高性能的 **Web 服务器**、**反向代理服务器**、**负载均衡器** 和 **HTTP 缓存**。  
   - 特点：事件驱动架构、高并发（单机支持数万并发）、低内存消耗、热部署（无需重启更新配置）。

2. **Nginx 与 Apache 的区别？**  
   - **连接处理模型**：Apache 多线程/多进程，Nginx 事件驱动（异步非阻塞）。  
   - **资源消耗**：Nginx 内存占用更低，适合高并发场景。  
   - **模块化**：Apache 动态加载模块，Nginx 模块需编译到核心。

3. **正向代理 vs 反向代理？**  
   - **正向代理**：代理客户端，隐藏客户端身份（如科学上网）。  
   - **反向代理**：代理服务端，隐藏服务器身份，实现负载均衡、安全防护。

---

### **二、配置与使用**
4. **如何配置一个虚拟主机（Server Block）？**  
   ```nginx
   server {
       listen 80;
       server_name example.com;
       root /var/www/html;
       index index.html;
   }
   ```

5. **负载均衡策略有哪些？如何配置？**  
   - **轮询（默认）**：均匀分配请求。  
   - **加权轮询**：按权重分配。  
   - **IP Hash**：同一客户端 IP 固定到同一后端。  
   - **最少连接（least_conn）**：优先分配给连接数最少的服务器。  
   ```nginx
   upstream backend {
       server 192.168.1.1 weight=3;
       server 192.168.1.2;
       ip_hash;  # 或 least_conn;
   }
   ```

6. **Location 块的匹配规则是什么？**  
   - `=`：精确匹配（最高优先级）。  
   - `^~`：前缀匹配（不检查正则）。  
   - `~`：正则匹配（区分大小写），`~*`：不区分大小写。  
   - `/`：通用匹配（最低优先级）。

7. **如何配置反向代理？**  
   ```nginx
   location /api {
       proxy_pass http://backend_server;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
   }
   ```

---

### **三、性能优化**
8. **如何优化 Nginx 的并发性能？**  
   - 调整 `worker_processes`（CPU 核心数）、`worker_connections`（单个 Worker 最大连接数）。  
   - 启用 `epoll`（Linux 高效事件模型），开启 `sendfile`、`gzip` 压缩。  
   - 合理配置 `keepalive_timeout` 减少连接建立开销。

9. **如何限制客户端请求速率？**  
   ```nginx
   limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;
   location / {
       limit_req zone=one burst=20;
   }
   ```

---

### **四、原理与机制**
10. **Nginx 如何处理高并发？**  
    - 基于 **事件驱动模型**（如 epoll、kqueue），异步非阻塞处理请求，避免为每个请求创建线程/进程。

11. **Master 和 Worker 进程的作用？**  
    - **Master**：读取配置、管理 Worker 进程（启动、停止、重载配置）。  
    - **Worker**：处理实际请求（多 Worker 利用多核 CPU）。

12. **如何实现热部署（Hot Reload）？**  
    - 更新配置文件后执行 `nginx -s reload`，Master 创建新 Worker，旧 Worker 处理完请求后退出。

---

### **五、常见问题排查**
13. **502 Bad Gateway 的可能原因？**  
    - 后端服务崩溃、超时、反向代理配置错误（如后端地址不可达）。

14. **如何记录访问日志和错误日志？**  
    ```nginx
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    ```

---

### **高频考点总结**
- **反向代理与负载均衡**：配置方法、算法选择（IP Hash 解决会话保持）。  
- **Location 优先级**：精确匹配 > 前缀匹配 > 正则匹配 > 通用匹配。  
- **动静分离**：通过 Location 规则分离静态文件与动态请求。  
- **性能优化参数**：Worker 数量、连接数、epoll、sendfile。  
- **热部署原理**：多进程模型下无缝切换配置。

掌握这些知识点，能覆盖 90% 的 Nginx 面试问题！建议结合实践配置加深理解。