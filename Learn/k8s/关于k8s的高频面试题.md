以下是 Kubernetes 高频面试题及其简要解答，涵盖基础概念、架构、核心组件、运维场景等方向，帮助快速掌握核心知识点：

---

### **一、基础概念**
1. **什么是 Kubernetes（k8s）？**  
   Kubernetes 是一个开源的容器编排平台，用于自动化部署、扩展和管理容器化应用，提供声明式配置、自愈、负载均衡等能力。

2. **Pod 是什么？**  
   Pod 是 Kubernetes 的最小调度单元，包含一个或多个共享网络/存储的容器（如主容器+Sidecar）。

3. **Deployment vs StatefulSet**  
   - **Deployment**：管理无状态应用，支持滚动更新、回滚。  
   - **StatefulSet**：管理有状态应用（如数据库），提供稳定的网络标识（如 `pod-name-0`）和持久化存储。

4. **Service 的作用和类型**  
   Service 提供稳定的网络端点访问 Pod，类型包括：  
   - **ClusterIP**（默认，集群内部访问）  
   - **NodePort**（通过节点端口暴露）  
   - **LoadBalancer**（云厂商提供外部负载均衡器）  
   - **ExternalName**（映射到外部 DNS）

5. **ConfigMap 和 Secret 的区别**  
   - **ConfigMap**：存储非敏感配置（如环境变量、配置文件）。  
   - **Secret**：存储敏感数据（如密码、Token），以 Base64 编码存储（非加密）。

---

### **二、架构与组件**
1. **Master 节点组件**  
   - **API Server**：集群操作的入口，处理 REST 请求。  
   - **Scheduler**：将 Pod 调度到合适 Node。  
   - **Controller Manager**：运行控制器（如 Deployment、Node 控制器）。  
   - **etcd**：分布式键值存储，保存集群状态。

2. **Worker 节点组件**  
   - **kubelet**：管理节点上的 Pod 生命周期。  
   - **kube-proxy**：维护节点网络规则（如 iptables/IPVS 实现 Service 流量转发）。  
   - **容器运行时**（如 Docker、containerd）。

3. **kube-proxy 的工作模式**  
   - **iptables**：默认模式，通过规则链转发流量，性能中等。  
   - **IPVS**：基于内核的负载均衡，支持更多算法（如轮询、加权），性能更高。

4. **Ingress 的作用**  
   Ingress 是管理外部访问的 API 对象，通过 Ingress Controller（如 Nginx、Traefik）实现 HTTP/HTTPS 路由、SSL 终止。

---

### **三、网络与存储**
1. **K8s 网络模型的要求**  
   每个 Pod 拥有独立 IP，所有 Pod 可直接跨节点通信，无需 NAT。

2. **Service 如何实现负载均衡？**  
   通过 kube-proxy 维护的 iptables/IPVS 规则，将请求分发到后端 Pod。

3. **Persistent Volume（PV）和 Persistent Volume Claim（PVC）**  
   - **PV**：集群级别的存储资源（如 NFS、云磁盘）。  
   - **PVC**：用户对存储资源的请求，绑定到 PV。

4. **StorageClass 的作用**  
   动态创建 PV，按需为 PVC 分配存储（如自动创建云盘）。

---

### **四、运维与调试**
1. **Pod 的常见状态**  
   - **Pending**：调度中（资源不足或镜像拉取失败）。  
   - **Running**：运行中。  
   - **CrashLoopBackOff**：容器反复崩溃。  
   - **ImagePullBackOff**：镜像拉取失败。

2. **如何查看 Pod 日志？**  
   ```bash
   kubectl logs <pod-name> -c <container-name>  # 查看指定容器日志
   kubectl logs -f <pod-name> --tail=100        # 实时查看尾部日志
   ```

3. **如何进入 Pod 的容器？**  
   ```bash
   kubectl exec -it <pod-name> -- /bin/sh
   ```

4. **如何排查 Pod 无法启动的问题？**  
   - `kubectl describe pod <pod-name>`：查看事件（如镜像错误、资源不足）。  
   - `kubectl get events`：查看集群事件。

---

### **五、进阶场景**
1. **滚动更新与回滚**  
   - Deployment 通过滚动更新逐步替换 Pod，旧版本 ReplicaSet 保留用于回滚。  
   - 回滚命令：  
     ```bash
     kubectl rollout undo deployment/<deployment-name>
     ```

2. **HPA（Horizontal Pod Autoscaler）原理**  
   根据 CPU/内存或自定义指标自动扩缩 Pod 数量，依赖 Metrics Server 提供监控数据。

3. **RBAC 权限控制**  
   通过 Role（命名空间权限）、ClusterRole（集群权限）、RoleBinding、ClusterRoleBinding 实现细粒度权限管理。

4. **K8s 安全最佳实践**  
   - 使用 NetworkPolicy 限制 Pod 网络通信。  
   - 限制容器以非 root 用户运行。  
   - 定期更新集群版本。

---

### **六、场景题示例**
1. **如何实现零停机部署？**  
   配置 Deployment 的 `strategy`：  
   ```yaml
   strategy:
     type: RollingUpdate
     rollingUpdate:
       maxSurge: 1        # 最大临时超出 Pod 数
       maxUnavailable: 0  # 最大不可用 Pod 数
   ```

2. **如何调试 Service 无法访问？**  
   - 检查 Endpoints：`kubectl get endpoints <service-name>`。  
   - 检查 Pod 的标签是否匹配 Service 的 Selector。  
   - 检查 kube-proxy 和网络插件（如 Calico）是否正常。

---

掌握以上问题后，建议结合实践（如 Minikube 或 Kind 集群）加深理解，并熟悉 `kubectl` 常用命令和 YAML 编写。