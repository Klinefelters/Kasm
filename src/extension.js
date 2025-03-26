const vscode = require('vscode');

function activate(context) {
    const hoverProvider = vscode.languages.registerHoverProvider('kasm', {
        provideHover(document, position, token) {
            const range = document.getWordRangeAtPosition(position);
            const word = document.getText(range);

            const tooltips = {
                // Math Operations
                "ADD": "Math Operation: `ADD R1, R2, R3`\nAdds the values in R2 and R3 and stores the result in R1.",
                "SUB": "Math Operation: `SUB R1, R2, R3`\nSubtracts the value in R3 from R2 and stores the result in R1.",
                "MUL": "Math Operation: `MUL R1, R2, R3`\nMultiplies the values in R2 and R3 and stores the result in R1.",
                "DIV": "Math Operation: `DIV R1, R2, R3`\nDivides the value in R2 by R3 and stores the result in R1.",
                "REM": "Math Operation: `REM R1, R2, R3`\nCalculates the remainder of R2 divided by R3 and stores it in R1.",
                "SLL": "Math Operation: `SLL R1, R2, R3`\nPerforms a logical left shift on R2 by the value in R3 and stores the result in R1.",
                "SLR": "Math Operation: `SLR R1, R2, R3`\nPerforms a logical right shift on R2 by the value in R3 and stores the result in R1.",
                "SAR": "Math Operation: `SAR R1, R2, R3`\nPerforms an arithmetic right shift on R2 by the value in R3 and stores the result in R1.",
                "AND": "Math Operation: `AND R1, R2, R3`\nPerforms a bitwise AND on R2 and R3 and stores the result in R1.",
                "NAND": "Math Operation: `NAND R1, R2, R3`\nPerforms a bitwise NAND on R2 and R3 and stores the result in R1.",
                "ORR": "Math Operation: `ORR R1, R2, R3`\nPerforms a bitwise OR on R2 and R3 and stores the result in R1.",
                "NOR": "Math Operation: `NOR R1, R2, R3`\nPerforms a bitwise NOR on R2 and R3 and stores the result in R1.",
                "XOR": "Math Operation: `XOR R1, R2, R3`\nPerforms a bitwise XOR on R2 and R3 and stores the result in R1.",
                "XNOR": "Math Operation: `XNOR R1, R2, R3`\nPerforms a bitwise XNOR on R2 and R3 and stores the result in R1.",
                "NMOV": "Math Operation: `NMOV R1, R2, R3`\nNegates the value in R2 and stores it in R1.",
                "MOV": "Math Operation: `MOV R1, R2`\nCopies the value in R2 to R1.",

                // Instructions
                "NOOP": "Instruction: `NOOP`\nPerforms no operation. Used as a placeholder.",
                "LOAD": "Instruction: `LOAD R1, R2`\nLoads the value from the memory address in R2 into R1.",
                "LOADI": "Instruction: `LOADI mode, imm, R1`\nLoads an immediate value into R1 based on the specified mode.",
                "STORE": "Instruction: `STORE R1, R2`\nStores the value in R1 into the memory address in R2.",
                "JMPIF": "Instruction: `JMPIF condition, R1`\nJumps to the address in R1 if the specified condition is met.",
                "RIO": "Instruction: `RIO R1, R2`\nReads input from the device in R2 into R1.",
                "WIO": "Instruction: `WIO R1, R2`\nWrites the value in R1 to the device in R2.",
                "WIOI": "Instruction: `WIOI mode, imm, R1`\nWrites an immediate value to the device in R1 based on the specified mode.",
                "HALT": "Instruction: `HALT`\nHalts the program execution."
            };

            if (tooltips[word]) {
                return new vscode.Hover(tooltips[word]);
            }
        }
    });

    // Add the hover provider to the context subscriptions
    context.subscriptions.push(hoverProvider);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};