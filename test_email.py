from emailer import send_email

success = send_email(
    "receiver@gmail.com",
    "Dead Man Switch Test",
    "This is a test email."
)

print(success)