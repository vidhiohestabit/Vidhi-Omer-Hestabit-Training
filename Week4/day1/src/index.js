import express from "express";
import dotenv from "dotenv";
import connectDB from "./config/index.js"; // your db connection
import { securityMiddleware } from "./middlewares/security.js";
import productRoutes from "./routes/product.routes.js";
import userRoutes from "./routes/user.routes.js";
import { requestTracer } from "./utils/tracing.js";
import { startEmailWorker } from "./jobs/email.job.js";
import emailRoutes from "./routes/email.routes.js";


dotenv.config();

const app = express();

app.use(express.json());
app.use("/email", emailRoutes);
// Request Tracing Middleware
app.use(requestTracer);

// Global Security Middlewares
securityMiddleware(app);

// Health check route
app.get("/health", (req, res) => {
  res.status(200).json({
    status: "OK",
    uptime: process.uptime(),
    timestamp: new Date(),
    requestId: req.requestId
  });
});

// Routes
app.use("/products", productRoutes);
app.use("/users", userRoutes);

const startServer = async () => {
  await connectDB(); // ensure DB connects before server start
  console.log(" DB connected");

  // Start Email Worker
  startEmailWorker();
  console.log("📨 Email worker started");

  const PORT = process.env.PORT || 4000;

  app.listen(PORT, () => {
    console.log(`🚀 Secure Server running on port ${PORT}`);
  });
};

startServer();