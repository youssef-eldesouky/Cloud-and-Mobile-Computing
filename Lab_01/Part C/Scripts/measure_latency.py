import csv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import matplotlib.pyplot as plt
import requests

URL = "http://localhost:5000/"
TOTAL_REQUESTS = 100
CONCURRENCY = 10

RESULTS_DIR = Path("lab-01/part-c/results")
CSV_PATH = RESULTS_DIR / "response_times.csv"
PNG_PATH = RESULTS_DIR / "latency_histogram.png"


def fetch_one(request_id: int):
    start = time.perf_counter()
    try:
        response = requests.get(URL, timeout=30)
        status_code = response.status_code
        ok = True
    except Exception:
        status_code = None
        ok = False
    elapsed = time.perf_counter() - start
    return {
        "request_id": request_id,
        "elapsed_seconds": elapsed,
        "status_code": status_code,
        "ok": ok,
    }


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(fetch_one, i + 1) for i in range(TOTAL_REQUESTS)]
        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda x: x["request_id"])

    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["request_id", "elapsed_seconds", "status_code", "ok"],
        )
        writer.writeheader()
        writer.writerows(results)

    response_times = [r["elapsed_seconds"] for r in results if r["ok"]]

    plt.figure(figsize=(10, 6))
    plt.hist(response_times, bins=20)
    plt.title("Response Time Histogram")
    plt.xlabel("Response time (seconds)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(PNG_PATH, dpi=150)

    print(f"Saved CSV to {CSV_PATH}")
    print(f"Saved histogram to {PNG_PATH}")
    print(f"Collected {len(response_times)} successful response times")


if __name__ == "__main__":
    main()