# Reflection on Lab_04

### 1. Which parts of this lab show the benefits of microservices over a monolith?

One clear benefit is the separation between `product-service` and `order-service`. Each service has its own responsibility, which makes the system easier to understand and manage. For example, the product logic is completely independent from the order logic.

Another benefit is that each service can be developed and deployed separately. If we want to update how products are handled, we don’t need to change the order service. This makes the system more flexible.

Also, using Docker containers makes each service isolated. This means each service runs in its own environment, which reduces conflicts and makes deployment more consistent.

### 2. Which new complexities were introduced by splitting the system into two services?

Splitting the system introduced communication between services. Instead of calling functions directly (like in a monolith), the `order-service` now has to send HTTP requests to the `product-service`.

This also means we have to handle errors like timeouts or unavailable services. In this lab, we had to add retry logic and return proper error responses.

Another complexity is configuration. Instead of hardcoding values, we had to use environment variables like `PRODUCT_SERVICE_URL`. This adds flexibility but also requires more setup.

### 3. What would break if network latency increased or one service became slow?

If the `product-service` becomes slow or has high latency, the `order-service` will also become slow because it depends on it. Since the communication is synchronous, the order request will wait until it gets a response.

If the delay is too long, the request may timeout and fail completely. This means users won’t be able to create orders even if the `order-service` itself is working fine.

In general, performance and availability of one service directly affect the other service in this setup.

### 4. Which 12-factor app principles are visible in this implementation?

One principle is using environment variables for configuration. The `PRODUCT_SERVICE_URL` is not hardcoded, which makes the system easier to run in different environments.

Another principle is stateless services. Both services do not store data locally and can be restarted without losing important information.

The services are also exposed through ports, which follows the idea of treating services as independent processes.

Finally, Docker helps separate the build and run stages, and logs are shown through container output, which matches the 12-factor approach.