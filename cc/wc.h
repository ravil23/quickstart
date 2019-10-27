#include <unordered_map>
#include <vector>


namespace quickstart {

using WordCountsMap    = std::unordered_map<std::string, unsigned int>;
using WordCountsVector = std::vector<std::pair<unsigned int, std::string>>;

const WordCountsMap wordCounts(const std::string& text);

const WordCountsVector sortByValuesAndKeys(const WordCountsMap& collection, bool reverse = false);

} // namespace quickstart
