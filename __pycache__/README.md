# NL2SQL Demo — 自然语言转 SQL 探索与实验演示

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-brightgreen.svg)](https://www.sqlite.org/)

一个轻量级的自然语言转 SQL 演示系统，基于关键词匹配与正则表达式的规则驱动方法，用于展示 Text-to-SQL 技术的基本工作流程。

## 📖 项目背景

本项目是“自然语言转SQL技术研究”课程设计的一部分。项目旨在通过构建一个基于规则的 Text-to-SQL 演示系统，帮助理解自然语言查询到 SQL 语句转换的核心流程、方法局限以及技术挑战。

## ✨ 支持的自然语言查询示例

- 查询所有学生
- 计算机1班的学生
- 成绩最高的学生
- 姓名、年龄、成绩查询
- 年龄大于20的学生
- 成绩大于80分的计算机1班学生

## 🏗️ 系统架构

```
用户输入 → NLP解析（关键词+正则） → SQL生成 → SQL执行 → 格式化输出
```

### 模块说明

| 模块文件 | 功能描述 |
|---------|----------|
| `init_db.py` | 初始化 SQLite 数据库，创建 `students` 表并插入测试数据 |
| `nlp_parser.py` | 核心解析模块：将自然语言转换为 SQL 语句 |
| `query_executor.py` | 执行 SQL 并格式化输出查询结果 |
| `main.py` | 程序入口，提供命令行交互界面 |

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/nl2sql-demo.git
cd nl2sql-demo
```

### 2. 运行系统

```bash
python main.py
```

### 3. 输入查询体验

```
===== 自然语言 → SQL 演示系统（规则版）=====
支持查询示例：
  - 查询所有学生
  - 计算机1班的学生
  - 成绩最高的学生
  - 输入 exit 退出

请输入查询：计算机1班的学生
```

## 🧠 解析规则示例（nlp_parser.py）

### SELECT 字段映射

| 自然语言关键词 | SQL 生成 |
|---------------|----------|
| 所有 / 全部 | `SELECT *` |
| 姓名 | `SELECT name` |
| 成绩 / 分数 | `SELECT name, score` |

### WHERE 条件生成

- 班级匹配：`计算机1班` → `WHERE class = '计算机1班'`
- 年龄比较：`年龄大于20` → `WHERE age > 20`

### ORDER BY 规则

- `成绩最高的学生` → `ORDER BY score DESC LIMIT 1`

## 📊 示例运行效果

```
请输入查询：成绩最高的学生

生成的SQL：
   SELECT name, score FROM students ORDER BY score DESC LIMIT 1

查询结果：
   ('王五', 92.5)
--------------------------------------------------
```

## 🧪 技术局限性（规则驱动方法）

- ❌ 不支持复杂逻辑（嵌套查询、多表 JOIN）
- ❌ 对输入表达变化敏感（如“分数最高”≠“成绩最高”）
- ❌ 无法处理口语化、省略、歧义表达
- ✅ 逻辑透明，完全可控，适合教学演示

## 📚 相关理论

本项目基于以下 Text-to-SQL 技术阶段：

> 规则驱动（Rule-based） → 深度学习（Seq2Seq） → 大模型驱动（LLM）

详细理论请参阅项目文档：`自然语言转SQL技术研究.doc`

## 📁 项目结构

```
nl2sql-demo/
├── init_db.py          # 数据库初始化
├── nlp_parser.py       # 自然语言解析器
├── query_executor.py   # SQL执行与格式化
├── main.py             # 主程序入口
├── students.db         # SQLite数据库
└── README.md           # 项目说明
```


## 📄 许可证

本项目仅供学习与教学演示使用。

## 🔗 参考资料

- [WikiSQL Dataset](https://github.com/salesforce/WikiSQL)
- [Spider Dataset](https://yale-lily.github.io/spider)
- [BIRD Benchmark](https://bird-bench.github.io/)
```

