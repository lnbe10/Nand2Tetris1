// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


//KBD refers to RAM[24576], in wich the last digit is stored
// if no digit was pressed, its = 0.


// SCREEN refers to RAM[16384] = 16bits
// a pixel is located in RAM[16384 + 32 * row + col / 16]
//  and is the col % 16 th bit... a %b (remainder of a/b)
// 256px x 512px


(START)


	@KBD
	D = M

	@BLACK
	D;JGT

	@WHITE
	D;JMP

(BLACK)

	@color
	M = -1

	@DRAW
	0;JMP

(WHITE)

	@color
	M = 0

	@DRAW
	0;JMP

(DRAW)

	@8191
	D = A
	@i
	M = D 	//setting i = max

	(NEXT)

		@i
		D = M

		@pos
		M = D

		@SCREEN
		D = A

		@pos
		M = M + D 	// pos = screen + i



		@color
		D = M 		// D = color
		@pos
		A = M 		// Address to paint
		M = D 		// Painted the Address



		@i
		MD = M-1

		@NEXT
		D;JGE 		// if i>=0 -> draw next

	@START
	0;JMP		// if i=0 -> start again