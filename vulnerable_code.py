import sqlite3

SECRET_KEY = "mysecret123"
DEBUG = True

def setup_database():
    conn = sqlite3.connect("vulnerable_users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        ("Moulika G J", "test@1234")
    )

    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect("vulnerable_users.db")

    query = f"""
        SELECT * FROM users
        WHERE username='{username}'
        AND password='{password}'
    """

    result = conn.execute(query).fetchone()
    conn.close()

    return result is not None

if __name__ == "__main__":
    setup_database()

    username = input("Username: ")
    password = input("Password: ")

    if login(username, password):
        print("Login successful!")
    else:
        print("Invalid login!")