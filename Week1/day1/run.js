// run.js
console.log("RUN.JS STARTED");

const fs = require("fs");
const path = require("path");
const getSysInfo = require("./sysinfo");
const getRuntimeMetrics = require("./metrics");

try {
  // Collect data
  const systemInfo = getSysInfo();
  const runtimeMetrics = getRuntimeMetrics();

  // Print to terminal
  console.log("\nSYSTEM INFO:");
  console.log(systemInfo);

  console.log("\nRUNTIME METRICS:");
  console.log(runtimeMetrics);

  // Ensure logs directory exists
  const logDir = path.join(__dirname, "logs");
  if (!fs.existsSync(logDir)) fs.mkdirSync(logDir);

  // Prepare log data
  const logData = {
    timestamp: new Date().toISOString(),
    systemInfo,
    runtimeMetrics,
  };

  fs.writeFileSync(
    path.join(logDir, "day1-sysmetrics.json"),
    JSON.stringify(logData, null, 2),
  );
  console.log("\nSaved to logs/day1-sysmetrics.json");
} catch (error) {
  console.error("ERROR IN run.js:", error.message);
}
