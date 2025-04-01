以下是在 Mac 电脑上安装 AI 编程工具 Cursor 的详细教程，结合了官方指南和社区实践经验：

---

### 一、下载与安装
#### 1. **通过官网下载安装**
- 访问 [Cursor 官网](https://www.cursor.com/)，点击 **Download for Mac** 获取 `.dmg` 安装包。
- 双击下载的 `.dmg` 文件，将 **Cursor 图标拖拽到 Applications 文件夹** 完成安装。
- 首次启动时，系统可能提示安全验证，需在 **系统设置 > 隐私与安全性** 中允许运行。

#### 2. **通过 Homebrew 安装（推荐开发者）**
- 打开终端，输入以下命令安装 Homebrew（若未安装）：
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
- 安装 Cursor：
  ```bash
  brew install --cask cursor
  ```
  此方式可简化后续更新流程。

---

### 二、首次启动与基础设置
#### 1. **语言设置**
- 默认界面为英文，可通过快捷键 `Ctrl+Shift+X` 打开插件市场，搜索 **Chinese (Simplified)** 插件并安装，重启生效。

#### 2. **账户注册与登录**
- 打开 Cursor 后，点击 **Sign Up** 注册新账户（支持 GitHub 或邮箱注册）。
- 注册后可免费体验 **14 天 Pro 会员**，解锁高级模型（如 Claude-3.5-Sonnet 和 GPT-4o）。

#### 3. **基础配置**
- **主题设置**：在 `Settings > Theme` 中选择深色/浅色模式。
- **快捷键绑定**：建议开启 `Tab 补全` 和 `Composer` 功能，路径为 `Settings > Features`。

---

### 三、核心功能使用指南
#### 1. **AI 代码生成**
- **快捷键生成**：在编辑器中按 `Command + K`，输入自然语言指令（如“用 Python 实现快速排序算法”），Cursor 将自动生成代码并插入当前文件。
- **上下文增强**：使用 `@` 注记调用上下文：
  - `@Files`：引入指定文件内容。
  - `@Code`：引用代码块。
  - `@Web`：联网搜索解决方案。

#### 2. **代码优化与调试**
- 选中代码后右键选择 **Explain Code**，获取逻辑解释。
- 按 `Command + L` 打开对话窗口，输入报错信息或优化需求（如“优化这段代码的性能”）。

#### 3. **项目管理**
- **新建项目**：通过 `File > New Project` 创建，支持从 Git 克隆仓库。
- **版本控制**：内置 Git 功能，可在 `Source Control` 面板提交、推送代码。

---

### 四、高级功能与优化
#### 1. **Yolo 模式（自动化开发）**
- 在 `Settings > Features` 中启用 **Enable Yolo Mode**，Cursor 将自动执行代码生成、依赖安装及运行测试，适合快速原型开发。

#### 2. **关闭自动更新**
- 若需锁定版本，进入 `Settings > Application > Update`，将更新模式设为 **None**，并保持 Cursor 常驻后台避免强制升级。

#### 3. **无限白嫖方案**
- Pro 试用到期后，可通过 **删除账户重新注册** 或使用临时邮箱（如 [2925.com](https://www.2925.com)）无限续期。

---

### 五、常见问题解决
- **安装失败**：检查 macOS 版本是否 ≥ 10.15，或尝试终端命令 `xcode-select --install` 安装开发者工具。
- **中文插件失效**：重启 Cursor 或重新安装插件。
- **模型响应慢**：切换至 `gpt-4o-mini` 或 `cursor-small` 模型节省配额。

---

通过以上步骤，你可以在 Mac 上高效使用 Cursor 进行 AI 辅助编程。如需进一步探索高级功能（如多模态开发或企业级集成），可参考 [Cursor 官方文档](https://docs.cursor.com/) 或社区教程。