package main

import (
	"fmt"

	"github.com/ravil23/quickstart/go/wc"
)

func main() {
	text := "To be, or not to be?"
	counts := wc.WordCounts(text)
	orderedCounts := wc.SortByValuesAndKeys(counts, true)
	for _, elem := range orderedCounts {
		fmt.Println(elem.Count, elem.Word)
	}
}
