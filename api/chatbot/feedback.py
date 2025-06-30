import sqlite3

def save_feedback(question, response):
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS feedback (question TEXT, response TEXT)")
    c.execute("INSERT INTO feedback VALUES (?, ?)", (question, response))
    conn.commit()
    conn.close()
