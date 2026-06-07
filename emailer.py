import smtplib
from email.mime.text import MIMEText


# Replace with YOUR values
SENDER_EMAIL = "tharunvta@gmail.com"
APP_PASSWORD = "ebkz kvce wffd ieoo"


def send_email(receiver_email, subject, body):

    try:

        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(
            SENDER_EMAIL,
            APP_PASSWORD
        )

        server.sendmail(
            SENDER_EMAIL,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        return True

    except Exception as e:
        print("Email Error:", e)
        return False