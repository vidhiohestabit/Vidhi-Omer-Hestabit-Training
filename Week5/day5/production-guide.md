# Week 5 — Day 5: CI-Style Deployment Automation + Capstone

## Overview
This guide documents the production deployment of the full-stack application using **Docker**, **docker-compose**, and **NGINX reverse proxy** with **HTTPS**.

The application stack consists of:

- **Frontend:** React app (`/client`)
- **Backend:** Node.js + Express app (`/server`)
- **Database:** MongoDB
- **Reverse Proxy:** NGINX with HTTPS termination

The deployment is automated via `deploy.sh` and environment configuration is handled using `.env` file.

---

## 1️⃣ Prerequisites

Make sure the following are installed on your system:

- Docker & Docker Compose
- Node.js and npm (for building frontend/backend locally if needed)
- OpenSSL or mkcert for SSL certificate generation
- curl (for healthcheck testing)
- Browser (for testing frontend)

---

## 2️⃣ Project Structure


day5/
├─ client/ # React frontend
├─ server/ # Node.js backend
├─ nginx/ # NGINX config + SSL certs
│ ├─ nginx.conf
│ └─ certs/
├─ docker-compose.prod.yml # Production docker-compose file
├─ deploy.sh # Deployment automation script
├─ .env # Environment variables (not committed)
└─ production-guide.md # This guide


---

## 3️⃣ Environment Variables (.env)

Create a `.env` file in the root directory (not committed to git):


MONGO_URI=mongodb://mongo:27017/day5db
BACKEND_PORT=3000
NODE_ENV=production


> **Note:** You can provide `.env.example` without secrets for submission.

---

## 4️⃣ Backend Health Route

The backend exposes a health route for monitoring:

```js
// server/index.js
app.get("/health", (req, res) => {
  res.status(200).json({ status: "OK" });
});

This is required for the Docker healthcheck in docker-compose.prod.yml.

5️⃣ Docker Compose Configuration

docker-compose.prod.yml defines services:

mongo: Database container with persistent volume

backend: Node.js API

Depends on mongo

Healthcheck configured

Restart policy: always

frontend: React app

Built and served via NGINX

reverse-proxy: NGINX

Ports: 443:443, 3000:3000 (HTTP optional)

Mounts SSL certificates and NGINX config

Depends on backend and frontend

Volumes:

mongo_data for MongoDB persistence

Healthcheck example:

healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
  interval: 10s
  retries: 5

Restart policy:

restart: always
6️⃣ Deployment Script

deploy.sh automates the following:

Stop and remove existing containers

Build backend and frontend Docker images

Start all containers using docker-compose.prod.yml

Usage:

chmod +x deploy.sh
./deploy.sh

Expected output:

✔ Container day5-mongo-1         Created
✔ Container day5-frontend-1      Created
✔ Container day5-backend-1       Created
✔ Container day5-reverse-proxy-1 Created
7️⃣ Verifying Deployment
7.1 Check Running Containers
docker ps

Example output:

CONTAINER ID   IMAGE           STATUS                    PORTS
...            day5-backend    Up (healthy)             3000/tcp
...            day5-frontend   Up                       80/tcp
...            day5-reverse-proxy Up                    443/tcp, 3000/tcp
...            mongo:6         Up                       27017/tcp
7.2 Healthcheck
curl http://localhost:3000/health

Expected output:

{"status":"OK"}
7.3 Frontend Access

Open browser: https://localhost (or your domain)

Check lock icon in address bar → HTTPS is working

Application UI should load

7.4 Backend Logs
docker logs day5-backend-1

Expected:

Server running on port 3000
Mongoose connected successfully
8️⃣ SSL Certificates

Stored in nginx/certs/

Used by NGINX for HTTPS termination

Generated via mkcert or OpenSSL

NGINX config (nginx/nginx.conf) points to server.crt and server.key

9️⃣ Notes / Tips

Remove obsolete version: attribute from docker-compose.prod.yml to avoid warnings

Use .env for secrets; never commit

Frontend build must be done before deployment (npm run build inside /client)

Restart policy ensures containers restart on failure

10️⃣ Proof / Submission

Include:

docker-compose.prod.yml

deploy.sh

.env.example

production-guide.md (this file)

Optional: Demo recording

Show running containers

curl /health returning {"status":"OK"}

Browser frontend via HTTPS

Screenshots placeholders:

Docker Containers Running:


Backend Healthcheck:


Frontend via HTTPS:


To run :

chmod +x deploy.sh
./deploy.sh
curl -L http://localhost:8080
curl -L http://localhost:8080/api/health