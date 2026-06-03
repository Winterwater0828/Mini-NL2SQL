from init_db import init_database
from nlp_parser import SimpleNLToSQL
from query_executor import execute_sql, format_result

def main():
    init_database()  # 确保数据库存在
    parser = SimpleNLToSQL()

    print("===== 自然语言 → SQL 演示系统（规则版）=====")
    print("支持查询示例：")
    print("  - 查询所有学生")
    print("  - 计算机1班的学生")
    print("  - 成绩最高的学生")
    print("  - 输入 exit 退出\n")

    while True:
        query = input("请输入查询：").strip()
        if query.lower() == "exit":
            break
        if not query:
            continue

        sql = parser.parse(query)
        if not sql:
            print("无法解析该查询，请尝试更简单的表达")
            continue

        result = execute_sql(sql)
        format_result(result, sql)

if __name__ == "__main__":
    main()