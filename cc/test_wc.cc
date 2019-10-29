#include "gmock/gmock.h"
#include "gtest/gtest.h"

#include "wc.h"


namespace quickstart {

class TestWordCounts : public ::testing::Test {
protected:
  std::string   text;
  WordCountsMap expected;
};

TEST_F(TestWordCounts, EmptyText) {
    const auto actual = wordCounts(text);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

TEST_F(TestWordCounts, TextWithUniqWords) {
    text = "a b c";
    expected = {{"a", 1}, {"b", 1}, {"c", 1}};

    const auto actual = wordCounts(text);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

TEST_F(TestWordCounts, TextWithExtraSymbols) {
    text = " a, 1b c?";
    expected = {{"a", 1}, {"b", 1}, {"c", 1}};

    const auto actual = wordCounts(text);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

TEST_F(TestWordCounts, TextWithDuplicatedWords) {
    text = "Ab ab aB AB";
    expected = {{"ab", 4}};

    const auto actual = wordCounts(text);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

class TestSortByValuesAndKeys : public ::testing::Test {
protected:
  WordCountsMap    collection;
  bool             reverse;
  WordCountsVector expected;
};

TEST_F(TestSortByValuesAndKeys, EmptyCollection) {
    const auto actual = sortByValuesAndKeys(collection);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

TEST_F(TestSortByValuesAndKeys, CollectionAscendingWithUniqValues) {
    collection = {{"a", 1}, {"b", 3}, {"c", 2}};
    expected = {{1, "a"}, {2, "c"}, {3, "b"}};

    const auto actual = sortByValuesAndKeys(collection, false);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

TEST_F(TestSortByValuesAndKeys, CollectionDescendingWithUniqValues) {
    collection = {{"a", 1}, {"b", 3}, {"c", 2}};
    expected = {{3, "b"}, {2, "c"}, {1, "a"}};

    const auto actual = sortByValuesAndKeys(collection, true);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

TEST_F(TestSortByValuesAndKeys, CollectionAscendingWithEqualValues) {
    collection = {{"b", 0}, {"c", 0}, {"a", 0}};
    expected = {{0, "a"}, {0, "b"}, {0, "c"}};

    const auto actual = sortByValuesAndKeys(collection, false);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

TEST_F(TestSortByValuesAndKeys, CollectionDescendingWithEqualValues) {
    collection = {{"a", 0}, {"c", 0}, {"b", 0}};
    expected = {{0, "c"}, {0, "b"}, {0, "a"}};

    const auto actual = sortByValuesAndKeys(collection, true);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

class TestOfIntegration : public ::testing::Test {
protected:
  std::string      text;
  WordCountsVector expected;
};

TEST_F(TestOfIntegration, Example) {
    text = "To be, or not to be?";
    expected = {{2, "to"}, {2, "be"}, {1, "or"}, {1, "not"}};

    const auto collection = wordCounts(text);
    const auto actual = sortByValuesAndKeys(collection, true);

    EXPECT_THAT(actual, ::testing::ContainerEq(expected));
}

} // namespace quickstart
