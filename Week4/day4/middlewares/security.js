import express from "express"; 
import helmet from "helmet";
import rateLimit from "express-rate-limit";
import cors from "cors";
import hpp from "hpp";
import mongoSanitize from "express-mongo-sanitize";
import xss from "xss-clean";

export const securityMiddleware = (app) => {
  // Set security headers
  app.use(helmet());

  // Enable CORS
  app.use(cors());

  // Rate limiting
  const limiter = rateLimit({
    windowMs: 10 * 60 * 1000, // 10 minutes
    max: 100, // limit each IP to 100 requests per windowMs
    message: "Too many requests from this IP, please try again later",
  });
  app.use(limiter);

  // Prevent HTTP param pollution
  app.use(hpp());

  // Data sanitization against NoSQL injection
  app.use(mongoSanitize());

  // Data sanitization against XSS
  app.use(xss());

  // Limit JSON body size
  app.use(express.json({ limit: "10kb" }));
};