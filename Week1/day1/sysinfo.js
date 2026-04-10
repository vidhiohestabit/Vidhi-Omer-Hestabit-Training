// sysinfo.js
const os = require("os");
const { execSync } = require("child_process");

function getSysInfo() {
  // Hostname
  const hostname = os.hostname();

  // Available Disk Space (GB)
  let diskSpace = "N/A";
  try {
    const output = execSync("df -BG --total | grep total").toString();
    diskSpace = output.split(/\s+/)[3]; // available column
  } catch {}

  // Open Ports (top 5)
  let openPorts = [];
  try {
    const output = execSync(
      "lsof -i -P -n | grep LISTEN | awk '{print $9}' | head -n 5",
    ).toString();
    openPorts = output.split("\n").filter(Boolean);
  } catch {}

  // Default Gateway
  let defaultGateway = "N/A";
  try {
    defaultGateway = execSync("ip route | grep default | awk '{print $3}'")
      .toString()
      .trim();
  } catch {}

  // Logged-in users count
  let loggedInUsers = 0;
  try {
    loggedInUsers = parseInt(execSync("who | wc -l").toString());
  } catch {}

  return {
    hostname,
    diskSpace,
    openPorts,
    defaultGateway,
    loggedInUsers,
  };
}

module.exports = getSysInfo;
