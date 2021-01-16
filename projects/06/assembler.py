# this is a cross compiler, that transforms
# human hack assembly language in hack binary language

# loading and cleaning lines of original assembly
from dict import *


file  = 'Pong';



lines = open(file+'.asm', 'r').read().split('\n');

# this list will track the commands in sequence
commands = [];

for i in range(len(lines)):
	no_comments = lines[i].split('//')[0];
	clean1      = no_comments.replace(' ', '');
	clean2      = clean1.replace('\t', '');
	commands.append(clean2);

commands[:] = [x for x in commands if x];


# saving clean commands in .txt file
As = open('Assembly_Clean.txt', 'w');
for i in range(len(commands)):
	As.write(commands[i] + '\n');
As.close();


#tables of C instruction


# creating a binary list, that is
# equivalent to commands, but in binary

binlist = commands;

symbolspar ={};

lin_counter = 0;
for i in range(len(binlist)):
	
	c = binlist[i];

	
	if c[0] == '@':
		if c[1:].isnumeric(): # A instruction no symbolic 
				binlist[i] = '0' + '{0:015b}'.format(int(c[1:]));

		if not(c[1:].isnumeric()) and c[1:] in address: # A symbolic in dict
				binlist[i] = '0' + '{0:015b}'.format(address[c[1:]]); 
	
		lin_counter += 1;

	# C instruction
	if c[0] == 'A' or c[0] == 'M' or c[0] == 'D' or c[0] == 'n' or c[0] == '0':
		if '=' in c:
			dest, comp_jmp = c.split('=');
			
			if ';' in comp_jmp: #dest and jump
				comp, jmp   = comp_jmp.split(';');
				binlist[i] = '111' + compute[comp] + destin[dest] + jump[jmp];

			else: #no jump
				binlist[i] = '111' + compute[comp_jmp] + destin[dest] + '000';


		else: #if there's no '=', it's a jump expression, like "M;JMP"	
			comp, jmp  = c.split(';');
			binlist[i] = '111'+ compute[comp] + '000' + jump[jmp];

		lin_counter += 1;



	if c[0] == '(': #attatching the (symbol) to the number of next valid code line
		
		binlist[i] = c.replace('(','').replace(')','');
		symbolspar[binlist[i]] = lin_counter;



# second pass, substituting @symbol for the right address of code line

symbol_address = {};
reg = 16;

for i in range(len(binlist)):
	c = binlist[i];
	if c[0] == '@' and c[1:] in symbolspar:
		binlist[i] = '0' + '{0:015b}'.format(symbolspar[c[1:]]);
	if c[0] == '@' and (c[1:] not in symbolspar):
		if c[1:] in symbol_address: # @symbol used before, just check address and use
			binlist[i] = '0' + '{0:015b}'.format(symbol_address[c[1:]]);
		if c[1:] not in symbol_address: # @symbol first used, assign in dictionary and give address
			symbol_address[c[1:]] = reg;
			binlist[i] = '0' + '{0:015b}'.format(reg);
			reg += 1;




s_p = open('SecondPass.txt', 'w');
for i in range(len(binlist)):
	s_p.write(binlist[i] + '\n');
s_p.close();







#removing the symbols remaining in binary
final_bin = [];
for i in range(len(binlist)):
	if binlist[i].isnumeric():
		final_bin.append(binlist[i]);


# saving binary version in .txt
# now the symbols still unassigned
f_bin = open(file+'.hack', 'w');
for i in range(len(final_bin)):
	f_bin.write(final_bin[i] + '\n');
f_bin.close();