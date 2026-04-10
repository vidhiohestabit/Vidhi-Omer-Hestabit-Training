# Day 2 — Service Architecture

## Services
1. MongoDB
   - Image: mongo:6
   - Port: 27017
   - Persistent volume: mongo-data

2. Node Server
   - Built from server/Dockerfile
   - Connects to Mongo via mongodb://mongo:27017/day2db
   - Port: 5000

3. React Client
   - Built from client/Dockerfile (Vite)
   - Calls server API at http://localhost:5000
   - Port: 5173

## Networking
- All services share default Docker network
- Server connects to Mongo using service name `mongo`

## Volumes
- `mongo-data` persists MongoDB data

## to run:

- container build: `docker compose up --build`
- down comtainer: `docker compose down`
- remove all running container: `docker rm -f $(docker ps -q)`
- used port: `systemctl stop mongod`