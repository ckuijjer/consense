const { spawn } = require('child_process');
// const EventEmitter = require('events');

class PythonService {

    constructor(sourceFileName) {
        this.pythonProcess = spawn('python', [sourceFileName]);
        this.output = pythonProcess.stdout;
    }

    sendMessage(data) {
        this.pythonProcess.stdin.write(JSON.stringify(data));
    }

    endProccess() {
        this.pythonProcess.stdin.end();
    }
}

module.exports = PythonService;