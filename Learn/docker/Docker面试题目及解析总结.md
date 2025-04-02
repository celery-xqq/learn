以下是 Docker 常见的面试题目及简要解析，涵盖基础到进阶知识点，帮助候选人系统复习：

---

### **一、基础概念**
1. **Docker 和虚拟机的区别是什么？**  
   - **虚拟机**：基于 Hypervisor 虚拟化硬件，运行完整操作系统，资源占用高。  
   - **Docker**：利用宿主内核，通过容器隔离进程，轻量快速，资源占用低。

2. **Docker 的核心组件有哪些？**  
   - **Docker Daemon**：后台服务，管理容器生命周期。  
   - **Docker Client**：命令行工具，与 Daemon 交互。  
   - **Images**：只读模板，用于创建容器。  
   - **Registry**：镜像仓库（如 Docker Hub）。

3. **Docker 的优势有哪些？**  
   - 环境一致性、快速部署、资源隔离、易于扩展、微服务友好。

---

### **二、镜像与容器管理**
4. **如何从镜像启动一个容器？**  
   ```bash
   docker run -d --name my_container -p 8080:80 nginx:latest
   ```
   - `-d`：后台运行，`-p`：端口映射，`--name`：容器命名。

5. **如何查看运行中的容器和所有镜像？**  
   ```bash
   docker ps         # 查看运行中的容器
   docker ps -a      # 查看所有容器（包括已停止的）
   docker images     # 查看本地镜像
   ```

6. **容器停止后如何保留数据？**  
   - 使用 **数据卷（Volume）** 或 **绑定挂载（Bind Mount）** 持久化存储。

---

### **三、Dockerfile**
7. **Dockerfile 中的常见指令有哪些？**  
   - `FROM`：基础镜像。  
   - `COPY/ADD`：复制文件。  
   - `RUN`：执行命令。  
   - `EXPOSE`：声明端口。  
   - `CMD/ENTRYPOINT`：容器启动命令。

8. **如何优化 Docker 镜像体积？**  
   - 使用 Alpine 等小基础镜像。  
   - 合并多个 `RUN` 命令，清理缓存。  
   - **多阶段构建**：分离编译环境和运行环境。

9. **多阶段构建的作用是什么？举例说明。**  
   ```Dockerfile
   # 第一阶段：编译应用
   FROM golang:1.18 AS builder
   COPY . .
   RUN go build -o app .

   # 第二阶段：仅复制二进制文件到小镜像
   FROM alpine:latest
   COPY --from=builder /app .
   CMD ["./app"]
   ```

---

### **四、网络与存储**
10. **Docker 网络模式有哪些？**  
    - `bridge`（默认）：容器通过虚拟网桥通信。  
    - `host`：直接使用宿主机网络。  
    - `none`：无网络。  
    - `overlay`：跨主机容器通信（Swarm/Kubernetes）。

11. **如何实现容器间通信？**  
    - 使用自定义 bridge 网络：  
      ```bash
      docker network create my_network
      docker run --network=my_network ...
      ```

12. **数据卷（Volume）和绑定挂载（Bind Mount）的区别？**  
    - **Volume**：由 Docker 管理，存储在 `/var/lib/docker/volumes`。  
    - **Bind Mount**：直接挂载宿主机目录。

---

### **五、Docker Compose**
13. **Docker Compose 的作用是什么？**  
    - 通过 YAML 文件定义多容器应用，实现一键启动、停止。

14. **编写一个 Compose 文件启动 Web + Redis 服务**  
    ```yaml
    version: "3"
    services:
      web:
        image: nginx
        ports: ["80:80"]
      redis:
        image: redis
        volumes: ["redis_data:/data"]
    volumes:
      redis_data:
    ```

---

### **六、进阶与实战**
15. **如何查看容器日志？**  
    ```bash
    docker logs [容器ID]        # 查看日志
    docker logs -f [容器ID]    # 实时追踪日志
    ```

16. **容器如何与宿主机复制文件？**  
    ```bash
    docker cp [容器ID]:/path/to/file /host/path   # 从容器复制到宿主机
    docker cp /host/path [容器ID]:/path/to/file   # 反向复制
    ```

17. **如何调试运行中的容器？**  
    - 进入容器内部：  
      ```bash
      docker exec -it [容器ID] /bin/bash
      ```

18. **Docker 安全最佳实践有哪些？**  
    - 避免以 root 用户运行容器（使用 `USER` 指令）。  
    - 定期更新镜像和依赖。  
    - 限制容器资源（CPU、内存）。  
    - 扫描镜像漏洞（如 `docker scan`）。

---

### **七、容器编排**
19. **Docker Swarm 和 Kubernetes 的区别？**  
    - **Swarm**：Docker 原生，简单易用，适合小规模集群。  
    - **Kubernetes**：功能强大，生态丰富，适合大规模复杂场景。

20. **什么是容器编排？解决了什么问题？**  
    - 自动化部署、扩展、管理容器集群，解决微服务架构下的多容器调度问题。

---

### **八、场景问题**
21. **如何清理无用的 Docker 资源？**  
    ```bash
    docker system prune      # 清理停止的容器、未使用的镜像和网络
    docker volume prune      # 清理未使用的数据卷
    ```

22. **如何实现容器的健康检查？**  
    - 在 Dockerfile 中使用 `HEALTHCHECK` 指令，或在 Compose 中配置 `healthcheck` 参数。

23. **CI/CD 中如何集成 Docker？**  
    - 构建镜像并推送到私有仓库，在部署阶段拉取镜像运行（如 GitLab CI、Jenkins Pipeline）。

---

掌握这些问题后，候选人可覆盖 Docker 的核心知识点，应对多数面试场景。建议结合实战经验（如部署项目、优化镜像）加深理解。