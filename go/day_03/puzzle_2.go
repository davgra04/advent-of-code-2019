package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

// Utility Functions
////////////////////////////////////////////////////////////////////////////////

func check(err error, msg string) {
	if err != nil {
		panic(fmt.Sprintf("%s: %s", msg, err))
	}
}

func readWiresFromFile(path string) ([]string, []string) {

	// read file
	buf, err := ioutil.ReadFile(path)
	check(err, fmt.Sprintf("Problem opening file %s", path))
	// fmt.Printf("buf [%T]: %v\n", buf, buf)

	s := string(buf)
	// fmt.Printf("s [%T]: %v\n", s, s)

	wireStrings := strings.Split(s, "\n")
	// fmt.Printf("wireStrings [%T]: %v\n", wireStrings, wireStrings)
	// fmt.Printf("wireStrings[0] [%T]: %v\n", wireStrings[0], wireStrings[0])
	// fmt.Printf("wireStrings[1] [%T]: %v\n", wireStrings[1], wireStrings[1])

	wire1 := strings.Split(wireStrings[0], ",")
	wire2 := strings.Split(wireStrings[1], ",")

	return wire1, wire2

}

func coordStringToInt(coord string) (int, int) {
	stringSlice := strings.Split(coord, ",")
	x, _ := strconv.Atoi(stringSlice[0])
	y, _ := strconv.Atoi(stringSlice[1])

	return x, y
}

func coordIntToString(x, y int) string {
	return fmt.Sprintf("%v,%v", x, y)
}

func calcManhattanDistance(coord1, coord2 string) int {
	c1X, c1Y := coordStringToInt(coord1)
	c2X, c2Y := coordStringToInt(coord2)

	return int(math.Abs(float64(c1X-c2X)) + math.Abs(float64(c1Y-c2Y)))
}

func getCoordMap(wire []string) map[string]int {

	curX, curY, incr, length := 0, 0, 0, 0
	var curDim *int
	direction := ""
	coordLabel := ""
	m := make(map[string]int)
	cost := 0

	for _, wireSegment := range wire {

		// parse wireSegment
		// fmt.Printf("wireSegment:%v curX:%v curY:%v incr:%v\n", wireSegment, curX, curY, incr)
		direction = string(wireSegment[0])
		length, _ = strconv.Atoi(wireSegment[1:])
		// fmt.Printf("direction:%v length:%v\n", direction, length)

		// set currently active dimension and increment value
		switch direction {
		case "U":
			curDim = &curY
			incr = 1
			break
		case "D":
			curDim = &curY
			incr = -1
			break
		case "L":
			curDim = &curX
			incr = -1
			break
		case "R":
			curDim = &curX
			incr = 1
			break
		}

		// add wireSegment data to the map
		for i := 0; i < length; i++ {
			// increment in active dimension
			*curDim += incr
			cost++

			// add to map
			coordLabel = coordIntToString(curX, curY)
			m[coordLabel] = cost

		}

	}

	return m

}

// Main
////////////////////////////////////////////////////////////////////////////////

func main() {

	// read wire data from file
	wire1, wire2 := readWiresFromFile("input.txt")
	// fmt.Printf("wire1 [%T]: %v\n", wire1, wire1)
	// fmt.Printf("wire2 [%T]: %v\n", wire2, wire2)

	// build map of wire1 coordinates
	wire1Coords := getCoordMap(wire1)
	// fmt.Printf("wire1Coords [%T]: %v\n", wire1Coords, wire1Coords)

	// build map of wire2 coordinates
	wire2Coords := getCoordMap(wire2)
	// fmt.Printf("wire2Coords [%T]: %v\n", wire2Coords, wire2Coords)

	// find intersection closest to center
	lowestCostIntersection := "0,0"
	lowestCost := math.MaxUint32

	for coord := range wire1Coords {

		if _, ok := wire2Coords[coord]; ok {
			// found intersection, check cost
			c := wire1Coords[coord] + wire2Coords[coord]
			if c < lowestCost {
				lowestCostIntersection = coord
				lowestCost = c
			}
		}

	}

	fmt.Printf("Lowest cost intersection at (%v) with cost %v\n", lowestCostIntersection, lowestCost)
}
