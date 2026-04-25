# Reflection - Lab 3

## 1. Why do namespaces alone not guarantee fair resource use?
Namespaces isolate resources but do not limit how much of those resources a process can consume. Without cgroups, one container can consume excessive CPU or memory.

## 2. How do cgroups improve cluster stability?
Cgroups enforce resource limits, preventing containers from overusing system resources. This ensures fair distribution and prevents system crashes.

## 3. Why is Docker image layering important?
Layering improves caching, reduces rebuild time, and minimizes storage usage. It allows reuse of unchanged layers across builds.

## 4. What does Kubernetes mean by desired state?
Desired state refers to the configuration defined by the user (e.g., number of replicas). Kubernetes continuously ensures the actual state matches this desired state.

## 5. How is self-healing different from traditional operations?
Traditional systems require manual intervention. Kubernetes automatically detects failures and replaces or restarts components.

## 6. Why are readiness and liveness probes not interchangeable?
Readiness determines if a Pod can receive traffic, while liveness determines if it should be restarted. They serve different purposes.

## 7. What is a limitation of a single-node kind cluster?
A single-node cluster cannot fully demonstrate scheduling decisions across multiple nodes, limiting realism compared to production environments.