"""
test_benchmark.py
Tests for benchmarking utilities.
"""

from src.benchmark import measure_time
import time


def dummy_function():
    time.sleep(0.01)


def test_measure_time():
    result = measure_time(dummy_function, repeats=3)

    assert "min" in result
    assert "max" in result
    assert "avg" in result
    assert len(result["runs"]) == 3
    assert result["min"] > 0
