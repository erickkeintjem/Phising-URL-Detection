import sqlite3


DATABASE = "phishguard.db"


def save_scan(url, prediction, confidence):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO scan_history
        (
            url,
            prediction,
            confidence
        )
        VALUES (?, ?, ?)
    """, (
        url,
        prediction,
        confidence
    ))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM scan_history
        ORDER BY scan_date DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_statistics():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM scan_history"
    )
    total_scan = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM scan_history
        WHERE prediction='SAFE'
        """
    )
    total_safe = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM scan_history
        WHERE prediction='PHISHING'
        """
    )
    total_phishing = cursor.fetchone()[0]

    conn.close()

    return {
        "total_scan": total_scan,
        "total_safe": total_safe,
        "total_phishing": total_phishing
    }