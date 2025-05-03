import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

cursor.execute('DELETE FROM students')
cursor.executemany('''
    INSERT INTO students (name, age) VALUES (?, ?)
''', [
    ('Alice', 22),
    ('Bob', 19),
    ('Charlie', 25),
])

cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_name TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
''')

cursor.execute('DELETE FROM courses')

cursor.executemany('''
    INSERT INTO courses (student_id, course_name) VALUES (?, ?)
''', [
    (1, 'Math'),
    (2, 'Biology'),
    (3, 'Python')
])

cursor.execute('''
    SELECT students.name, courses.course_name
    FROM students
    JOIN courses ON students.id = courses.student_id
''')

print('Студенты и их курсы:')
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
