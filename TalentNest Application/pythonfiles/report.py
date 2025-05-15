import sqlite3

def generate_report():
    # Connect to the correct database (used by your apply_job logic)
    conn = sqlite3.connect('db/hireme.db')  # <- fixed path
    cursor = conn.cursor()
    # Fetch all jobs
    cursor.execute("SELECT id, role, company, package FROM job")
    jobs = {row[0]: {'role': row[1], 'company': row[2], 'package': row[3]} for row in cursor.fetchall()}
    # Build report data
    report_data = []
    for job_id, status in applications:
        job = jobs.get(job_id)
        if  job:
            report_data.append({
                'job_role': job['role'],
                'company': job['company'],
                'package': job['package'],
                'status': status
            })

    conn.close()
    return report_data
