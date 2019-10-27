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
            collection.items(),
            key=lambda x: (x[1], x[0]),
            reverse=reverse,
    )


def main() -> None:
    text = 'To be, or not to be?'
    counts = word_counts(text)
    sorted_items = sort_by_values_and_keys(counts, reverse=True)
    print('Words count in sentence: "{text}"'.format(text=text))
    for word, count in sorted_items:
        print(word, count)


if __name__ == '__main__':
    main()
