const express = require('express');
const cors = require('cors');

const PythonService = require('./python.service');

const app = express();

app.use(cors());

/**
 * route to get the available data for the researcher from the crypto database
 * TODO: implement parameters provided by request
 */
app.get('/getAvailableResearchData', async (req, res) => {
    const payload = {
        mySecretMessage: 'nobody said it was easy :('
    };
    // const responseFromPythonProcess = await getDataFromPythonProcess(payload);
    res.json({ numberOfPeople: 7 });
    // res.json(responseFromPythonProcess);
});

/**
 * gets data from the python process by sending proper payload
 * @returns Promise 
 */
function getDataFromPythonProcess(payload) {
    return new Promise((resolve, reject) => {
        const pc = new PythonService('../BackendTest.py');
        pc.sendMessage(payload);
        const pythonResponse = '';
        pc.output.on('data', function (data) {
            // handle data
            pythonResponse = data;
        });
        pc.output.on('end', function () {
            // handle end of process execution
            resolve(pythonResponse);
        });
    });
}

app.listen(3000, () => console.log('The server app is listening on port 3000!'));

if (process.send) {
    process.send('listening');
}

