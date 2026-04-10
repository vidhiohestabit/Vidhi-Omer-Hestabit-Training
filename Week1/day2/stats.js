const fs = require("fs").promises;
const path = require("path");
const processArgs = process.argv.slice(2);

// Helper functions
const countLines = (content) => content.split("\n").length;
const countWords = (content) => content.split(/\s+/).filter(Boolean).length;
const countChars = (content) => content.length;
const removeDuplicateLines = (content) =>
  Array.from(new Set(content.split("\n"))).join("\n");

// Log performance to JSON (UNIQUE per file)
const logPerformance = async (file, executionTimeMs, memoryMB) => {
  const logFile = path.join(
    __dirname,
    "logs",
    `performance-${path.basename(file)}-${process.hrtime.bigint()}.json`,
  );

  const logData = {
    file,
    executionTimeMs,
    memoryMB,
    timestamp: new Date().toISOString(),
  };

  await fs.mkdir(path.dirname(logFile), { recursive: true });
  await fs.writeFile(logFile, JSON.stringify(logData, null, 2), "utf-8");
};

// Process a single file
const processFile = async (filePath, flags) => {
  const startTime = process.hrtime();
  const content = await fs.readFile(filePath, "utf-8");

  // Calculate stats
  const stats = {};
  if (flags.includes("--lines")) stats.lines = countLines(content);
  if (flags.includes("--words")) stats.words = countWords(content);
  if (flags.includes("--chars")) stats.chars = countChars(content);

  // Performance
  const endTime = process.hrtime(startTime);
  const executionTimeMs = endTime[0] * 1000 + endTime[1] / 1e6;
  const memoryMB = process.memoryUsage().rss / 1024 / 1024;

  // Output
  console.log(`Stats for ${filePath}:`, stats);
  console.log(
    `Performance -> Execution: ${executionTimeMs.toFixed(2)}ms, Memory: ${memoryMB.toFixed(2)}MB`,
  );

  await logPerformance(filePath, executionTimeMs, memoryMB);

  // Handle --unique
  if (flags.includes("--unique")) {
    const uniqueContent = removeDuplicateLines(content);
    const outputFile = path.join(
      __dirname,
      "output",
      `unique-${path.basename(filePath)}`,
    );
    await fs.mkdir(path.dirname(outputFile), { recursive: true });
    await fs.writeFile(outputFile, uniqueContent, "utf-8");
    console.log(`Unique content saved: ${outputFile}`);
  }

  return { file: filePath, executionTimeMs, memoryMB };
};

// Parse arguments
const parseArgs = (args) => {
  const flags = [];
  const files = {};

  args.forEach((arg, i) => {
    if (arg === "--lines" && args[i + 1]) files.lines = args[i + 1];
    if (arg === "--words" && args[i + 1]) files.words = args[i + 1];
    if (arg === "--chars" && args[i + 1]) files.chars = args[i + 1];
    if (arg === "--unique") flags.push("--unique");
  });

  // Always calculate stats
  flags.push("--lines", "--words", "--chars");

  return { flags, files };
};

// Main
const main = async () => {
  const { flags, files } = parseArgs(processArgs);
  const filePaths = Object.values(files).filter(Boolean);

  if (filePaths.length === 0) {
    console.error(
      "Please provide at least one file with --lines, --words, or --chars",
    );
    return;
  }

  console.log("Processing files in parallel...");

  const results = await Promise.all(
    filePaths.map((file) => processFile(file, flags)),
  );

  console.log("\n=== PERFORMANCE REPORT ===");
  console.log(JSON.stringify(results, null, 2));
};

main();
