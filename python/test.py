import unittest

from main import sort_by_values_and_keys, symbol_counts


class TestSymbolCounts(unittest.TestCase):

    def test_empty_text(self):
        text = ''
        expected = {}

        actual = symbol_counts(text)

        self.assertDictEqual(expected, actual)

    def test_text_with_uniq_symbols(self):
        text = 'abc'
        expected = {'a': 1, 'b': 1, 'c': 1}

        actual = symbol_counts(text)

        self.assertDictEqual(expected, actual)

    def test_text_with_spaces(self):
        text = ' a b '
        expected = {'a': 1, 'b': 1}

        actual = symbol_counts(text)

        self.assertDictEqual(expected, actual)

    def test_text_with_duplicated_symbols(self):
        text = 'aaa'
        expected = {'a': 3}

        actual = symbol_counts(text)

        self.assertDictEqual(expected, actual)


class TestSortByValuesAndKeys(unittest.TestCase):

    def test_empty_collection(self):
        collection = {}
        expected = []

        actual = sort_by_values_and_keys(collection)

        self.assertListEqual(expected, actual)

    def test_collection_ascending_with_uniq_values(self):
        collection = {'a': 1, 'b': 3, 'c': 2}
        expected = [('a', 1), ('c', 2), ('b', 3)]

        actual = sort_by_values_and_keys(collection, reverse=False)

        self.assertListEqual(expected, actual)

    def test_collection_descending_with_uniq_values(self):
        collection = {'a': 1, 'b': 3, 'c': 2}
        expected = [('b', 3), ('c', 2), ('a', 1)]

        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)

    def test_collection_ascending_with_equal_values(self):
        collection = {'a': 0, 'c': 0, 'b': 0}
        expected = [('a', 0), ('b', 0), ('c', 0)]

        actual = sort_by_values_and_keys(collection, reverse=False)

        self.assertListEqual(expected, actual)

    def test_collection_descending_with_equal_values(self):
        collection = {'a': 0, 'c': 0, 'b': 0}
        expected = [('c', 0), ('b', 0), ('a', 0)]

        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)


class TestOfIntegration(unittest.TestCase):

    def test_hello_world(self):
        text = 'Hello World!'
        expected = [
                ('l', 3),
                ('o', 2),
                ('r', 1),
                ('e', 1),
                ('d', 1),
                ('W', 1),
                ('H', 1),
                ('!', 1),
        ]

        collection = symbol_counts(text)
        actual = sort_by_values_and_keys(collection, reverse=True)

        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
