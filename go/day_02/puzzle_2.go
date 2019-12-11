package main

import (
	"fmt"
	"io/ioutil"
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

func readIntcodeFromFile(path string) []int {

	// read file
	buf, err := ioutil.ReadFile(path)
	check(err, fmt.Sprintf("Problem opening file %s", path))

	s := string(buf)
	s = strings.Replace(s, "\n", "", -1) // remove newlines
	dataStrings := strings.Split(s, ",") // split on ,

	// convert strings to ints
	var data []int

	for _, val := range dataStrings {
		i, err := strconv.Atoi(val)
		check(err, "Problem converting string to int")
		data = append(data, i)
	}

	return data

}

// Intcode Computer
////////////////////////////////////////////////////////////////////////////////

// Instructions
////////////////////////////////////////

type instruction interface {
	execute(c *Computer)
	nParams() int
	incrementPC() bool
}

// ADD
////////////////////

type opADD struct{}

func (i opADD) execute(c *Computer) {
	// fmt.Println("executing ADD")
	param1 := c.readFromMemory(c.pc+1, 0)
	param2 := c.readFromMemory(c.pc+2, 0)
	param3 := c.readFromMemory(c.pc+3, 0)

	a := c.readFromMemory(param1, 0)
	b := c.readFromMemory(param2, 0)
	result := a + b
	addr := param3

	// fmt.Printf("  param_1:%v  param_2:%v  param_3:%v\n", param1, param2, param3)
	// fmt.Printf("  a:%v  b:%v  result: %v  addr:%v\n", a, b, result, addr)

	c.writeToMemory(result, addr, 0)
}

func (i opADD) nParams() int {
	return 3
}

func (i opADD) incrementPC() bool {
	return true
}

// MULT
////////////////////

type opMULT struct{}

func (i opMULT) execute(c *Computer) {
	// fmt.Println("executing MULT")
	param1 := c.readFromMemory(c.pc+1, 0)
	param2 := c.readFromMemory(c.pc+2, 0)
	param3 := c.readFromMemory(c.pc+3, 0)

	a := c.readFromMemory(param1, 0)
	b := c.readFromMemory(param2, 0)
	result := a * b
	addr := param3

	// fmt.Printf("  param_1:%v  param_2:%v  param_3:%v\n", param1, param2, param3)
	// fmt.Printf("  a:%v  b:%v  result: %v  addr:%v\n", a, b, result, addr)

	c.writeToMemory(result, addr, 0)
}

func (i opMULT) nParams() int {
	return 3
}

func (i opMULT) incrementPC() bool {
	return true
}

// HALT
////////////////////

type opHALT struct{}

func (i opHALT) execute(c *Computer) {
	// fmt.Println("executing HALT")
	c.halted = true
}

func (i opHALT) nParams() int {
	return 0
}

func (i opHALT) incrementPC() bool {
	return true
}

// Instruction Helpers
////////////////////////////////////////

func getInstruction(opcode int) instruction {
	switch opcode {
	case 1:
		return opADD{}
	case 2:
		return opMULT{}
	case 99:
		return opHALT{}
	default:
		panic(fmt.Sprintf("Opcode not recognized! [%d]", opcode))
	}
}

// Computer
////////////////////////////////////////

// MemorySize represents the size of the memory in the Intcode Computer
var MemorySize int = 10000

// Computer represents the Intcode computer
type Computer struct {
	pc             int
	halted, paused bool
	memory         []int
}

func newComputer() *Computer {
	memory := make([]int, MemorySize)
	return &Computer{pc: 0, halted: false, paused: false, memory: memory}
}

func (c *Computer) reset() {
	c.pc = 0
	c.halted = false
	c.paused = false
	for idx := range c.memory {
		c.memory[idx] = 0
	}
}

func (c *Computer) loadMemory(data []int) {
	if len(data) > MemorySize {
		panic("Cannot load program, not enough Intcode Computer memory!")
	}

	for idx, val := range data {
		c.memory[idx] = val
	}
}

func (c *Computer) printMemory() {
	for idx, val := range c.memory {
		fmt.Printf("%05d: %v\n", idx, val)
	}
}

func (c *Computer) printMemoryRange(l int) {

	if l < 1 {
		return
	}

	for idx, val := range c.memory {
		if idx == l {
			return
		}
		fmt.Printf("%05d: %v\n", idx, val)
	}
}

func (c *Computer) readFromMemory(param, paramMode int) int {

	switch paramMode {
	case 0:
		addr := param
		// fmt.Printf("  read value %v from address %v\n", c.memory[addr], addr)
		return c.memory[addr]
	default:
		panic(fmt.Sprintf("Unrecognized read paramMode! [%v]", paramMode))
	}

}

func (c *Computer) writeToMemory(value, param, paramMode int) {

	switch paramMode {
	case 0:
		addr := param
		// fmt.Printf("  wrote value %v to address %v\n", value, addr)
		c.memory[addr] = value
	default:
		panic(fmt.Sprintf("Unrecognized read paramMode! [%v]", paramMode))
	}

}

func (c *Computer) executeProgram() {

	for !c.halted && !c.paused {
		// parse instruction
		i := getInstruction(c.memory[c.pc])

		// execute instruction
		i.execute(c)

		// increment program counter
		if i.incrementPC() {
			c.pc += i.nParams() + 1
		}
	}

}

// Main
////////////////////////////////////////////////////////////////////////////////

func main() {

	// read program from file and modify
	data := readIntcodeFromFile("input.txt")
	data[1] = 12
	data[2] = 2

	// test all noun/verb combos
	comp := newComputer()
	found := false
	value := 0
	target := 19690720

	for noun := 0; noun < 100 && !found; noun++ {
		for verb := 0; verb < 100 && !found; verb++ {

			data[1] = noun
			data[2] = verb

			comp.reset()
			comp.loadMemory(data)
			comp.executeProgram()
			value = comp.memory[0]

			if value == target {
				fmt.Printf("noun %v and verb %v yields %v\n", noun, verb, value)
				fmt.Printf("answer: %v", noun*100+verb)
				found = true
			}

		}
	}

}
