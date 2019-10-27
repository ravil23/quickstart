from wc import sort_by_values_and_keys, word_counts


def main() -> None:
    text = 'To be, or not to be?'
    counts = word_counts(text)
    sorted_items = sort_by_values_and_keys(counts, reverse=True)
    print('Words count in sentence: "{text}"'.format(text=text))
    for word, count in sorted_items:
        print(word, count)


if __name__ == '__main__':
    main()
