# Lab 4 - Microservices and Cloud-Native Design

### Overview

This lab demonstrates how to build a simple cloud-native system using two Python Flask microservices: `product-service` and `order-service`. The project focuses on microservice communication, Docker containerization, Docker Compose orchestration, health checks, environment variables, and basic failure simulation.

The lab is organized into separate parts so that each section has its own files, screenshots, and outputs.

## Folder Structure

### Lab 04

- `README.md` → main overview for the lab
- `Reflection on Lab_04.md` → answers to the reflection questions
- `docker-compose.yml` → runs both services together with Docker Compose

### Part A - Project Setup

This part contains the initial notes for the project structure and setup decisions.

Files in this folder:

- `notes.md`

### Part B - product-service

This part contains the source code, dependencies, Dockerfile, and screenshots for the product lookup microservice.

Files in this folder:

- `app.py`
- `requirements.txt`
- `Dockerfile`

Screenshots in the `screenshots` folder:

- `B1-product-health.png`
- `B2-product-found.png`
- `B3-product-not-found.png`

### Part C - order-service

This part contains the source code, dependencies, Dockerfile, and screenshots for the order microservice.

Files in this folder:

- `app.py`
- `requirements.txt`
- `Dockerfile`

Screenshots in the `screenshots` folder:

- `C1-order-success.png`

### Part D - Docker Compose

This part contains the screenshots showing the Docker Compose orchestration and container status.

Screenshots in the `screenshots` folder:

- `D1-docker-compose-up.png`
- `D2-docker-compose-ps.png`
- `D3-logs-product-service.png`
- `D4-logs-order-service.png`

### Part E - Functional Testing

This part contains the screenshots showing successful API calls for both services.

Screenshots in the `screenshots` folder:

- `E1-test-product-health.png`
- `E2-test-product-found.png`
- `E3-test-order-success.png`

### Part F - Failure Simulation

This part contains the screenshots showing failure simulation after stopping `product-service` and testing how `order-service` behaves.

Screenshots in the `screenshots` folder:

- `F1-product-service-stopped.png`
- `F2-order-service-failure.png`
- `F3-product-service-restarted.png`

## What Was Implemented

### Part A

- Created a clean project structure for the lab
- Separated the lab into organized parts for easier submission and review

### Part B

- Implemented `product-service` using Flask
- Added `/health` and `/products/<product_id>` endpoints
- Used in-memory product data for simplicity
- Containerized the service with its own Dockerfile

### Part C

- Implemented `order-service` using Flask and Requests
- Added `/health` and `/orders` endpoints
- Used `PRODUCT_SERVICE_URL` as an environment variable
- Added synchronous communication with `product-service`
- Returned appropriate HTTP responses for successful and failed requests

### Part D

- Created a Docker Compose setup for both services
- Connected the services through the Docker network
- Added health checks and restart policies

### Part E

- Tested the `product-service` endpoints successfully
- Tested the `order-service` with a valid order request
- Verified the JSON responses from both services

### Part F

- Simulated failure by stopping `product-service`
- Observed the effect on `order-service`
- Verified error handling and service dependency behavior

## Outputs and Evidence

All screenshots are stored inside the matching part folders under their respective `screenshots` subfolders.

The project files are organized so that each part is easy to locate and review.

## Reflection

The answers to the reflection questions are available in:

- `Reflection on Lab_04.md`

## Conclusion

This lab demonstrated the basics of microservices architecture, containerization, orchestration with Docker Compose, and service-to-service communication. It also showed how failures in one service can affect another service in a distributed system.