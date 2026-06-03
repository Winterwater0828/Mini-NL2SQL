import re

class SimpleNLToSQL:
    def __init__(self):
        self.table = "students"
        self.columns = ["name", "age", "score", "class"]

    def parse(self, query: str):
        """
        输入：用户自然语言
        输出：SQL 字符串 or None
        """
        query = query.lower()

        # ---------- 1. SELECT 字段映射 ----------
        if "所有" in query or "全部" in query:
            select_clause = "SELECT *"
        elif "姓名" in query:
            select_clause = "SELECT name"
        elif "年龄" in query and "姓名" not in query:
            select_clause = "SELECT age"
        elif "成绩" in query or "分数" in query:
            select_clause = "SELECT name, score"
        else:
            select_clause = "SELECT *"

        # ---------- 2. WHERE 条件 ----------
        where_clause = ""
        # 年龄条件：大于 / 小于 / 等于
        age_match = re.search(r"年龄[大>于]?\s*(\d+)", query)
        if age_match:
            age_val = age_match.group(1)
            if "大于" in query or "以上" in query or ">" in query:
                where_clause = f"WHERE age > {age_val}"
            elif "小于" in query or "以下" in query:
                where_clause = f"WHERE age < {age_val}"
            else:
                where_clause = f"WHERE age = {age_val}"

        # 班级条件
        class_match = re.search(r"([计算机|软件|大数据]*\d*班)", query)
        if class_match and not where_clause:
            class_name = class_match.group(1)
            where_clause = f"WHERE class = '{class_name}'"
        elif class_match and where_clause:
            # 已有年龄条件，追加 AND
            class_name = class_match.group(1)
            where_clause += f" AND class = '{class_name}'"

        # 成绩条件
        if "成绩大于" in query or "分数大于" in query:
            score_match = re.search(r"大于\s*(\d+)", query)
            if score_match:
                score_val = score_match.group(1)
                if where_clause:
                    where_clause += f" AND score > {score_val}"
                else:
                    where_clause = f"WHERE score > {score_val}"

        # ---------- 3. 排序 ----------
        order_clause = ""
        if "最高" in query or "最大" in query:
            if "年龄" in query:
                order_clause = "ORDER BY age DESC LIMIT 1"
            elif "成绩" in query or "分数" in query:
                order_clause = "ORDER BY score DESC LIMIT 1"

        # ---------- 4. 组装 SQL ----------
        sql = f"{select_clause} FROM {self.table} {where_clause} {order_clause}".strip()
        # 清理多余空格
        sql = re.sub(r"\s+", " ", sql)
        return sql