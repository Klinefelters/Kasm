##NOOP: Instruction: `NOOP`
Performs no operation. Used as a placeholder.

##LOAD: Instruction: `LOAD, R1, R2`
Loads the value from the memory address in R2 into R1.

##LOADIL: Instruction: `LOADIL, imm, Rb`
Loads an immediate value (`imm`) into the register `Rb` as the low byte.

##LOADIL: Instruction: `LOADIH, imm, Rb`
Loads an immediate value (`imm`) into the register `Rb` as the high byte.

##STORE: Instruction: `STORE, Ra, Rb`
Stores the value from register `Ra` into the memory address specified by `Rb`.

##RIO: Instruction: `RIO, Rd, Db`
Reads input from device `Db` and stores it in register `Rd`.

##WIO: Instruction: `WIO, Ra, Db`
Writes the value from register `Ra` to device `Db`.

##WIOIL: Instruction: `WIOIL, imm, Db`
Writes an immediate value (`imm`) to device `Db` as the low byte.

##WIOIH: Instruction: `WIOIH, imm, Db`
Writes an immediate value (`imm`) to device `Db` as the low byte.

##HALT: Instruction: `HALT`
Stops the execution of the program.