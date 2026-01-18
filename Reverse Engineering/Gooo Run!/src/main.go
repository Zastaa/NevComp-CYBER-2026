package main

import (
	"bufio"
	"fmt"
	"os"
)

func rol1(x byte) byte {
	return (x << 1) | (x >> 7)
}

func xorshift32(s uint32) uint32 {
	s ^= s << 13
	s ^= s >> 17
	s ^= s << 5
	return s
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter PIN (8 digits): ")

	var pin string
	fmt.Fscanln(reader, &pin)

	if len(pin) != 8 {
		fmt.Println("nope")
		return
	}

	// Pastikan digit semua
	digits := make([]byte, 8)
	for i := 0; i < 8; i++ {
		c := pin[i]
		if c < '0' || c > '9' {
			fmt.Println("nope")
			return
		}
		digits[i] = c - '0'
	}

	key1 := []byte{0xA3, 0x5C, 0x1F, 0xD2, 0x77, 0x09, 0xBE, 0x48}
	key2 := []byte{0x19, 0xE4, 0x55, 0x2B, 0xC0, 0x7A, 0x13, 0x9D}
	target := []byte{127, 116, 214, 215, 114, 1, 129, 229}

	ok := true
	comp := make([]byte, 8)
	for i := 0; i < 8; i++ {
		t := byte((int(digits[i]) + 3*i) & 0xFF)
		t ^= key1[i]
		t = byte((int(t) + int(key2[i])) & 0xFF)
		t = rol1(t)
		comp[i] = t
		if t != target[i] {
			ok = false
		}
	}

	if !ok {
		fmt.Println("nope")
		return
	}

	var seed uint32 = 0
	for i := 0; i < 8; i++ {
		seed = (seed*131 + uint32(comp[i])) & 0xFFFFFFFF
	}

	cipher := []byte{
		0x4C, 0xBE, 0xE7, 0xAF, 0x8C, 0xC4, 0x59, 0xC3,
		0x40, 0x45, 0xA5, 0x4B, 0xB5, 0xAF, 0x2E, 0xD8,
		0xE2, 0x60, 0x9E, 0x00, 0xCC, 0xC7, 0x02, 0xE7,
		0x5C, 0x82, 0xA1, 0x58, 0xBD, 0x0C, 0x89,
	}

	plain := make([]byte, len(cipher))
	s := seed
	for i := 0; i < len(cipher); i++ {
		s = xorshift32(s)
		k := byte(s & 0xFF)
		plain[i] = cipher[i] ^ k
	}

	fmt.Println(string(plain))
}
