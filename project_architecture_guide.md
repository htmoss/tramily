# Subway-Style Location Tracker — Tech Stack & Architecture Guide

## 1. Executive Summary

This document serves as the primary architectural blueprint and tech stack reference for the **Subway-Style Location Tracker** project. The application is a full-stack Single Page Application (SPA) designed to display personal network connections as visual subway/transit lines, where stops represent generalized location states (e.g., *Home*, *Work*, *Gym*) without exposing precise GPS coordinates.

---

## 2. Tech Stack Overview

| Layer | Technology | Decision & Justification |
| :--- | :--- | :--- |
| **Frontend Framework** | **React + Vite** | High-performance client-side development with minimal build overhead. Optimized for single-page dashboard interaction. |
| **Routing** | **TanStack Router** | Fully type-safe client-side routing. Ideal for handling path parameters (e.g., active connection views or transit line details). |
| **State & Data Fetching** | **TanStack Query** | Efficient server-state management, automated caching, and clean polling hooks for status updates. |
| **Backend Framework** | **Django + Django Ninja** | Django's robust ORM and security paired with Django Ninja's FastAPI-like experience (Pydantic models, type hints, auto-generated OpenAPI docs). |
| **Database** | **PostgreSQL** | Relational data model perfect for graph-like transit structures (Users $\rightarrow$ Lines $\rightarrow$ Stations/Stops $\rightarrow$ Current Status). |
| **Hosting & Deployment** | **Render** | Streamlined platform-as-a-service (PaaS) handling both the containerized Django app and managed PostgreSQL instance. |
| **Authentication** | **Magic Code / Link Auth** | Custom passwordless flow using timed tokens (Django `SigningSerializer` / `django-sesame`). |

---

## 3. High-Level System Architecture

```
+-----------------------------------------------------------------------+
|                           FRONTEND (Render / CDN)                     |
|                                                                       |
|   +---------------------------------------------------------------+   |
|   |                       React SPA (Vite)                        |   |
|   |                                                               |   |
|   |   +----------------------+        +-----------------------+   |   |
|   |   |   TanStack Router    |        |    TanStack Query     |   |   |
|   |   +----------------------+        +-----------------------+   |   |
|   +---------------------------------------------------------------+   |
+-----------------------------------│-----------------------------------+
                                    │ HTTP REST API
                                    ▼
+-----------------------------------------------------------------------+
|                        BACKEND (Render Web Service)                   |
|                                                                       |
|   +---------------------------------------------------------------+   |
|   |                       Django + Django Ninja                   |   |
|   |                                                               |   |
|   |   +----------------------+        +-----------------------+   |   |
|   |   | Magic Code Auth API  |        |  OpenAPI / Swagger UI |   |   |
|   |   +----------------------+        +-----------------------+   |   |
|   +---------------------------------------------------------------+   |
+-----------------------------------│-----------------------------------+
                                    │ Django ORM
                                    ▼
+-----------------------------------------------------------------------+
|                       DATABASE (Render PostgreSQL)                    |
|                                                                       |
|   +---------------+     +---------------+     +-------------------+   |
|   |  User Profile | ───>| Transit Line  | ───>|   Station / Stop  |   |
|   +---------------+     +---------------+     +-------------------+   |
+-----------------------------------------------------------------------+
```

---

## 4. Key Architectural Decisions & Details

### 4.1 Django Ninja vs. Standard Django REST Framework
* **Type Safety & Schema Validation:** Built natively on **Pydantic**, ensuring request/response parsing with standard Python type annotations.
* **Built-in Interactive API Docs:** OpenAPI / Swagger UI generated automatically at `/api/docs`.
* **Clean Syntax:** Modern function-based view pattern with explicit path parameters.

### 4.2 Data Modeling Strategy (PostgreSQL)
A relational model maps naturally to subway systems:
* **User:** Account info, contacts, active status.
* **Line:** Visual line mapping associated with a specific friend/connection (color, route ID).
* **Station / Stop:** Discrete general location categories (*Home*, *Work*, *Gym*, *In Transit*, *Out of Town*).
* **UserLocationState:** Current stop association per user with timestamp tracking.

### 4.3 Real-Time & Polling Strategy
* Initial implementation leverages **TanStack Query** with configurable `refetchInterval` polling.
* Transition to WebSockets (e.g., via Django Channels or Render WebSocket support) if lower latency is needed in future iterations.

---

## 5. Environment Setup & Milestones

### Phase 1: Core Setup & Data Schema
- [ ] Initialize Django project with `django-ninja` and PostgreSQL connection.
- [ ] Set up Vite + React + TanStack Router project structure.
- [ ] Define DB models: `User`, `TransitLine`, `Station`, `UserLocationState`.

### Phase 2: Auth Flow & API Implementation
- [ ] Implement passwordless magic code generation and verification endpoints.
- [ ] Build CRUD endpoints for updating current station status.
- [ ] Configure auto-generated OpenAPI documentation (`/api/docs`).

### Phase 3: Frontend Visualization & Integration
- [ ] Build SVG / Canvas component for subway lines and stations.
- [ ] Integrate TanStack Query for polling active line states.
- [ ] Implement user state selection interface (e.g., updating "Current Stop").

### Phase 4: Deployment on Render
- [ ] Provision PostgreSQL instance on Render.
- [ ] Deploy Django web service (using `gunicorn` or `uvicorn`).
- [ ] Host static frontend assets on Render Static Sites / CDN.

---

*Document version: 1.0.0*
