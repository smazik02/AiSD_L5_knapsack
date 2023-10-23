package main

import (
	"fmt"
	"math"
	"math/rand"
	"strconv"
	"time"
)

func genItems(n int) [][]int {
	rand.Seed(time.Now().UnixNano())
	items := make([][]int, n)
	for i := range items {
		items[i] = make([]int, 3)
		items[i][0] = i + 1
		items[i][1] = rand.Intn(10) + 1
		items[i][2] = rand.Intn(10) + 1
	}
	return items
}

func getRatio(list []int) int {
	return list[2] / list[1]
}

func replaceAtIndex(in string, r rune, i int) string {
	out := []rune(in)
	out[i] = r
	return string(out)
}

func bruteForce(items [][]int, cap int) {
	elems := len(items)
	max := 0
	solution := "Brak rozwiazania"
	for i := 1; i <= int(math.Pow(2, float64(elems))); i++ {
		knapsack := strconv.FormatInt(int64(elems), 2)
		massSum := 0
		for j := 1; j <= int(math.Pow(2, float64(elems))); j = j << 1 {

		}
	}
}

func main() {
	fmt.Println(genItems(5))
}
