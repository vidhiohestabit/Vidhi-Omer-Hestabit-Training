import express from "express";
import { emailQueue } from "../jobs/email.job.js";

const router = express.Router();

router.post("/send", async (req, res) => {
  const { to, subject } = req.body;

  const job = await emailQueue.add(
    "sendEmail",
    { to, subject },
    {
      attempts: 3,
      backoff: {
        type: "exponential",
        delay: 2000
      }
    }
  );

  res.json({
    success: true,
    message: "Email job added to queue",
    jobId: job.id
  });
});

export default router;