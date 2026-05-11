from flask import Flask, render_template, request, redirect
from detector import detect_scam
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():

    result = None

    if request.method == 'POST':

        job_text = request.form['job_text']

        result = detect_scam(job_text)

        # Save scan to database
        conn = sqlite3.connect("scam_jobs.db")

        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO scans (job_text, result, probability)

        VALUES (?, ?, ?)

        """, (

            job_text,

            result["result"],

            result["percentage"]

        ))

        conn.commit()

        conn.close()

    # Fetch scan history
    conn = sqlite3.connect("scam_jobs.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scans")

    history = cursor.fetchall()

    conn.close()

    # Dashboard counts
    safe_count = 0
    suspicious_count = 0
    scam_count = 0

    for row in history:

        if row[2] == "Real Job":

            safe_count += 1

        elif row[2] == "Suspicious Job Post":

            suspicious_count += 1

        else:

            scam_count += 1

    return render_template(

        'index.html',

        result=result,

        history=history,

        safe_count=safe_count,

        suspicious_count=suspicious_count,

        scam_count=scam_count

    )

@app.route('/delete/<int:id>')

def delete(id):

    conn = sqlite3.connect("scam_jobs.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM scans WHERE id = ?", (id,))

    conn.commit()

    conn.close()

    return redirect('/')

if __name__ == '__main__':

    app.run(debug=True)