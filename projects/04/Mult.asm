// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.


@R2
M = 0		//cleaning R2 before start mult.

@R0
D = M

@END
D;JLE		// R0 <= 0 -> end


@R1
D = M 		//setting D = R1 to use it in i register

@i
MD = D 		//setting i=R1 to do regressive counting

@END
D;JLE		// R1 <= 0 -> end


@LOOP
0;JMP 		// go to loop if R1, R0 != 0

// loop
// R2 = R2 + R1
// i  = i  - 1
// if(i>0) -> loop

(LOOP)

	@R0
	D = M		// D = R0
	@R2
	M = D+M 	// R2 = R2 + R0

	@i
	MD = M-1   	// we have to repeat i-1 times now


	@LOOP
	D;JGT		// if i>0, loop again

	@END
	D;JEQ 		// if i=0, end

(END)
	
	@END
	0;JMP		// jump to END continuously
				// these avoid attacks
