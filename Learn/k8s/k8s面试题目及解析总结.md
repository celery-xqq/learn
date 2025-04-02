以下是 Kubernetes 常见的面试题目及解析，涵盖基础概念、架构设计、网络存储、运维管理等核心知识点，帮助候选人系统复习：

---

### **一、基础概念**
1. **Kubernetes 是什么？核心功能是什么？**  
   Kubernetes 是一个开源的容器编排平台，核心功能包括自动化部署、弹性伸缩、负载均衡、服务发现、自我修复等。它通过声明式配置管理容器化应用，支持多云和混合云环境。

2. **Kubernetes 和 Docker 的关系是什么？**  
   Docker 负责容器的生命周期管理和镜像构建，而 Kubernetes 用于编排和管理跨主机的容器集群，实现服务通信、资源调度和扩展。

3. **什么是 Pod？为什么它是 Kubernetes 的最小调度单元？**  
   Pod 是 Kubernetes 的最小部署单元，包含一个或多个共享网络和存储的容器。Pod 内的容器通过 `localhost` 直接通信，共享同一网络命名空间，适合微服务场景。

---

### **二、架构与组件**
4. **Kubernetes 集群的架构包含哪些核心组件？**  
   - **Master 节点**：  
     - **API Server**：集群操作的唯一入口，处理 REST 请求。  
     - **Scheduler**：调度 Pod 到合适的 Node。  
     - **Controller Manager**：执行节点管理、副本控制等控制器。  
     - **etcd**：分布式键值数据库，存储集群状态。  
   - **Worker 节点**：  
     - **kubelet**：管理 Pod 生命周期。  
     - **kube-proxy**：实现 Service 的负载均衡和网络代理。  
     - **容器运行时**（如 Docker、containerd）。

5. **etcd 的作用和特点是什么？**  
   etcd 是分布式键值存储，用于保存集群配置和状态数据。特点包括高可用（基于 Raft 算法）、强一致性、支持 HTTPS 访问，适用于服务发现和配置管理。

---

### **三、网络与存储**
6. **Kubernetes 的网络模型如何实现跨节点通信？**  
   - **Pod 唯一 IP**：每个 Pod 分配独立 IP，直接通过 IP 通信，无需 NAT。  
   - **CNI 插件**：如 Flannel（基于 VXLAN）、Calico（基于 BGP）实现跨节点网络互联。

7. **Service 的作用及类型有哪些？**  
   Service 抽象一组 Pod 并提供稳定的访问入口。类型包括：  
   - **ClusterIP**：集群内部访问。  
   - **NodePort**：通过节点端口暴露服务。  
   - **LoadBalancer**：云平台提供的负载均衡器。

8. **如何实现持久化存储？**  
   - **PersistentVolume (PV)**：集群级存储资源。  
   - **PersistentVolumeClaim (PVC)**：用户对存储资源的请求。  
   - **StorageClass**：动态按需创建 PV。

---

### **四、运维与安全**
9. **如何实现滚动更新和回滚？**  
   - **滚动更新**：通过 Deployment 逐步替换旧 Pod，参数 `maxSurge`（最大新增 Pod 数）和 `maxUnavailable`（最大不可用 Pod 数）控制更新节奏。  
   - **回滚**：使用 `kubectl rollout undo deployment/<name>` 回退到上一版本。

10. **Kubernetes 的健康检查机制有哪些？**  
    - **Liveness Probe**：检测容器是否存活，失败则重启。  
    - **Readiness Probe**：检测容器是否就绪，失败则从 Service 移除。  
    - **Startup Probe**：延迟其他探针，适用于启动慢的应用。

11. **如何保证集群安全？**  
    - **RBAC**：基于角色的访问控制。  
    - **Pod 安全策略**：限制容器权限（如禁止特权模式）。  
    - **网络策略**：通过 Calico 等插件限制 Pod 间通信。

---

### **五、高级特性**
12. **StatefulSet 和 Deployment 的区别？**  
    StatefulSet 适用于有状态应用（如数据库），提供稳定的网络标识（Pod 名称、IP）和持久化存储。Deployment 适用于无状态应用，支持滚动更新。

13. **如何实现灰度发布？**  
    - **金丝雀发布**：先部署少量新版本 Pod，逐步替换旧版本。  
    - **蓝绿部署**：通过 Service 切换新旧版本流量。

14. **Helm 的作用是什么？**  
    Helm 是 Kubernetes 的包管理工具，通过 Chart 定义应用及其依赖，简化复杂应用的部署和管理。

---

### **六、场景与故障排查**
15. **如何排查 Pod 无法启动的问题？**  
    - `kubectl describe pod <name>`：查看事件和错误信息。  
    - `kubectl logs <pod-name>`：检查容器日志。  
    - 资源不足：检查 Node 的 CPU/内存使用情况。

16. **Service 无法访问的可能原因？**  
    - Endpoints 未正确关联 Pod（标签不匹配）。  
    - 网络策略限制流量。  
    - kube-proxy 配置错误。

---

### **七、扩展知识**
17. **什么是 Service Mesh？举例说明其作用。**  
    Service Mesh（如 Istio）提供微服务间通信的流量管理、安全认证和监控，通过 Sidecar 代理（如 Envoy）实现。

18. **Kubernetes 的自动扩缩容机制（HPA）如何工作？**  
    HPA 根据 CPU/内存使用率或自定义指标动态调整 Pod 数量，需配合 Metrics Server 收集监控数据。

---

### **总结**
掌握以上问题可覆盖 Kubernetes 面试的核心考点。建议结合实战经验（如集群搭建、应用部署）加深理解。更多完整问题可参考：[CSDN博客](https://blog.csdn.net/weiwosuoai/article/details/139060279)、[博客园](https://www.cnblogs.com/qinzhi1209/p/18531136.html)。