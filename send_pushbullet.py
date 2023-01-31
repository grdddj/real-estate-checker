import json

import requests

from config import Config


def send_pushbullet_message(title: str, body: str) -> None:
    msg = {"type": "note", "title": title, "body": body}
    resp = requests.post(
        "https://api.pushbullet.com/v2/pushes",
        data=json.dumps(msg),
        headers={
            "Authorization": "Bearer " + Config.PUSHBULLET_TOKEN,
            "Content-Type": "application/json",
        },
    )
    if resp.status_code != 200:
        raise Exception("Error", resp.status_code)
    else:
        print("Message sent")


if __name__ == "__main__":
    # For testing purposes
    send_pushbullet_message(title=Config.subject, body=Config.example_text)
