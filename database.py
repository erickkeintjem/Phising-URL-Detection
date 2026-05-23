import sqlite3


def create_database():

    conn = sqlite3.connect("phishguard.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scan_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        prediction TEXT NOT NULL,
        confidence REAL NOT NULL,
        scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")