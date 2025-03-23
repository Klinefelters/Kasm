const vscode = require('vscode');

function activate(context) {
    const hoverProvider = vscode.languages.registerHoverProvider('kasm', {
        provideHover(document, position, token) {
            const range = document.getWordRangeAtPosition(position);
            const word = document.getText(range);

            const tooltips = {
                // Declarables
                "register": "Declaration: `name = new register`\nDefines a new 5-bit register. Maximum of 32 registers allowed.",
                "address": "Declaration: `name = new address`\nDefines a new 24-bit memory address. Maximum of 2^24 addresses allowed.",
                "device": "Declaration: `name = new device(index)`\nDefines a new device with a 5-bit index. Maximum index value is 31.",
                "int": "Declaration: `name = new int(value)`\nDefines a new integer value. Maximum value is 2^24 - 1.",
                "char": "Declaration: `name = new char('character')`\nDefines a new character value. Converts the character to its ASCII representation.",

                // Instructions
                "In": "Instruction: `In(device, register)`\nReads input from the specified device into the given register.",
                "Out": "Instruction: `Out(device, register)`\nWrites the value of the given register to the specified device.",
                "Jump": "Instruction: `Jump(address)`\nJumps to the specified memory address.",
                "Halt": "Instruction: `Halt`\nHalts the program execution.",
                "NoOp": "Instruction: `NoOp`\nPerforms no operation. Used as a placeholder.",
                "Load": "Instruction: `Load(register, address)`\nLoads the value from the specified memory address into the given register.",
                "LoadL": "Instruction: `LoadL(register, value)`\nLoads a literal value into the specified register.",
                "Store": "Instruction: `Store(register, address)`\nStores the value of the specified register into the given memory address."
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