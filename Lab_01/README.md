# Lab 1 - Exploring Cloud Virtualization and Data Center Architecture

### Objective
Compare VMs and containers, inspect cloud infrastructure, and observe tail latency behavior.



## Part A - VM vs Container

### Files
- part-a/screenshots/vm-launch.png
- part-a/screenshots/vm-resources.png
- part-a/screenshots/container-launch.png
- part-a/screenshots/container-resources.png
- part-a/comparison.md

### Summary
In this part, a Virtual Machine (VM) was launched using Multipass and a container was launched using Docker. Both environments were analyzed using system commands to compare their resource usage and behavior.

The following commands were used in both environments:
- `free -h` → to check memory usage
- `ps aux --sort=-%mem | head` → to inspect running processes
- `df -h` → to check disk usage


### Conclusion

Containers are more lightweight and efficient, making them suitable for microservices and scalable applications. Virtual Machines, on the other hand, provide stronger isolation and are better suited for cases requiring a full operating system environment.

## Part B - Cloud Infrastructure Exploration

Could not be implemented on AWS (Requires Card Information for Payments and Subscription Plans)

## Part C - Tail Latency Mini-Simulation

### Files
- part-c/app/app.py
- part-c/scripts/measure_latency.py
- part-c/results/ab-output.txt
- part-c/results/response_times.csv
- part-c/results/latency_histogram.png
- part-c/screenshots/flask-running.png
- part-c/screenshots/test-flask-running.png
- part-c/screenshots/script-running.png
- part-c/screenshots/ab-command-output.png



### Summary
A Flask application with random delay was deployed locally. ApacheBench was used to simulate concurrent requests, and a custom Python script was used to collect response times and generate a histogram.

The results demonstrated tail latency behavior, where most requests are fast but some are significantly slower.
