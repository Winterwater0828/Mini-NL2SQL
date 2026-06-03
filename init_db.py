import sqlite3

def init_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            score REAL NOT NULL,
            class TEXT NOT NULL
        )
    """)

    # 插入测试数据
    sample_data = [
        ("张三", 20, 85.5, "计算机1班"),
        ("李四", 21, 78.0, "计算机1班"),
        ("王五", 19, 92.5, "计算机2班"),
        ("赵六", 22, 67.0, "计算机2班"),
        ("小明", 20, 88.0, "计算机1班"),
    ]

    cursor.execute("DELETE FROM students")  # 清空旧数据
    for name, age, score, cls in sample_data:
        cursor.execute(
            "INSERT INTO students (name, age, score, class) VALUES (?, ?, ?, ?)",
            (name, age, score, cls)
        )

    conn.commit()
    conn.close()
    print("数据库初始化完成，表 students 已创建，数据已插入")

if __name__ == "__main__":
    init_database()