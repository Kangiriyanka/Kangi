

from typing import List


def process_word_list(field: str) -> List[str]:
    """Convert a comma-separated string to a list of stripped strings."""
    return [w.strip() for w in field.split(",") if w.strip()]