from typing import Dict, List, Tuple


def symbol_counts(text: str) -> Dict[str, int]:
    counts = {}
    for symbol in text:
        if symbol != ' ':
            if symbol in counts:
                counts[symbol] += 1
            else:
                counts[symbol] = 1
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
    text = 'Hello world!'
    counts = symbol_counts(text)
    sorted_items = sort_by_values_and_keys(counts, reverse=True)
    print('Symbols count in sequence:', text)
    for symbol, count in sorted_items:
        print(symbol, count)


if __name__ == '__main__':
    main()
