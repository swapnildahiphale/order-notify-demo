from notifications import email


def test_send_email_appends_to_outbox():
    email.clear()
    email.send_email("a@example.com", "Hello", "World")
    assert email.outbox == [{"to": "a@example.com", "subject": "Hello", "body": "World"}]
