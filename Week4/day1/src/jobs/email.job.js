import { Queue, Worker } from "bullmq";
import IORedis from "ioredis";

const connection = new IORedis({
  maxRetriesPerRequest: null
});

export const emailQueue = new Queue("emailQueue", { connection });

export const startEmailWorker = () => {
  new Worker(
    "emailQueue",
    async (job) => {
      console.log(`[Worker] Processing job ${job.id}:`, job.data);

      // Simulate email sending
      await new Promise((resolve) => setTimeout(resolve, 1000));

      console.log(`[Worker] Email sent to: ${job.data.to}`);

      return { success: true };
    },
    { connection }
  );
};