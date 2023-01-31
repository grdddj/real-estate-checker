from __future__ import annotations

import requests
from pathlib import Path
import json

from bs4 import BeautifulSoup

HERE = Path(__file__).parent

JSON_DB = HERE / "json_db.json"

if not JSON_DB.exists():
    with open(JSON_DB, "w") as f:
        json.dump({}, f)

user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
)
request_headers = {"User-Agent": user_agent}


def get_response(url: str) -> requests.Response:
    return requests.get(url, headers=request_headers)


def get_response_text(url: str) -> str:
    return get_response(url).text


def get_response_json(url: str) -> dict:
    return get_response(url).json()


def get_soup(url: str) -> BeautifulSoup:
    return BeautifulSoup(get_response_text(url), "html.parser")


def get_old_flats(website_name: str) -> list[str]:
    with open(JSON_DB, "r") as f:
        json_db = json.load(f)
    if website_name not in json_db:
        return []
    return json_db[website_name]


def include_new_flats(website_name: str, new_flats: list[str]) -> None:
    with open(JSON_DB, "r") as f:
        json_db = json.load(f)
    if website_name not in json_db:
        json_db[website_name] = []
    json_db[website_name] = list(set(json_db[website_name] + new_flats))
    with open(JSON_DB, "w") as f:
        json.dump(json_db, f, indent=4)


class Base:
    url: str

    def __init__(self):
        pass

    def name(self) -> str:
        return self.__class__.__name__

    def get_current(self) -> list[str]:
        raise NotImplementedError

    def get_old(self) -> list[str]:
        return get_old_flats(self.name())

    def get_new(self) -> list[str]:
        current = self.get_current()
        old = self.get_old()
        return [flat for flat in current if flat not in old]

    def save_new(self, new: list[str]) -> None:
        include_new_flats(self.name(), new)

    def string_to_report(self, info: str) -> str:
        return f"Website: {self.name()}\nCommon URL:{self.url}\nDetail URL:{info}"

    def to_report(self) -> list[str]:
        new = self.get_new()
        if not new:
            return []
        self.save_new(new)
        return [self.string_to_report(info) for info in new]
