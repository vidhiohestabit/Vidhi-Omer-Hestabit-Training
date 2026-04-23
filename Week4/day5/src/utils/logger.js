import winston from "winston";

const logger = winston.createLogger({
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: "logs/app.log" })
  ]
});

export const logRequest = (message) => {
  logger.info(message);
};

export const logError = (message) => {
  logger.error(message);
};