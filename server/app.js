const express = require('express');
const cors = require('cors');

import { PythonCommunicator } from "./python-communicator";

const app = express();

app.use(cors());

/**
 * route to get the available data for the researcher from the database
 */
app.get('/getAvailableResearchData', (req, res) => {
    const pc = new PythonCommunicator('test.py');
    pc.output.on('data', function (data) {
        // handle data
    });
    pc.output.on('end', function () {
        // handle end
    });
    res.json({ numberOfPeople: 7 });
});

app.listen(3000, () => console.log('Example app listening on port 3000!'));

if (process.send) {
    process.send('listening');
}

