const { spawn } = require('child_process');
const EventEmitter = require('events');

export class PythonCommunicator {

    pythonProcess;
    output;

    constructor(sourceFileName) {
        pythonProcess = spawn('python', [sourceFileName]);
        output = pythonProcess.stdout;
    }

    sendMessage(data) {
        pythonProcess.stdin.write(JSON.stringify(data));
    }

    endProccess() {
        pythonProcess.stdin.end();
    }
}