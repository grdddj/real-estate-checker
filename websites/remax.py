from __future__ import annotations

import re

from .common import get_soup, Base


class Remax(Base):
    url = "https://www.remax-czech.cz/reality/vyhledavani/?desc_text=Charbulova&regions%5B116%5D%5B3702%5D=on&sale=1&types%5B4%5D=on"

    def get_current(self) -> list[str]:
        soup = get_soup(self.url)
        links = soup.findAll("a")
        links_to_flats: set[str] = set()
        for link in links:
            href = link.get("href")
            if href is None:
                continue
            pattern = r"/reality/detail/\d+/"
            prefix = "https://www.remax-czech.cz"
            if re.match(pattern, href):
                links_to_flats.add(prefix + href)
        return list(links_to_flats)
