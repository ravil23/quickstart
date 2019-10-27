#include <algorithm>
#include <functional>
#include <iostream>
#include <set>
#include <sstream>
#include <unordered_map>
#include <vector>


using WordCountsMap    = std::unordered_map<std::string, uint>;
using WordCountsPair   = std::pair<std::string, uint>;
using WordCountsVector = std::vector<WordCountsPair>;


const WordCountsMap wordCounts(const std::string& text) {
    WordCountsMap counts;
    std::istringstream ss(text);
    do {
        std::string buffer;
        ss >> buffer;
        std::string word;
        std::transform(
             buffer.cbegin(),
             buffer.cend(),
             std::back_inserter(word),
             [](char c) {
                 if (std::isalpha(c, std::locale())) {
                     return std::tolower(c, std::locale());
                 }
		 return '\0';
             });
	if (not word.empty()) {
             ++counts[word];
        }
    } while (ss);
    return counts;
}


const WordCountsVector sortByValuesAndKeys(const WordCountsMap& collection, bool reverse = false) {
    WordCountsVector items(collection.cbegin(), collection.cend());
    std::sort(
        items.begin(),
	items.end(),
	[&](const WordCountsPair& left, const WordCountsPair& right) {
	    return (not reverse) xor (
                (left.second > right.second) or (
                    (left.second == right.second) and
                    (left.first > right.first)));
        });
    return items;
}


int main() {
    const std::string text("To be, or not to be?");
    const auto counts = wordCounts(text);
    const auto sorted_items = sortByValuesAndKeys(counts, true);
    std::cout << "Words count in sentence: " << '"' << text << '"' << std::endl;
    for (const auto& item : sorted_items) {
        std::cout << item.first << ' ' << item.second << std::endl;
    }
}
