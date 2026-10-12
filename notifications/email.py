"""Stub email sender: appends to an in-memory outbox."""

outbox = []


def send_email(to, subject, body):
    outbox.append({"to": to, "subject": subject, "body": body})


def clear():
    outbox.clear()
