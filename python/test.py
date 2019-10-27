import unittest

from main import sort_by_values_and_keys, word_counts


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
        expected = [('a', 1), ('c', 2), ('b', 3)]

        actual = sort_by_values_and_keys(collection, reverse=False)

        self.assertListEqual(expected, actual)

    def test_collection_descending_with_uniq_values(self) -> None:
        collection = {'a': 1, 'b': 3, 'c': 2}
        expected = [('b', 3), ('c', 2), ('a', 1)]

        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)

    def test_collection_ascending_with_equal_values(self) -> None:
        collection = {'a': 0, 'c': 0, 'b': 0}
        expected = [('a', 0), ('b', 0), ('c', 0)]

        actual = sort_by_values_and_keys(collection, reverse=False)

        self.assertListEqual(expected, actual)

    def test_collection_descending_with_equal_values(self) -> None:
        collection = {'a': 0, 'c': 0, 'b': 0}
        expected = [('c', 0), ('b', 0), ('a', 0)]

        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)


class TestOfIntegration(unittest.TestCase):

    def test_example(self) -> None:
        text = 'To be, or not to be?'
        expected = [
                ('to', 2),
                ('be', 2),
                ('or', 1),
                ('not', 1),
        ]

        collection = word_counts(text)
        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
