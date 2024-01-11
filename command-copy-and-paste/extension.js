const vscode = require('vscode');
const fs = require('fs');

async function input(command, prompt, terminal) {
    const user_input = await vscode.window.showInputBox({
        placeHolder: command,
        prompt: prompt,
        value: command
    });

    if (user_input === '') {
        vscode.window.showErrorMessage('A search query is mandatory to execute this action');
    }

    if (user_input !== undefined) {
        console.log(user_input);
        terminal.sendText(user_input, true);
    }
}

async function executeCommands(commands, terminal) {
    for (let i = 0; i < commands.length; i++) {
        await input(commands[i], "Please modify the command and press Enter.", terminal);
    }
}

function readTxtFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n').map(line => line.trim()).filter(line => line !== '');
    return lines;
}

function activate(context) {
    const terminal = vscode.window.createTerminal("Open Terminal");
    context.subscriptions.push(terminal);

    let disposable = vscode.commands.registerCommand('command-copy-and-paste.openCmdFolder', () => {
        const editor = vscode.window.activeTextEditor;

        if (editor && editor.document.languageId === 'plaintext') {
            const txtFilePath = editor.document.fileName;
            const commands = readTxtFile(txtFilePath);
            
            if (commands.length > 0) {
                terminal.show();
                executeCommands(commands, terminal);
            } else {
                vscode.window.showWarningMessage('The file is empty or does not contain valid commands.');
            }
        } else {
            vscode.window.showErrorMessage('Open a .txt file in the editor.');
        }
    });

    context.subscriptions.push(disposable);
}

function deactivate() {
    // Cleanup logic, if any
}

module.exports = {
    activate,
    deactivate
};
