import sqlite3


def add_message(
        user_id,
        recipient_name,
        recipient_email,
        subject,
        message):

    conn = sqlite3.connect("deadman.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO messages
        (
            user_id,
            recipient_name,
            recipient_email,
            subject,
            message
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        recipient_name,
        recipient_email,
        subject,
        message
    ))

    conn.commit()
    conn.close()


def get_messages(user_id):

    conn = sqlite3.connect("deadman.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM messages
        WHERE user_id=?
    """, (user_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def delete_message(message_id):

    conn = sqlite3.connect("deadman.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM messages
        WHERE id=?
    """, (message_id,))

    conn.commit()
    conn.close()