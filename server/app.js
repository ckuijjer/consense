const express = require('express');
const app = express();

function getAvailableResearchData(req, res) {
    res.json({ numberOfPeople: 7 });
}

app.get('/getAvailableResearchData', (req, res) => getAvailableResearchData(req, res));

app.listen(3000, () => console.log('Example app listening on port 3000!'));

if (process.send) {
    process.send('listening');
}
