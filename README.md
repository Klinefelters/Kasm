# Kasm Language

Kasm is a custom assembly-like language designed for low-level programming on a Kasm CPU designed in Logisim Evolution. This repository contains the Kasm compiler, examples, and syntax highlighting support for Visual Studio Code.

---

## Features

- **Sections**: Organize your code into `.vars` (variables) and `.code` (instructions).
- **Instructions**: Includes load/store, branching, math, bitwise, IO, and stack operations.
- **Labels**: Define subroutines and jump points using `@label:` syntax.
- **Syntax Highlighting**: Custom syntax highlighting for Visual Studio Code.

---

## Code Example

```asm
section .vars ; A section for variables
    num: .int 0 ; A variable to store an integer
    msg: .ascii "Hello, World!\n" ; A string variable

section .code ; A section for code

    ; LOAD/STORE instructions
    STR R0, [R1] ; Store the value in R0 into memory address [R1]
    LDR R0, [R1] ; Load a value from memory address [R1] into R0
    LDRL R0, 0xFF ; Load a literal value (0x00FF) R0
    LDRH R0, 0xFF ; Load a literal value (0xFF00) R0
    ...
    HALT ; Halt the program
```
For the full example, see examples/all.kasm.

## Using the Compiler
Compile a Kasm File
To compile a Kasm file, run the following command:
```bash
git clone https://github.com/Klinefelters/Kasm
cd ./Kasm
pip install .
kasm ./path/to/file.kasm
```

This will generate a .hex file in the same directory as the input file.

## Syntax Highlighting
This repository includes a Visual Studio Code extension for Kasm syntax highlighting. To enable it:

Open the syntaxes/kasm.tmLanguage.json file.
Install the extension in Visual Studio Code.
Open any .kasm file to see the syntax highlighting.

## Instructions Overview

### Load/Store Instructions
- STR R0, [R1] ; Store the value in R0 into memory address [R1]
- LDR R0, [R1] ; Load a value from memory address [R1] into R0
- LDRL R0, 0xFF ; Load a literal value (0x00FF) R0
- LDRH R0, 0xFF ; Load a literal value (0xFF00) R0
- LDL R0, 0xFF ; Load a value from memory address (0x00FF) into R0
- LDH R0, 0xFF ; Load a value from memory address (0xFF00) into R0

### Branching Instructions
- JMP [R0] ; Jump to the address in R0
- BGT [R0], R1, R2 ; Branch to address [R0] if R1 is greater than R2
- BLT [R0], R1, R2 ; Branch to address [R0] if R1 is less than R2
- BEQ [R0], R1, R2 ; Branch to address [R0] if R1 is equal to R2
- BSGT [R0], R1, R2 ; Branch to address [R0] if R1 is greater than R2 (Signed Version)
- BSLT [R0], R1, R2 ; Branch to address [R0] if R1 is less than R2 (Signed Version)
- BSEQ [R0], R1, R2 ; Branch to address [R0] if R1 is equal to R2 (Signed Version)

### Math Instructions
- ADD R0, R1, R2 ; Add R1 and R2, store result in R0
- SUB R0, R1, R2 ; Subtract R2 from R1, store result in R0
- MUL R0, R1, R2 ; Multiply R1 and R2, store result in R0
- DIV R0, R1, R2 ; Divide R1 by R2, store result in R0
- REM R0, R1, R2 ; Remainder of R1 divided by R2, store result in R0
- SLL R0, R1, R2 ; Shift left logical R1 by the number of bits stored in R2, store result in R0    
- SLR R0, R1, R2 ; Shift left logical R1 by the number of bits stored in R2, store result in R0    
- SAR R0, R1, R2 ; Shift left logical R1 by the number of bits stored in R2, store result in R0    
- INC R0 ; Increment R0 by 1
- DEC R0 ; Decrement R0 by 1
- RST R0 ; Reset R0 to 0

### Bitwise Instructions
- AND R0, R1, R2 ; Bitwise AND of R1 and R2, store result in R0
- OR R0, R1, R2 ; Bitwise OR of R1 and R2, store result in R0
- XOR R0, R1, R2 ; Bitwise XOR of R1 and R2, store result in R0
- NMOV R0, R1, R2 ; Bitwise NOT of R2, store result in R0, R1 is ignored
- MOV R0, R1, R2 ; R2 stored to R0, R1 is ignored

### IO Instructions
- IN D0, R0 ; Input from device D0 into R0
- OUT D0, R0 ; Output from R0 to device D0
- OUTL D0, 0xFF ; Output a literal value (0x00FF) to device D0
- OUTH D0, 0xFF ; Output a literal value (0xFF00) to device D0

### Stack Instructions
PUSH R0 ; Push R0 onto the stack
POP R0 ; Pop the top value from the stack into R0

### Labels and Subroutines
Labels are defined using the @label: syntax and can be used for subroutines or jump points.

Example:
```asm
section .vars
    msg: .ascii "Hello, World!\n" ; A string variable

section .code
    LDRL R2, 8
    @start:
        LDR R0, msg
        NOP
        @print:
            LDR R1, R0
            OUT D0, R1
            SLL R1, R1, R2
            INC R0
            OUT D0, R1
            LDR R3, @print
            LDR R3, R3
            BGT R3, R1, M0
            LDR R3, @start
            LDR R3, R3
            JMP R3
```
Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.


### Key Sections:
1. **Features**: Highlights the main features of the language.
2. **Example**: Provides a snippet of the [all.kasm](https://github.com/Klinefelters/Kasm/blob/main/examples/all.kasm) file.
3. **Using the Compiler**: Explains how to compile and test Kasm files.
4. **Syntax Highlighting**: Describes how to enable syntax highlighting in Visual Studio Code.
5. **Instructions Overview**: Summarizes the available instructions.
6. **Labels and Subroutines**: Explains how to use labels in Kasm.
7. **Contributing**: Encourages contributions to the project.
8. **License**: Includes licensing information.
