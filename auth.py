import sqlite3
import bcrypt
from datetime import datetime


def register_user(name, email, password, interval_days=7):
    conn = sqlite3.connect("deadman.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Email already exists!")
        conn.close()
        return False

    password_hash = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )

    cursor.execute("""
        INSERT INTO users
        (name,email,password_hash,interval_days,last_checkin)
        VALUES (?,?,?,?,?)
    """, (
        name,
        email,
        password_hash.decode('utf-8'),
        interval_days,
        datetime.now().strftime("%Y-%m-%d")
    ))

    conn.commit()
    conn.close()

    print("Registration Successful!")
    return True


def login_user(email, password):

    conn = sqlite3.connect("deadman.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        print("User not found!")
        return None

    stored_hash = user[3]

    if bcrypt.checkpw(
        password.encode('utf-8'),
        stored_hash.encode('utf-8')
    ):
        print("Login Successful!")
        return user

    print("Incorrect Password!")
    return None