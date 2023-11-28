"""copyright 2023 Bill Erhard"""

import argparse
import time


def dumb_sum(start: int = 1, stop: int = 10):
    """sums linear for loop"""
    result = 0
    for i in range(start, stop + 1):
        result += i
    return result


def smarter_sum(start: int = 1, stop: int = 10):
    """sum algorithm"""
    first = (start - 1 * (start)) / 2
    last = (stop * (stop + 1)) / 2
    return last - first


def table_sum(start: int = 1, stop: int = 10):
    """if it's in the table..."""
    one_to_x = {
        "1": 1,
        "2": 3,
        "3": 6,
        "4": 10,
        "5": 15,
        "6": 21,
        "7": 28,
        "8": 36,
        "9": 45,
        "10": 55,
        "100": 5050,
        "1000": 500500,
        "10000": 50005000,
        "100000": 5000050000,
        "1000000": 500000500000,
        "10000000": 500000500000,
        "100000000": 50000005000000,
        "1000000000": 5000000050000000,
    }
    if start == 1 and str(stop) in one_to_x.keys():
        return one_to_x[str(stop)]
    return "dunno"


def main(start: int = 1, stop: int = 10):
    """main..."""

    start_time = time.perf_counter_ns()
    ans = dumb_sum(start, stop)
    runtime = time.perf_counter_ns() - start_time
    print(f"Runtime = {runtime} ns, answer = {ans}")

    start_time = time.perf_counter_ns()
    ans = smarter_sum(start, stop)
    runtime = time.perf_counter_ns() - start_time
    print(f"Runtime = {runtime} ns, answer = {ans}")

    start_time = time.perf_counter_ns()
    ans = table_sum(start, stop)
    runtime = time.perf_counter_ns() - start_time
    print(f"Runtime = {runtime} ns, answer = {ans}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="code golf for sums")
    parser.add_argument("start", type=int, default=1)
    parser.add_argument("stop", type=int, default=10)
    args = parser.parse_args()
    main(start=args.start, stop=args.stop)
