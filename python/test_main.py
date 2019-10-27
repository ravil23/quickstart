import unittest

from wc import sort_by_values_and_keys, word_counts


class TestWordCounts(unittest.TestCase):

    def test_empty_text(self) -> None:
        text = ''
        expected = {}

        actual = word_counts(text)

        self.assertDictEqual(expected, actual)

    def test_text_with_uniq_words(self) -> None:
        text = 'a b c'
        expected = {'a': 1, 'b': 1, 'c': 1}

        actual = word_counts(text)

        self.assertDictEqual(expected, actual)

    def test_text_with_extra_symbols(self) -> None:
        text = ' a,  1b c?'
        expected = {'a': 1, 'b': 1, 'c': 1}

        actual = word_counts(text)

        self.assertDictEqual(expected, actual)

    def test_text_with_duplicated_words(self) -> None:
        text = 'Ab ab aB AB'
        expected = {'ab': 4}

        actual = word_counts(text)

        self.assertDictEqual(expected, actual)


class TestSortByValuesAndKeys(unittest.TestCase):

    def test_empty_collection(self) -> None:
        collection = {}
        expected = []

        actual = sort_by_values_and_keys(collection)

        self.assertListEqual(expected, actual)

    def test_collection_ascending_with_uniq_values(self) -> None:
        collection = {'a': 1, 'b': 3, 'c': 2}
        expected = [(1, 'a'), (2, 'c'), (3, 'b')]

        actual = sort_by_values_and_keys(collection, reverse=False)

        self.assertListEqual(expected, actual)

    def test_collection_descending_with_uniq_values(self) -> None:
        collection = {'a': 1, 'b': 3, 'c': 2}
        expected = [(3, 'b'), (2, 'c'), (1, 'a')]

        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)

    def test_collection_ascending_with_equal_values(self) -> None:
        collection = {'b': 0, 'c': 0, 'a': 0}
        expected = [(0, 'a'), (0, 'b'), (0, 'c')]

        actual = sort_by_values_and_keys(collection, reverse=False)

        self.assertListEqual(expected, actual)

    def test_collection_descending_with_equal_values(self) -> None:
        collection = {'a': 0, 'c': 0, 'b': 0}
        expected = [(0, 'c'), (0, 'b'), (0, 'a')]

        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)


class TestOfIntegration(unittest.TestCase):

    def test_example(self) -> None:
        text = 'To be, or not to be?'
        expected = [
                (2, 'to'),
                (2, 'be'),
                (1, 'or'),
                (1, 'not'),
        ]

        collection = word_counts(text)
        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)
