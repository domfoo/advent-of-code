package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"strconv"
	"sort"
)

type Interval struct {
	Start int
	End int
}

func NewInterval(s string) Interval {
	tmp := strings.Split(s, "-")
	a, _ := strconv.Atoi(tmp[0])
	b, _ := strconv.Atoi(tmp[1])
	return Interval{a, b}
}

func (iv *Interval) Contains(num int) bool {
	return iv.Start <= num && num <= iv.End
}

func (iv *Interval) Size() int {
	return iv.End - iv.Start + 1
}

// {3 5} {10 14} {12 18} {16 20}
// {3 5} {10 18} 
// 3 5 10 14 12 18 16 20
// {3 5} {10 20}
func MyMergeIntervals(intervals []Interval) []Interval {
	merged := []Interval{intervals[0]}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})

	// fmt.Println("Sorted Intervals", intervals)

	i := 0
	j := 1
	for j < len(intervals) {
		a := merged[i]
		b := intervals[j]
		// fmt.Print("Merged Intervals ", merged, i, j, a, b)
		if a.End < b.Start { // []{}
			merged = append(merged, b)
			i = j
			j++
		} else if a.End >= b.Start && a.Start < b.End { // [{]}
			merged = append(merged, Interval{a.Start, b.End})
			j++
		} else { // [{}]
			merged = append(merged, a)
		}
		//  fmt.Println(" =>", merged)
	}
	return merged
}

// corrected version by ChatGPT
func MergeIntervals(intervals []Interval) []Interval {
	if len(intervals) == 0 {
		return nil
	}

	// sort by Start
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})

	merged := []Interval{intervals[0]}

	for _, curr := range intervals[1:] {
		last := &merged[len(merged)-1]

		if curr.Start <= last.End { // overlap
			if curr.End > last.End {
				last.End = curr.End
			}
		} else { // no overlap
			merged = append(merged, curr)
		}
	}

	return merged
}

func parse(data string) ([]Interval, []int) {
	parts := strings.Split(data, "\n\n")
	
	intervals_str := strings.Split(parts[0], "\n")
	intervals := make([]Interval, len(intervals_str))
	for i, s := range intervals_str {
		intervals[i] = NewInterval(s)
	}
	
	ids_str := strings.Split(parts[1], "\n")
	ids := make([]int, len(ids_str))
	for i, s := range ids_str {
		ids[i], _ = strconv.Atoi(s)
	}

	return intervals, ids
}

func part1(data string) int {
	res := 0

	intervals, ids := parse(data)
	for _, id := range ids {
		for _, interval := range intervals {
			if interval.Contains(id) {
				res++
				break
			}
		}
	}

	return res
}

func part2(data string) int {
	res := 0
	intervals, _ := parse(data)
	for _, interval := range MergeIntervals(intervals) {
		res += interval.Size()
	}
	return res
}

func main() {
	data, err := os.ReadFile("input/day05.txt")
	if err != nil {
		log.Fatal(err)
	}

// 	data := `3-5
// 10-14
// 16-20
// 12-18

// 1
// 5
// 8
// 11
// 17
// 32`

    fmt.Println("Day 5, Part 1:", part1(string(data)))
    fmt.Println("Day 5, Part 2:", part2(string(data)))
}
