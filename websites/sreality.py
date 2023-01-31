from __future__ import annotations

from .common import get_response_json, Base


class Sreality(Base):
    url = "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=20&region=ulice Charbulova&region_entity_id=79057&region_entity_type=street"

    def get_current(self) -> list[str]:
        json = get_response_json(self.url)
        estates = json["_embedded"]["estates"]
        flat_ids: set[str] = set()
        for estate in estates:
            if "charbulova" in estate["locality"].lower():
                identifier = f"{estate['hash_id']} - {estate['price']},-"
                flat_ids.add(identifier)
        return list(flat_ids)

    def string_to_report(self, info: str) -> str:
        common_url = "https://www.sreality.cz/hledani/prodej/byty?region=ulice%20Charbulova&region-id=79057&region-typ=street"
        return f"Website: {self.name()}\nCommon URL:{common_url}\nDetail URL:{info}"
