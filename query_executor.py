import sqlite3

def execute_sql(sql: str):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"SQL执行错误: {e}"

def format_result(rows, sql):
    print("\n生成的SQL：")
    print(f"   {sql}")
    print("\n查询结果：")
    if isinstance(rows, str):
        print(rows)
    elif not rows:
        print("   (无数据)")
    else:
        for row in rows:
            print(f"   {row}")
    print("-" * 50)