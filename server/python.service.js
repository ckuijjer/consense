const { spawn } = require('child_process');

class PythonService {

    constructor(sourceFileName) {
        this.pythonProcess = spawn('python', [sourceFileName]);
        this.output = this.pythonProcess.stdout;
        this.pythonProcess.on('exit', (code, signal) => {
            if (code !== 0) {
                console.error('exit code:', code);
            }
        });
    }

    sendMessage(data) {
        this.pythonProcess.stdin.write(JSON.stringify(data));
    }

    endInput() {
        this.pythonProcess.stdin.end();
    }
}

module.exports = PythonService;