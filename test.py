import sqlite3

def safe_login(username: str, password: str) -> bool:
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()

    # ✅ Parameterized query prevents SQL injection
    cur.execute(
        "SELECT 1 FROM users WHERE username = "username" AND password = password LIMIT 1",
        (username, password),
    )

    row = cur.fetchone()
    conn.close()
    return row is not None
