## Backend System Bootstrapping & Lifecycle Architecture

This document describes the **architecture, bootstrapping flow, and lifecycle design** of the backend system built during **Week 4 – Day 1**.

The focus of Day 1 is to establish a **production-grade foundation** that supports:
- Deterministic startup and shutdown
- Environment-driven configuration
- Clear separation of concerns
- Observability from the first boot
- Future scalability and extensibility

This is not a feature-oriented setup, but a **system-oriented backend architecture**.

---

## Overview

The backend is designed as a **long-running Node.js service** following layered architecture principles.  
Each layer has a single responsibility and communicates only with adjacent layers.

Primary goals:
- Predictable application lifecycle
- Clean dependency orchestration
- Centralized logging
- Safe failure handling
- Readiness for production workloads

---

## Folder Structure (Day 1 Scope)

```text
src/
├── app.js               # Application entry point
│
├── config/              # Environment & configuration loading
│   └── index.js
│
├── loaders/             # System bootstrapping
│   ├── app.js           # Express initialization
│   └── db.js            # Database connection
│
├── models/              # Schemas (introduced later)
├── repositories/        # DB access layer (introduced later)
├── services/            # Business logic (introduced later)
├── controllers/         # HTTP controllers (introduced later)
├── routes/              # Route definitions
│
├── middlewares/         # Global & custom middlewares
├── utils/               # Logger, helpers
├── jobs/                # Background jobs (introduced later)
├── logs/                # Application logs
Architectural Principles
Separation of Concerns

Each layer owns one responsibility only.

Layer	Responsibility
app.js	System coordination
config	Environment configuration
loaders	Dependency orchestration
routes	HTTP route mapping
controllers	Request/response handling
services	Business rules
repositories	Database operations
utils	Cross-cutting utilities

Rules:

No business logic in controllers

No database logic outside repositories

No environment access outside config

Dependency Direction

Dependencies flow strictly downward:

Routes → Controllers → Services → Repositories → Database

No circular dependencies

No cross-layer shortcuts

Loaders exist outside the request lifecycle

Application Lifecycle
Startup Flow
node src/app.js
   ↓
Load environment configuration
   ↓
Initialize logger
   ↓
Connect to database
   ↓
Initialize Express application
   ↓
Load global middlewares
   ↓
Mount routes
   ↓
Register error middleware
   ↓
Start HTTP server

Each step must complete successfully before proceeding.
Failure at any critical step causes the application to exit safely.

Entry Point (src/app.js)
Responsibilities

Load configuration

Initialize logging

Establish database connection

Bootstrap Express via app loader

Start the HTTP server

Register graceful shutdown handlers

Non-Responsibilities

No business logic

No route definitions

No database queries

The entry point acts only as a system coordinator.

Configuration Management
Environment Isolation

The backend supports multiple environments:

NODE_ENV	Config File
local	.env.local
dev	.env.dev
prod	.env.prod

Rules:

No hardcoded values

Secrets come only from environment variables

Configuration is loaded once at startup

Missing or invalid config results in startup failure

Loaders
App Loader (loaders/app.js)

Responsible for:

Creating the Express application

Registering global middlewares

Mounting routes

Registering centralized error handling

Not responsible for:

Starting the HTTP server

Connecting to the database

Database Loader (loaders/db.js)

Responsible for:

Establishing database connection

Verifying connectivity at startup

Failing fast if connection cannot be established

The application does not start in a partial DB state.

Logging Strategy
Logger Design

Centralized logger utility

Structured logs

Environment-aware verbosity

Mandatory Startup Logs
✔ Configuration loaded
✔ Logger initialized
✔ Database connected
✔ Middlewares loaded
✔ Routes mounted: <count>
✔ Server started on port <PORT>

Logs are written to:

Console (development)

Files under /logs (production-ready)

Graceful Shutdown

The application listens for:

SIGINT

SIGTERM

Unhandled promise rejections

Shutdown sequence:

Receive shutdown signal
   ↓
Stop accepting new requests
   ↓
Close database connection
   ↓
Flush logs
   ↓
Exit process

This prevents:

Dropped requests

Corrupted connections

Incomplete operations

Failure Philosophy

Fail fast during startup

Never run in a partially initialized state

Prefer controlled crash over undefined behavior

Centralized error handling ensures consistent failure behavior.

Scalability Readiness

Although clustering and workers are introduced later, Day 1 architecture is designed to:

Run behind a process manager (PM2)

Scale horizontally

Remain stateless at the HTTP layer

Externalize all configuration

Future Extensions

This architecture supports:

Advanced data modeling and repositories (Day 2)

Query engines and soft deletes (Day 3)

Security hardening (Day 4)

Async job queues and observability (Day 5)

No architectural refactor is required to add these capabilities.

Summary

Week 4 Day 1 establishes a strong backend foundation by focusing on:

Deterministic lifecycle management

Clean architecture boundaries

Production-safe bootstrapping

Long-term maintainability

This system is designed to evolve safely through the rest of Week 4 without breaking core architectural