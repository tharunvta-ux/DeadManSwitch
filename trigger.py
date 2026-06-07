import sqlite3
from datetime import datetime
from emailer import send_email


def update_checkin(user_id):

    conn = sqlite3.connect("deadman.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET last_checkin=?
        WHERE id=?
    """, (
        datetime.now().strftime("%Y-%m-%d"),
        user_id
    ))

    conn.commit()
    conn.close()


def get_status(user):

    last_checkin = datetime.strptime(
        user[5],
        "%Y-%m-%d"
    )

    interval = user[4]

    days_passed = (
        datetime.now() - last_checkin
    ).days

    if days_passed > interval:
        return f"OVERDUE ({days_passed} days)"

    return f"ACTIVE ({days_passed} days)"



def release_messages(user_id):

    conn = sqlite3.connect("deadman.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM messages
        WHERE user_id=? AND is_sent=0
    """, (user_id,))

    messages = cursor.fetchall()

    sent_count = 0

    for msg in messages:

        message_id = msg[0]
        recipient_email = msg[3]
        subject = msg[4]
        body = msg[5]

        success = send_email(
            recipient_email,
            subject,
            body
        )

        if success:

            cursor.execute("""
                UPDATE messages
                SET is_sent=1
                WHERE id=?
            """, (message_id,))

            sent_count += 1

    conn.commit()
    conn.close()

    return sent_count