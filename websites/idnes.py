from __future__ import annotations

import re

from .common import get_soup, Base


class Idnes(Base):
    url = "https://reality.idnes.cz/s/byty/?s-l=ULICE-22128"

    def get_current(self) -> list[str]:
        soup = get_soup(self.url)

        links = soup.findAll("a")
        links_to_flats: set[str] = set()
        for link in links:
            href = link.get("href")
            if href is None:
                continue
            pattern = r"/detail/prodej/"
            if re.search(pattern, href):
                links_to_flats.add(href)
        return list(links_to_flats)
