"""
benchmark.py
Performance benchmarking utilities for classical and post-quantum algorithms.
"""

import time
from typing import Callable, Dict


def measure_time(func: Callable, *args, repeats: int = 10, **kwargs) -> Dict:
    """
    Benchmark a function by running it multiple times.

    Returns:
        {
            "min": ...,
            "max": ...,
            "avg": ...,
            "runs": [...]
        }
    """
    results = []

    for _ in range(repeats):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        results.append(end - start)

    return {
        "min": min(results),
        "max": max(results),
        "avg": sum(results) / len(results),
        "runs": results,
    }


def print_benchmark_result(name: str, data: Dict):
    """Nicely format printed benchmark results."""
    print(f"\n=== Benchmark: {name} ===")
    print(f"Min Time: {data['min']:.6f} sec")
    print(f"Max Time: {data['max']:.6f} sec")
    print(f"Avg Time: {data['avg']:.6f} sec")
    print(f"Runs: {len(data['runs'])}")
