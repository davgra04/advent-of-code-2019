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

func getDigit(num, idx int) int {

	numString := strconv.Itoa(num)

	if idx < 0 || idx >= len(numString) {
		fmt.Printf("num:%v idx:%v numDigits:%v\n", num, idx, len(numString))
		panic("ERROR GETTING DIGIT")
	}

	digitString := numString[idx]

	digit, _ := strconv.Atoi(string(digitString))

	return digit

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

		// iterate over digits
		iString := strconv.Itoa(i)
		for idx := range iString {
			digit := getDigit(i, idx)

			// skip first digit
			if idx == 0 {
				continue
			}

			// test double digits
			if digit == getDigit(i, idx-1) && !hasDoubleDigits {

				// // ensure group is no larger than 2 digits
				if idx > 1 && getDigit(i, idx-2) == digit {
					hasDoubleDigits = false
				} else if idx < len(iString)-1 && getDigit(i, idx+1) == digit {
					hasDoubleDigits = false
				} else {
					hasDoubleDigits = true
				}

			}

			// test increasing digits
			if digit < getDigit(i, idx-1) {
				hasIncreasingDigits = false
			}

		}

		// increment if valid password
		if hasDoubleDigits && hasIncreasingDigits {
			validCount++
		}

	}

	fmt.Printf("Found %v valid passwords.\n", validCount)

}
