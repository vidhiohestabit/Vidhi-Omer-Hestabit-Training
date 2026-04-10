const http = require("http");

let counter = 0; // in-memory counter

const server = http.createServer((req, res) => {
  const { url, method, headers } = req;

  // /ping → return timestamp
  if (url === "/ping" && method === "GET") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify({
        message: "pong",
        timestamp: new Date().toISOString(),
      }),
    );
    return;
  }

  // /headers → return request headers
  if (url === "/headers" && method === "GET") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(headers, null, 2));
    return;
  }

  // /count → increment and return count
  if (url === "/count" && method === "GET") {
    counter++;
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(
      JSON.stringify({
        count: counter,
      }),
    );
    return;
  }

  // Default route (404)
  res.writeHead(404, { "Content-Type": "application/json" });
  res.end(
    JSON.stringify({
      error: "Route not found",
    }),
  );
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
