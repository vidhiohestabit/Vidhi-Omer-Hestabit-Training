const express = require("express");
const mongoose = require("mongoose");
require("dotenv").config();

const app = express();

app.use(express.json());

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("Mongo Connected"))
  .catch(err => console.log(err));

app.get("/health", (req, res) => {
  res.status(200).json({ status: "OK" });
});

app.get("/api/message", (req, res) => {
  res.json({ message: "Hello from Backend 🚀" });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});