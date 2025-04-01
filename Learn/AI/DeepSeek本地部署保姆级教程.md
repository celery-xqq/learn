以下是本地部署DeepSeek的保姆级教程，综合多种方案供不同需求的用户选择：

---

### **一、基础版部署（基于Ollama）**
**适用场景**：普通用户快速体验，无需编程基础，支持Windows/macOS/Linux。

#### **步骤1：安装Ollama**
1. 访问官网 [https://ollama.com/download](https://ollama.com/download)，选择对应操作系统的版本下载安装。
2. 安装完成后，打开终端（Windows为命令提示符），输入 `ollama --version` 验证是否安装成功。
3. 启动Ollama后台服务（Windows用户需从开始菜单启动，Mac/Linux用户可通过终端运行 `ollama serve`）。

#### **步骤2：选择模型版本**
根据硬件配置选择模型：
- **入门级**（显存≤8GB）：`deepseek-r1:1.5b`（1.5B参数）
- **中端**（显存8-12GB）：`deepseek-r1:7b` 或 `8b`（7B/8B参数）
- **高性能**（显存≥12GB）：`deepseek-r1:14b`、`32b`（需更高配置）

#### **步骤3：运行模型**
在终端输入命令（以7B为例）：
```bash
ollama run deepseek-r1:7b
```
等待下载完成后，直接在终端输入问题即可交互（如“你好”）。退出时输入 `/bye`。

**注意事项**：
- 首次下载模型需较长时间，网络不佳时可能中断，可重试命令继续下载。
- 显存不足可尝试关闭其他程序或选择更小模型。

---

### **二、进阶版部署（图形界面与API调用）**
**适用场景**：需要可视化界面或集成到其他应用。

#### **方案1：使用Chatbox AI**
1. 下载图形界面工具 [Chatbox AI](https://chatboxai.app/zh)。
2. 安装后选择“本地模型”，配置模型路径为 `deepseek-r1:[版本号]`（如7b）。
3. 通过界面直接提问，支持历史记录和格式优化。

#### **方案2：API调用**
1. 确保Ollama服务运行中（默认端口11434）。
2. 使用Python脚本调用：
```python
import requests

url = "http://localhost:11434/api/generate"
data = {
    "model": "deepseek-r1:7b",
    "prompt": "你的问题"
}
response = requests.post(url, json=data)
print(response.json()["response"])
```

---

### **三、高阶部署（vLLM或量化模型）**
**适用场景**：开发者或高性能需求用户，需优化推理速度。

#### **方案1：基于vLLM部署**
1. **安装Python环境**（3.8+）并创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
2. **安装依赖**：
```bash
pip install vllm
```
3. **下载模型**（以7B蒸馏版为例）：
```bash
pip install modelscope
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --local_dir ./model
```
4. **启动服务**：
```bash
CUDA_VISIBLE_DEVICES=0 vllm serve ./model --port 8102
```
5. **调用API**：
参考Python脚本调用本地端口（代码示例见网页7）。

#### **方案2：动态量化模型**
针对671B全量模型，通过HuggingFace下载动态量化版（压缩至131GB），需200GB以上内存，使用多显卡加速。

---

### **四、常见问题**
1. **显存不足**：选择更小模型（如1.5B），或关闭后台程序。
2. **下载中断**：重新运行命令继续下载。
3. **界面卡顿**：使用Chatbox AI或PageAssist插件优化交互体验。

---

### **五、扩展功能**
- **联网支持**：通过PageAssist插件配置DeepSeek API密钥，启用联网提问。
- **集成开发工具**：在VS Code或JetBrains IDE中安装Continue插件，直接调用本地模型辅助编程。

---

通过以上方案，用户可根据自身需求灵活选择部署方式。如需完整代码或更多配置细节，可参考对应来源链接。