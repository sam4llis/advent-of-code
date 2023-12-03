package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part1(input io.Reader) int {
	rx := regexp.MustCompile(`\d`)

	scanner := bufio.NewScanner(os.Stdin)
	sum := 0

	for scanner.Scan() {
		digits := rx.FindAllString(scanner.Text(), -1)

		firstDigit := digits[0]
		lastDigit := digits[len(digits)-1]

		// Convert from a string to integer, and combine.
		combined, err := strconv.Atoi(firstDigit + lastDigit)
		if err != nil {
			log.Fatal(err)
		}

		sum += combined
	}

	return sum
}

func part2(input io.Reader) int {
	rx := regexp.MustCompile(`\d`)
	r := strings.NewReplacer(
		"zero", "z0o",
		"one", "o1e",
		"two", "t2o",
		"three", "t3e",
		"four", "f4r",
		"five", "f5e",
		"six", "s6x",
		"seven", "s7n",
		"eight", "e8t",
		"nine", "n9e",
	)

	scanner := bufio.NewScanner(os.Stdin)
	sum := 0

	for scanner.Scan() {
		line := r.Replace(scanner.Text())
		line = r.Replace(line)

		digits := rx.FindAllString(line, -1)

		firstDigit := digits[0]
		lastDigit := digits[len(digits)-1]

		// Convert from a string to an integer, and combine.
		combined, err := strconv.Atoi(firstDigit + lastDigit)
		if err != nil {
			log.Fatal(err)
		}

		sum += combined
	}

	return sum
}

func main() {
	fmt.Println(part1(os.Stdin))
	// fmt.Println(part2(os.Stdin))
}
