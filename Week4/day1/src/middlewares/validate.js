export const validate = (schema) => (req, res, next) => {
  const { error } = schema.validate(req.body, { abortEarly: false });
  if (error) {
    return res.status(400).json({
      success: false,
      message: error.details.map((d) => d.message).join(", "),
      code: "VALIDATION_ERROR",
      path: req.originalUrl,
      timestamp: new Date(),
    });
  }
  next();
};