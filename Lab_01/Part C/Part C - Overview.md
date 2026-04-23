## Part C — Tail Latency Mini-Simulation

The goal of this part was to simulate and analyze tail latency in a simple web service using a Flask application with artificial delay.




## Flask Application
A simple Flask application was created that introduces a random delay before responding to each request:

- The delay follows an exponential distribution.
- This simulates real-world unpredictable response times.

The application was run locally on:
http://localhost:5000/


## Benchmarking using ApacheBench

ApacheBench (`ab`) was used to simulate multiple users accessing the service.

Command used:

```.\ab -n 100 -c 10 http://localhost:5000/ > "C:\Users\PC\Desktop\Cloud and Mobile Computing\lab-01\part-c\results\ab-output.txt"```


This file contains:
- total requests
- time taken
- requests per second
- time per request
- failed requests (if any)


## Latency Measurement Script

Since ApacheBench provides summary statistics only, a custom Python script was used to collect individual response times.

The script:
- sent 100 requests with concurrency = 10
- measured the time for each request
- saved results into:
  - `response_times.csv`
  - `latency_histogram.png`


## Results

### ApacheBench Results
The ApacheBench output showed:
- overall throughput (requests per second)
- average latency
- system performance under concurrent load


### Histogram Analysis

The histogram shows:
- most requests completed quickly
- a small number of requests took significantly longer

This creates a **long tail distribution**.


## Conclusion

- The system handled most requests efficiently
- However, some requests experienced higher latency due to randomness
- This demonstrates why tail latency is important in distributed systems