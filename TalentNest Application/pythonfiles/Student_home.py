import sqlite3
def get_jobs_by_application_status(usn):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()
    
    # Get applied job IDs
    cursor.execute("SELECT job_id FROM student_applications WHERE usn = ?", (usn,))
    applied_ids = {row[0] for row in cursor.fetchall()}

    # Get all jobs
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    
    conn.close()
    
    # Categorize manually in Python
    applied = []
    not_applied = []
    for job in jobs:
        job_dict = dict(id=job[0], job_role=job[1], company=job[2], package=job[3], job_description=job[4])
        if job[0] in applied_ids:
            applied.append(job_dict)
        else:
            not_applied.append(job_dict)

    return {"applied": applied, "not_applied": not_applied}

def apply_job(usn, job_id):
    conn2 = sqlite3.connect('db/hireme.db')
    cursor2 = conn2.cursor()
    cursor2.execute('''INSERT INTO student_applications (job_id)VALUES (?)''', (job_id))
    conn2.commit()
    conn2.close()
def fetch_job_details(job_id):
    conn3 = sqlite3.connect('db/hireme.db')
    cursor3 = conn3.cursor()
    cursor3.execute('SELECT * FROM jobs WHERE id =?', (job_id,))
    job = cursor3.fetchone()
    conn3.close()
    if job:
        return  {
        "job_role": job[1], 
        "company": job[2],
        "package": job[3],
        "job_description": job[4]} 
    else:
        return None 
    
         
         