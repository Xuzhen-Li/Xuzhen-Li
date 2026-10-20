<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <img alt="Banner: 李旭真, 植物古基因组学与葡萄群体遗传学" src="assets/banner-light.png">
</picture>

[English](README.md) | 中文

我开发分析流程并研究葡萄基因组，关注无性繁殖系、泛基因组、转座子、靶向测序面板、古DNA与群体遗传学理论。

[ORCID 0000-0003-3670-6657](https://orcid.org/0000-0003-3670-6657) | [paper-viz gallery](https://xuzhen-li.github.io/paper-viz/) | [grapeancestry demo](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html)

<table>
  <tr>
    <td width="50%">
      <a href="https://github.com/Xuzhen-Li/paper-viz">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="assets/card-paper-viz-dark.png">
          <img alt="paper-viz: 123个R绘图模板" src="assets/card-paper-viz-light.png">
        </picture>
      </a><br>
      运行120个R语言绘图模板，生成矢量PDF和600 dpi的PNG图。
    </td>
    <td width="50%">
      <a href="https://github.com/Xuzhen-Li/grapeancestry">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="assets/card-grapeancestry-dark.png">
          <img alt="grapeancestry: 167K靶向测序面板分析" src="assets/card-grapeancestry-light.png">
        </picture>
      </a><br>
      将新的葡萄样本映射至2449 × 167K靶向捕获面板，并生成交互式HTML报告。
    </td>
  </tr>
  <tr>
    <td width="50%">
      <a href="https://github.com/Xuzhen-Li/paper-reading">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="assets/card-paper-reading-dark.png">
          <img alt="paper-reading: PDF转图文笔记" src="assets/card-paper-reading-light.png">
        </picture>
      </a><br>
      将本地研究PDF转换为中文图文L3笔记，文件保留在本地。
    </td>
    <td width="50%">
      <a href="https://github.com/Xuzhen-Li/vitis-pangenome">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="assets/card-vitis-pangenome-dark.png">
          <img alt="vitis-pangenome: 泛基因组分析流程" src="assets/card-vitis-pangenome-light.png">
        </picture>
      </a><br>
      运行葡萄泛基因组图谱、存在与缺失变异以及混合变异剂量分析流程。
    </td>
  </tr>
  <tr>
    <td width="50%">
      <a href="https://github.com/Xuzhen-Li/qbar">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="assets/card-qbar-dark.png">
          <img alt="qbar: 排序与绘制结构图" src="assets/card-qbar-light.png">
        </picture>
      </a><br>
      排序ADMIXTURE Q文件，在不同K值间对齐列，并绘制群体结构柱状图。
    </td>
    <td width="50%">
      <a href="https://github.com/Xuzhen-Li/genomics-theory-mining">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="assets/card-genomics-theory-mining-dark.png">
          <img alt="genomics-theory-mining: 测试基因组学理论" src="assets/card-genomics-theory-mining-light.png">
        </picture>
      </a><br>
      挖掘经典基因组学理论，并在现代葡萄无性繁殖系和野生葡萄数据上测试其假设。
    </td>
  </tr>
</table>

## 全部仓库

![葡萄基因组与注释](https://img.shields.io/badge/%E8%91%A1%E8%90%84%E5%9F%BA%E5%9B%A0%E7%BB%84%E4%B8%8E%E6%B3%A8%E9%87%8A-5_%E4%B8%AA%E4%BB%93%E5%BA%93-119B76?style=flat-square)

| 仓库 | 功能说明 |
| --- | --- |
| [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome) | 葡萄泛基因组图谱、存在与缺失变异以及混合变异剂量分析方法的脚本与流程。 |
| [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) | 结构基因组注释流程，从FASTA序列和证据中提供基因模型与GFF3输出。 |
| [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation) | 在结构注释后，为蛋白质序列分配GO、KEGG与结构域等功能标签。 |
| [grapevine-plastid](https://github.com/Xuzhen-Li/grapevine-plastid) · 建设中 | 葡萄质体/叶绿体泛基因组分析笔记。 |
| [vitis-te](https://github.com/Xuzhen-Li/vitis-te) · 建设中 | 葡萄TE文库以及向基因注释流程移交软屏蔽结果的公开占位页。 |

![靶向测序分型芯片](https://img.shields.io/badge/%E9%9D%B6%E5%90%91%E6%B5%8B%E5%BA%8F%E5%88%86%E5%9E%8B%E8%8A%AF%E7%89%87-3_%E4%B8%AA%E4%BB%93%E5%BA%93-595594?style=flat-square)

| 仓库 | 功能说明 |
| --- | --- |
| [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry) | 167K葡萄靶向捕获面板配套工具：血统、同一性、PCA与colour GS。 |
| [gtbs-chip-service-kit](https://github.com/Xuzhen-Li/gtbs-chip-service-kit) | 将现有基因分型芯片注册为配置文件并进行验证。 |
| [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip) | 葡萄捕获阵列/167K芯片设计。 |

![群体遗传](https://img.shields.io/badge/%E7%BE%A4%E4%BD%93%E9%81%97%E4%BC%A0-4_%E4%B8%AA%E4%BB%93%E5%BA%93-F77E12?style=flat-square)

| 仓库 | 功能说明 |
| --- | --- |
| [qbar](https://github.com/Xuzhen-Li/qbar) | 排序ADMIXTURE Q文件，在不同K值间对齐列，并绘制群体结构柱状图。 |
| [TrioConcordance](https://github.com/Xuzhen-Li/TrioConcordance) | 跨三个独立数据集进行逐位点与逐样本的基因型一致性分析Python工具。 |
| [genomics-theory-mining](https://github.com/Xuzhen-Li/genomics-theory-mining) | 挖掘经典基因组学理论，并在现代数据上测试其假设。 |
| [vitis-popgen](https://github.com/Xuzhen-Li/vitis-popgen) · 建设中 | 葡萄群体遗传学与驯化。 |

![古 DNA](https://img.shields.io/badge/%E5%8F%A4_DNA-1_%E4%B8%AA%E4%BB%93%E5%BA%93-CC312C?style=flat-square)

| 仓库 | 功能说明 |
| --- | --- |
| [grapevine-adna](https://github.com/Xuzhen-Li/grapevine-adna) · 建设中 | 葡萄古DNA分析方法与笔记。 |

![工具与技能](https://img.shields.io/badge/%E5%B7%A5%E5%85%B7%E4%B8%8E%E6%8A%80%E8%83%BD-9_%E4%B8%AA%E4%BB%93%E5%BA%93-1F72AE?style=flat-square)

| 仓库 | 功能说明 |
| --- | --- |
| [paper-viz](https://github.com/Xuzhen-Li/paper-viz) | 以 R 为主的出版级图表画廊：123个模板加21个示意图（代码+模拟数据+预览），支持Web浏览与Agent调用。 |
| [paper-reading](https://github.com/Xuzhen-Li/paper-reading) | 将单篇研究PDF转换为中文图文阅读笔记；您的PDF库保存在本地。 |
| [literature-review-skills](https://github.com/Xuzhen-Li/literature-review-skills) | 独立于Agent的文献综述撰写技能套件，并在人工把关处停止，每一项声明均绑定至项目持有的来源。 |
| [patent-drafting-skills](https://github.com/Xuzhen-Li/patent-drafting-skills) | 中英双语的起草发明专利Agent技能——覆盖中美及PCT：公开、现有技术检索、创造性、权利要求、说明书、附图、一致性检查与.docx导出。 |
| [concept-learning](https://github.com/Xuzhen-Li/concept-learning) | 个人制作的Cursor技能：生物学概念课程与BioLogos风格系列写作。 |
| [famous-people](https://github.com/Xuzhen-Li/famous-people) | 个人制作的Cursor技能：将生物学家的科研生涯转为微信长文记录。 |
| [awesome-astra-science](https://github.com/Xuzhen-Li/awesome-astra-science) | AI模型作品集：展示模型实际生成的演示与图表。 |
| [cursor-state-vscdb](https://github.com/Xuzhen-Li/cursor-state-vscdb) | 诊断由数十GB state.vscdb SQLite数据库引起的macOS Cursor卡顿的脚本与案例。 |
| [grok-bot-dispatch](https://github.com/Xuzhen-Li/grok-bot-dispatch) | Cursor技能：Primary作为前门，项目机器人保持未分配状态，角色为共享池上的单任务分配。 |

### 研究方向

| 主题 | 仓库 |
| --- | --- |
| 葡萄基因组 | [vitis-te](https://github.com/Xuzhen-Li/vitis-te) (软屏蔽占位页), [grapevine-plastid](https://github.com/Xuzhen-Li/grapevine-plastid) (待更新方法) |
| 基因组注释 | [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) (基因模型：GFF3 + proteins), [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation) |
| 靶向测序基因分型 | [gtbs-chip-service-kit](https://github.com/Xuzhen-Li/gtbs-chip-service-kit) (验证芯片配置文件；步骤详见steps/), [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip) (设计笔记) |
| 群体遗传学 | [vitis-popgen](https://github.com/Xuzhen-Li/vitis-popgen) (预留项), [TrioConcordance](https://github.com/Xuzhen-Li/TrioConcordance) |
| 古DNA | [grapevine-adna](https://github.com/Xuzhen-Li/grapevine-adna) (预留项) |

