from __future__ import annotations

import smtplib
import ssl

from config import Config


def construct_email_message(
    from_addr: str, to_addr: str, subject: str, message_text: str
) -> str:
    return f"""\
From: {from_addr}
To: {to_addr}
Subject: {subject}

{message_text}
"""


def send_email(message_text: str) -> None:
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(Config.smtp_server, Config.port, context=context) as server:
        server.login(Config.sender_email, Config.password)
        for recipient in Config.recipients:
            print(f"Sending mail to {recipient}")
            message = construct_email_message(
                from_addr=Config.sender_email,
                to_addr=recipient,
                subject=Config.subject,
                message_text=message_text,
            )
            server.sendmail(Config.sender_email, recipient, message)


if __name__ == "__main__":
    # For testing purposes
    send_email(message_text=Config.example_text)
