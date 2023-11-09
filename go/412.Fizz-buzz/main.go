package main

import (
	"flag"
	"fmt"
	"strconv"
	"time"
)

var n = flag.Int("n", 5, "Number of elements in input array for fizzbuzz(): n = 3, nums = [1, 2, 3]")
var iter = flag.Int("iter", 1, "A number of iterations to measure mean execution time")

func simple_fizzbuzz(n int) []string {
	nums_str := make([]string, n)

	for i := 1; i <= n; i++ {
		div_by_3 := (i%3 == 0)
		div_by_5 := (i%5 == 0)

		switch {
		case div_by_3 && div_by_5:
			nums_str[i-1] = "FizzBuzz"
			break
		case div_by_3:
			nums_str[i-1] = "Fizz"
			break
		case div_by_5:
			nums_str[i-1] = "Buzz"
			break
		default:
			nums_str[i-1] = strconv.Itoa(i)
		}
	}

	return nums_str
}

func main() {
	flag.Parse()

	start := time.Now()
	nums := []string{}

	for i := 0; i < *iter; i++ {
		nums = simple_fizzbuzz(*n)
	}

	total := time.Since(start)

	fmt.Printf("n: %v ret: %v\n", *n, nums)
	fmt.Printf("Time: %.2f us\n", float64(total.Microseconds())/float64(*iter))
}
