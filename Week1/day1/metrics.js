function getRuntimeMetrics() {
  return {
    cpuUsage: process.cpuUsage(),
    resourceUsage: process.resourceUsage(),
  };
}

module.exports = getRuntimeMetrics;
