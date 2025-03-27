// filepath: c:\Users\steve\.vscode\Git\Kasm\tooltips\extension.js
const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

function loadTooltips() {
    const tooltips = {};
    const tooltipsDir = path.join(__dirname, './tooltips'); // Path to the tooltips folder

    // Read all Markdown files in the tooltips folder
    const files = fs.readdirSync(tooltipsDir);
    files.forEach(file => {
        if (file.endsWith('.md')) {
            const filePath = path.join(tooltipsDir, file);
            const content = fs.readFileSync(filePath, 'utf-8');
            console.log(content);

            // Parse the Markdown file content
            content.split('##').forEach(entry => {
                console.log(entry);
                const [key, ...description] = entry.split(':');
                if (key && description.length > 0) {
                    tooltips[key.trim()] = description.join(':').trim();
                }
            });
        }
    });

    return tooltips;
}

function activate(context) {
    const tooltips = loadTooltips();

    const hoverProvider = vscode.languages.registerHoverProvider('kasm', {
        provideHover(document, position, token) {
            const range = document.getWordRangeAtPosition(position);
            const word = document.getText(range);

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