package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)


func remove_paper_rolls(input map[complex128]string) (int, map[complex128]string) {
	res := 0
	steps := [8]complex128{1+0i, 1+1i, 0+1i, -1+1i, -1+0i, -1-1i, 0-1i, 1-1i}
	step_count := 0
	var to_be_removed []complex128

	for key, val := range input {
		if val != "." {
			step_count = 0
			for _, step := range steps {
				neighbor, ok := input[key+step]
				if ok && neighbor != "." {
					step_count++
				}
			}
			if step_count < 4 {
				res++
				to_be_removed = append(to_be_removed, key)
			}
		}
	}

	for _, key := range to_be_removed {
		input[key] = "."
	}

	return res, input
}

func parse(data string) map[complex128]string {
	res := make(map[complex128]string)
	
	lines := strings.Split(data, "\n")
	for y, line := range lines {
		for x, c := range line {
			res[complex(float64(x), float64(y))] = string(c)
		}
	}
	return res
}

func part1(data string) int {
	input := parse(data)
	res, _ := remove_paper_rolls(input)
	return res
}

func part2(data string) int {
	input := parse(data)
	res := 0
	inner_res := 0
	count := 0

	for {
		for y := range 138 {
			for x := range 138 {
				fmt.Print(input[complex(float64(x), float64(y))])
			}
			fmt.Println()
		}
		fmt.Println(count)
		inner_res, input = remove_paper_rolls(input)
		count++
		res += inner_res


		if inner_res == 0 {
			break
		}
	}

	return res
}

func main() {
	data, err := os.ReadFile("input/day04.txt")
	if err != nil {
		log.Fatal(err)
	}

// 	data := `..@@.@@@@.
// @@@.@.@.@@
// @@@@@.@.@@
// @.@@@@..@.
// @@.@@@@.@@
// .@@@@@@@.@
// .@.@.@.@@@
// @.@@@.@@@@
// .@@@@@@@@.
// @.@.@@@.@.`

    fmt.Println("Day 4, Part 2:", part1(string(data)))
    fmt.Println("Day 4, Part 2:", part2(string(data)))
}
