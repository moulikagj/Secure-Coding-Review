import sqlite3
import hashlib
import secrets
import hmac

def connect_db():
    return sqlite3.connect("secure_users.db")

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_bytes(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, 1000000
    )
    return salt.hex(), hashed.hex()

def register_user(username, password):
    salt, hashed = hash_password(password)

    with connect_db() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users "
            "(username TEXT UNIQUE, salt TEXT, password_hash TEXT)"
        )
        try:
            conn.execute(
                "INSERT INTO users VALUES (?, ?, ?)",
                (username, salt, hashed)
            )
            return "Registration successful!"
        except sqlite3.IntegrityError:
            return "Username already exists."

def login_user(username, password):
    with connect_db() as conn:
        result = conn.execute(
            "SELECT salt, password_hash FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    if result is None:
        return False

    salt, stored_hash = result
    _, entered_hash = hash_password(
        password, bytes.fromhex(salt)
    )

    return hmac.compare_digest(stored_hash, entered_hash)

if __name__ == "__main__":
    username = input("Create username: ")
    password = input("Create password: ")

    print(register_user(username, password))

    login_name = input("Login username: ")
    login_password = input("Login password: ")

    if login_user(login_name, login_password):
        print("Login successful!")
    else:
        print("Invalid username or password.")