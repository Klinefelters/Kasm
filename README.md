- 16 bit instructions
- R = one of the 8 registers
- Imm = 8 bit immediate value
- [] indicates that the value inside, or register's value, is being used as an address

### NOOP [000] 0000 000 000 000

### MATH [001] XXXX Rd Ra Rb

Perform Ra OP Rb store in Rd
OPS

- ADD   [0000];
- SUB   [0001];
- MUL   [0010];
- DIV   [0011]; 
- REM   [0100]; 
- SLL   [0101];
- SLR   [0110];
- SAR   [0111];
- AND   [1000];
- NAND  [1001];
- ORR   [1010];
- NOR   [1011];
- XOR   [1100];
- XNOR  [1101];
- NMOV  [1110];
- MOV   [1111];


### LOAD [010] 0000 Rd [Ra] 000

Load value stored in address [Ra] to Rd

### LOADI [011] 0 X Imm Rb

- 0 load imm into Rb as the low byte with high byte set to 0's
- 1 load imm into Rb as the high byte with the low byte set to 0's

### STORE [100] 0000 000 [Ra] Rb

Store value Rb into address [Ra]

### JMPIF [101] XXX 0 000 000 Rb

Uses status of the last MATH command to branch. These comparisons are made on Ra and Rb of the previous MATH command, not on the resulting Rd.

- GRT   [000]; jump if a was greater than b
- EQL   [001]; jump if a was equal to b
- LST   [010]; jump if a was less than b
- UGT   [011]; jump if unsigned a was greater than unsigned b
- UEQ   [100]; jump if unsigned a was equal to unsigned b
- ULT   [101]; jump if unsigned a was less than unsigned b
- NOOP  [110]; never jump
- JMP   [111]; always jump

### RIO [110] 00 Rd 000 [Rb]
Read the value from IO device [Rb] and store it in Rb

### WIO [110] 01 000 Ra [Rb]
Write the value stored in Ra to IO device [Rb]

### WIOI [110] 1X Imm [Rb]
- 0 Write imm to IO device [Rb] as the low byte with high byte set to 0's
- 1 Write imm to IO device [Rb] as the high byte with low byte set to 0's

### HALT [111]
Stops the CPU clock