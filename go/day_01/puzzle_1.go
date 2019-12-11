package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func check(err error, msg string) {
	if err != nil {
		panic(fmt.Sprintf("%s: %s", msg, err))
	}
}

func readIntsFromFile(path string) []int {

	f, err := os.Open(path)
	check(err, fmt.Sprintf("Problem opening file %s", path))
	defer f.Close()

	var data []int

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {

		s := scanner.Text()
		i, err := strconv.Atoi(s)
		check(err, "Problem converting string to int")

		data = append(data, i)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

	return data

}

func calcRequiredFuel(mass int) int {
	return int(math.Floor(float64(mass)/3)) - 2
}

func main() {

	data := readIntsFromFile("input.txt")
	totalFuel := 0

	for _, mass := range data {
		fuel := calcRequiredFuel(mass)
		totalFuel += fuel
	}

	fmt.Printf("total fuel: %v\n", totalFuel)

}
