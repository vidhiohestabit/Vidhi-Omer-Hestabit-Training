// backend/index.js
const express = require('express');
const app = express();
const PORT = 3000;

const INSTANCE_NAME = process.env.INSTANCE_NAME || 'backend';

app.get('/api', (req, res) => {
  res.json({ message: `Hello from ${INSTANCE_NAME} on port ${PORT}!` });
});

app.listen(PORT, () => {
  console.log(`Backend running: ${INSTANCE_NAME} on port ${PORT}`);
});