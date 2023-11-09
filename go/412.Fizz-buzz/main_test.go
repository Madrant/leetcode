package main

import "testing"

func compareStringArrays(s1 []string, s2 []string) bool {
	if len(s1) != len(s2) {
		return false
	}

	for i := range s1 {
		if s1[i] != s2[i] {
			return false
		}
	}

	return true
}

func checkTestResult(t *testing.T, answer []string, ret []string) {
	if compareStringArrays(answer, ret) != true {
		t.Errorf("n: %v answer: %v ret: %v\n", n, answer, ret)
	}
}

func Test1(t *testing.T) {
	n := 3
	answer := []string{"1", "2", "Fizz"}

	ret := simple_fizzbuzz(n)

	checkTestResult(t, answer, ret)
}

func Test2(t *testing.T) {
	n := 5
	answer := []string{"1", "2", "Fizz", "4", "Buzz"}

	ret := simple_fizzbuzz(n)

	checkTestResult(t, answer, ret)
}

func Test3(t *testing.T) {
	n := 15
	answer := []string{"1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"}

	ret := simple_fizzbuzz(n)

	checkTestResult(t, answer, ret)
}

func Test4(t *testing.T) {
	n := 0
	answer := []string{}

	ret := simple_fizzbuzz(n)

	checkTestResult(t, answer, ret)
}
