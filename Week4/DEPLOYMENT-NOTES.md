# DEPLOYMENT-NOTES.md

# Secure Backend API — Deployment Notes

## 1. Overview

This project implements a secure backend with:

- REST APIs for **products** and **users**
- **Async job queue** using BullMQ (email notifications)
- **Structured logging** (app.log and error.log)
- **Request tracing** (`X-Request-ID`)
- **Validation & security middlewares**
- **Production-ready setup** with PM2

---

## 2. Pre-requisites

Before deployment, ensure you have installed:

- **Node.js** (v20.x recommended)
- **npm**
- **MongoDB** (running locally or remote)
- **Redis** (for BullMQ queues)
- **PM2** (optional, for production process management)

---

## 3. Environment Setup

1. Copy environment variables from `.env.example`:

```bash
cp prod/.env.example .env

