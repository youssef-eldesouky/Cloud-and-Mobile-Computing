#### **1. Containers are better for microservices due to lower startup time, lower memory usage, and reduced overhead.**

#### **2. ApacheBench helped measure overall performance such as throughput and average response time. However, it did not provide individual request latencies, so a custom Python script was used to measure response time for each request.**

#### **3. The histogram generated from the script clearly showed a long-tail distribution, where most requests were fast but a few were significantly slower.**

#### **4. A small number of slow requests can impact the overall user experience even if the average latency is acceptable.**