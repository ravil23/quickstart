#include "wc.h"

#include <algorithm>
#include <functional>
#include <sstream>


namespace quickstart {

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
             [](const auto& symbol) {
                 if (std::isalpha(symbol, std::locale())) {
                     return std::tolower(symbol, std::locale());
                 }
		 return '\0';
             });
	if (not word.empty()) {
             ++counts[word];
        }
    } while (ss);
    return std::move(counts);
}


const WordCountsVector sortByValuesAndKeys(const WordCountsMap& collection, bool reverse) {
    WordCountsVector items;
    items.reserve(collection.size());
    std::transform(
        collection.cbegin(),
        collection.cend(),
        std::back_inserter(items),
        [](const auto& pair) { return std::make_pair(pair.second, pair.first); });
    if (reverse) {
        std::sort(items.begin(), items.end(), std::greater<>());
    } else {
        std::sort(items.begin(), items.end(), std::less<>());
    }
    return std::move(items);
}

} // namespace quickstart
