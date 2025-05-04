import sqlite3

def delete_job(job_id):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM jobs WHERE id = ?', (job_id,))
    conn.commit()
    conn.close()
