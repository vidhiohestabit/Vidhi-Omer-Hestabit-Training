import express from "express";
import connectDB from "./db.js";
import productRoutes from "../routes/product.routes.js";
import { errorHandler } from "../middlewares/error.middleware.js";
import { applySecurity } from "../middlewares/security.js";

const createApp = async () => {
  const app = express();

  app.use(express.json());
  applySecurity(app);
  await connectDB();

  app.use("/products", productRoutes);

  // Global error middleware (last)
  app.use(errorHandler);

  return app;
};

export default createApp;