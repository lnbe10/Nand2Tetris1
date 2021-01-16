# this script opens an assembly-hack .asm and
# make a .txt with clean commands 

lines = open('Max.asm', 'r').read().split('\n');

commands = [];

for i in range(len(lines)):

	no_comments = lines[i].split('//')[0];
	clean1      = no_comments.replace(' ', '');
	clean2      = clean1.replace('\t', '');
	commands.append(clean2);


commands[:] = [x for x in commands if x];

f = open('MaxAssembly.txt', 'w');

for i in range(len(commands)):
	f.write(commands[i] + '\n');

f.close();

compute={
			'0'		:'0101010',
			'1'		:'0111111',
			'-1'	:'0111010',
			'D'		:'0001100',
			'A'		:'0110000',
			'M'		:'1110000',
			'!D'	:'0001101',
			'!A'	:'0110001',
			'!M'	:'1110001',
			'-D'	:'0001111',
			'-A'	:'0110011',
			'-M'	:'1110011',
			'D+1'	:'0011111',
			'A+1'	:'0110111',
			'M+1'	:'1110111',
			'D-1'	:'0001110',
			'A-1'	:'0110010',
			'M-1'	:'1110010',
			'D+A'	:'0000010',
			'D+M'	:'1000010',
			'D-A'	:'0010011',
			'D-M'	:'1010011',
			'A-D'	:'0000111',
			'M-D'	:'1000111',
			'D&A'	:'0000000',
			'D&M'	:'1000000',
			'D|A'	:'0010101',
			'D|M'	:'1010101',
			};
destin={ 	
		'null'	:'000',
		'M'		:'001',
		'D'		:'010',
		'MD'	:'011',
		'A'		:'100',
		'AM'	:'101',
		'AD'	:'110',
		'AMD'	:'111',
		};
jump={
		'null'	:'000',
		'JGT'	:'001',
		'JEQ'	:'010',
		'JGE'	:'011',
		'JLT'	:'100',
		'JNE'	:'101',
		'JLE'	:'110',
		'JMP'	:'111',
		};
 
print(commands);

for i in range(len(commands)):
	c = commands[i];

	# A instruction no symbolic 
	if c[0] == '@' and c[1:].isnumeric():
		commands[i] = '0' + '{0:015b}'.format(int(c[1:]));

	# C instruction
	if c[0] == 'A' or c[0] == 'M' or c[0] == 'D' or c[0] == 'n' or c[0] == '0':
		if '=' in c:
			dest, comp_jmp = c.split('=');
			
			if ';' in comp_jmp: #dest and jump
				comp, jmp   = comp_jmp.split(';');
				commands[i] = '111' + compute[comp] + destin[dest] + jump[jmp];

			else: #no jump
				commands[i] = '111' + compute[comp_jmp] + destin[dest] + '000';


		else: #if there's no '=', it's a jump expression, like "M;JMP"	
			comp, jmp  = c.split(';');
			commands[i] = '111'+ compute[comp] + '000' + jump[jmp];







	if c[0] == '(':
		commands[i] = c.replace('(','').replace(')','');
		#(loop) -> loop
		#we have to save loop's address
		#somewhere now...


print(commands)


fas = open('MaxBin.txt', 'w');

for i in range(len(commands)):

	fas.write(commands[i] + '\n');

fas.close();