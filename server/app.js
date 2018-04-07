const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

function getAvailableResearchData(req, res) {
    res.json({ numberOfPeople: 7 });
}

app.get('/getAvailableResearchData', (req, res) => getAvailableResearchData(req, res));

app.listen(3000, () => console.log('Example app listening on port 3000!'));

if (process.send) {
    process.send('listening');
}
