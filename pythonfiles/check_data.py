import sqlite3

# Connect to your correct DB path
conn = sqlite3.connect('../db/hireme.db')

cursor = conn.cursor()

# Check applications
cursor.execute("SELECT * FROM student_applications")
applications = cursor.fetchall()
print("\n📄 Applications:")
for row in applications:
    print(row)

# Check students
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
print("\n🎓 Students:")
for row in students:
    print(row)

# Check jobs
cursor.execute("SELECT * FROM jobs")
jobs = cursor.fetchall()
print("\n💼 Jobs:")
for row in jobs:
    print(row)

conn.close()
