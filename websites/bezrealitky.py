from __future__ import annotations

import re

from .common import get_response_text, Base


class Bezrealitky(Base):
    url = "https://www.bezrealitky.cz/vyhledat?offerType=PRODEJ&estateType=BYT&osm_value=%C4%8Cernovice%2C+Brno%2C+okres+Brno-m%C4%9Bsto%2C+Jihomoravsk%C3%BD+kraj%2C+Jihov%C3%BDchod%2C+%C4%8Cesko&regionOsmIds=R436341"

    def get_current(self) -> list[str]:
        text = get_response_text(self.url)
        pattern = r'"uri":"(.*?)"'
        relative_links = re.findall(pattern, text)
        links = [
            "https://www.bezrealitky.cz/nemovitosti-byty-domy/" + link
            for link in relative_links
        ]
        return links
