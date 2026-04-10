// index.js
const express = require('express');
const app = express();
const PORT = 3001;

app.get('/', (req, res) => res.send('Hello from Docker!'));

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));