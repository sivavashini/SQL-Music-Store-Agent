import sqlite3


def execute_query(query):
    conn = sqlite3.connect("dataset/music.db")
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()
    return rows
