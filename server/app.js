const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const PythonService = require('./python.service');

const app = express();

app.use(cors());
app.use(bodyParser.json());


// just a test route to check if server is working properly
app.get('/getTestResponseFromServer', (req, res) => {
    res.json('ok');
});

// request for available research data based on provided parameters
app.get('/getAvailableResearchData' /*/sex/:sex/age:age/'*/, makeRequestForResearchData);

/**
 * @param sex
 * @param age
 */
async function makeRequestForResearchData(req, res) {
    const payload = {
        mySecretMessage: 'nobody said it was easy :('
    };
    const responseFromPythonProcess = await getDataFromPythonProcess(payload);
    res.json(responseFromPythonProcess);
}



/**
 * gets data from the python process by sending proper payload
 * @returns Promise that resolves with response from python app
 */
function getDataFromPythonProcess(payload) {
    return new Promise((resolve, reject) => {
        const pc = new PythonService('../BackendTest.py');
        pc.sendMessage(payload);
        pc.endInput();
        let pythonResponse = 'no data received';

        pc.output.on('data', function (data) {
            // handle data
            console.log('incoming data:', data.toString());
            pythonResponse = data.toString();
        });
        pc.output.on('end', function () {
            // handle end of process execution
            console.log('process ended')
            resolve(pythonResponse);
        });
    });
}

app.listen(3000, () => console.log('The server app is listening on port 3000!'));

if (process.send) {
    process.send('listening');
}

