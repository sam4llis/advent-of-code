package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

type Game struct {
	id      int
	colours []map[string]int
}

func parseLine(line string) Game {
	split := strings.Split(line, ": ")

	gameId, err := strconv.Atoi(strings.Split(split[0], " ")[1])
	if err != nil {
		log.Fatal(err)
	}

	colours := make([]map[string]int, 0)
	for _, subset := range strings.Split(split[1], "; ") {
		cubes := make(map[string]int)
		for _, cube := range strings.Split(subset, ", ") {
			item := strings.Split(cube, " ")
			colour := item[1]

			amount, err := strconv.Atoi(item[0])
			if err != nil {
				log.Fatal(err)
			}

			cubes[colour] = amount
		}
		colours = append(colours, cubes)
	}

	return Game{id: gameId, colours: colours}
}

func isSubsetPossible(given map[string]int, bag map[string]int) bool {
	for colour, amount := range given {
		if amount > bag[colour] {
			log.Println(fmt.Sprintf("Expected %s to be less than %d but got %d", colour, bag[colour], amount))
			return false
		}
	}
	return true
}

func calculatePower(colours []map[string]int) int {
	maxColour := make(map[string]int)

	for _, subset := range colours {
		for colour, amount := range subset {
			maxAmount, ok := maxColour[colour]
			if !ok || ok && maxAmount < amount {
				maxColour[colour] = amount
			}
		}
	}

	power := 1
	for _, amount := range maxColour {
		power *= amount
	}

	return power
}

func part1(input io.Reader, bag map[string]int) int {
	sum := 0
	scanner := bufio.NewScanner(input)
START:
	for scanner.Scan() {
		game := parseLine(scanner.Text())
		log.Println(fmt.Sprintf("Processing game with id %d", game.id))

		for _, colour := range game.colours {
			log.Println(fmt.Sprintf("Processing subset %+v", colour))

			// If a subset in a game isn't possible, don't add to the sum and
			// scan the next line.
			if !isSubsetPossible(colour, bag) {
				continue START
			}
		}
		sum += game.id
	}

	return sum
}

func part2(input io.Reader, bag map[string]int) int {
	sum := 0
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		game := parseLine(scanner.Text())
		log.Println(fmt.Sprintf("Processing game with id %d", game.id))
		sum += calculatePower(game.colours)
	}

	return sum
}

func main() {
	bag := make(map[string]int)
	bag["red"] = 12
	bag["green"] = 13
	bag["blue"] = 14

	// fmt.Println(part1(os.Stdin, bag))
	fmt.Println(part2(os.Stdin, bag))
}
