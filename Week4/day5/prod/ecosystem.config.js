module.exports = {
  apps: [
    {
      name: "day5-backend",
      script: "./src/index.js",
      watch: true,
      env: {
        NODE_ENV: "development",
        PORT: 4000
      },
      env_production: {
        NODE_ENV: "production",
        PORT: 4000
      }
    }
  ]
};