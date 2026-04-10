# Day 3 — NGINX Reverse Proxy + Load Balancing

## Setup

- Two backend containers (`backend1`, `backend2`) running Node.js on port 3000
- NGINX container as reverse proxy, listening on port 8080
- Requests to `/api` routed to backend services with **round-robin load balancing**

## Testing

1. Check running containers:

```bash
docker ps

Send requests:

curl http://localhost:8080/api

## running

docker compose up --build
