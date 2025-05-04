import sqlite3

def generate_report():
    # Connect to the correct database (used by your apply_job logic)
    conn = sqlite3.connect('db/hireme.db')  # <- fixed path
    cursor = conn.cursor()

    # Fetch all students using USN
    cursor.execute("SELECT usn, name, college FROM student")
    students = {row[0]: {'name': row[1], 'college': row[2]} for row in cursor.fetchall()}

    # Fetch all jobs
    cursor.execute("SELECT id, role, company, package FROM job")
    jobs = {row[0]: {'role': row[1], 'company': row[2], 'package': row[3]} for row in cursor.fetchall()}

    # Fetch student applications
    cursor.execute("SELECT usn, job_id FROM student_applications")
    applications = [(row[0], row[1], 'applied') for row in cursor.fetchall()]

    # Build report data
    report_data = []
    for usn, job_id, status in applications:
        student = students.get(usn)
        job = jobs.get(job_id)
        if student and job:
            report_data.append({
                'student_name': student['name'],
                'college': student['college'],
                'job_role': job['role'],
                'company': job['company'],
                'package': job['package'],
                'status': status
            })

    conn.close()
    return report_data
