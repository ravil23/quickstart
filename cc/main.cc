#include "wc.h"

#include <iostream>


int main() {
    const std::string text("To be, or not to be?");
    const auto counts = quickstart::wordCounts(text);
    const auto sorted_items = quickstart::sortByValuesAndKeys(counts, true);
    std::cout << "Words count in sentence: " << '"' << text << '"' << std::endl;
    for (const auto& item : sorted_items) {
        std::cout << item.first << ' ' << item.second << std::endl;
    }
}
