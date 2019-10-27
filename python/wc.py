from collections import defaultdict
from typing import Dict, List, Tuple


def word_counts(text: str) -> Dict[str, int]:
    counts = defaultdict(int)
    for part in text.split():
        word = ''.join([i for i in part if i.isalpha()])
        if word != '':
            counts[word.lower()] += 1
    return counts


def sort_by_values_and_keys(
        collection: Dict[str, int],
        reverse: bool = False,
) -> List[Tuple[str, int]]:

    return sorted(
            [(item[1], item[0]) for item in collection.items()],
            reverse=reverse,
    )
