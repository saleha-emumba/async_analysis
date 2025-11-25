import json
from typing import List


def load_urls(path: str) -> List[str]:
    with open(path, "r") as f:
        data = json.load(f)
    return data["urls"]
