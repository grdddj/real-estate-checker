from __future__ import annotations

import re

from .common import get_soup, Base


class Mmreality(Base):
    url = "https://www.mmreality.cz/nemovitosti/prodej/byty/brno-cernovice/?query=S87Pzc3Piy4uSSwpLY6NNoi1NVRLhoglJpdklqWCBNJT89OLEgsyKqNTUtMSS3NKnPNL80qKKoFyAA%3D%3D"

    def get_current(self) -> list[str]:
        soup = get_soup(self.url)
        links = soup.findAll("a")
        links_to_flats: set[str] = set()
        for link in links:
            href = link.get("href")
            if href is None:
                continue
            pattern = r"https://www.mmreality.cz/nemovitosti/\d+/"
            if re.match(pattern, href):
                links_to_flats.add(href)
        return list(links_to_flats)
