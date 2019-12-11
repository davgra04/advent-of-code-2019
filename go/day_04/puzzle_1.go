package main

import (
	"fmt"
	"strconv"
)

// Utility Functions
////////////////////////////////////////////////////////////////////////////////

func check(err error, msg string) {
	if err != nil {
		panic(fmt.Sprintf("%s: %s", msg, err))
	}
}

// Main
////////////////////////////////////////////////////////////////////////////////

func main() {

	rangeStart, rangeEnd := 254032, 789860
	validCount := 0

	// iterate through range
	for i := rangeStart; i < rangeEnd; i++ {

		hasDoubleDigits := false
		hasIncreasingDigits := true
		prevDigit := 0

		// iterate over digits
		for idx, digitStr := range strconv.Itoa(i) {
			digit, _ := strconv.Atoi(string(digitStr))

			// skip first digit
			if idx == 0 {
				prevDigit = digit
				continue
			}

			// test double digits
			if digit == prevDigit {
				hasDoubleDigits = true
			}

			// test increasing digits
			if digit < prevDigit {
				hasIncreasingDigits = false
			}

			prevDigit = digit
		}

		// increment if valid password
		if hasDoubleDigits && hasIncreasingDigits {
			validCount++
		}

	}

	fmt.Printf("Found %v valid passwords.\n", validCount)

}
