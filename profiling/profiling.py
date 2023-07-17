# Bron:
# https://realpython.com/python-profiling/

#%%
# Timer for profiling

import time

def sleeper():
    time.sleep(1.75)


def spinlock():
    for _ in range(100_000_000):
        pass


for function in sleeper, spinlock:
    t1 = time.perf_counter(), time.process_time()
    function()
    t2 = time.perf_counter(), time.process_time()
    print(f"{function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
    print()

#%%

from timeit import timeit

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


iterations = 100
total_time = timeit("fib(30)", number=iterations, globals=globals())

f"Average time is {total_time / iterations:.2f} seconds"

#%%

from cProfile import Profile
from pstats import SortKey, Stats

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


with Profile() as profile:
    print(f"{fib(35) = }")
    (
        Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.CALLS)
        .print_stats()
    )

#%%


from random import uniform

def estimate_pi(n):
    return 4 * sum(hits(point()) for _ in range(n)) / n


def hits(point):
    return abs(point) <= 1


def point():
    return complex(uniform(0, 1), uniform(0, 1))


for exponent in range(1, 8):
    n = 10 ** exponent
    estimates = [estimate_pi(n) for _ in range(5)]
    print(f"{n = :<10,} {estimates}")


#%%

from pyinstrument import Profiler
with Profiler(interval=0.1) as profiler:
    estimate_pi(n=10_000_000)



profiler.print()



#%%

# profile_perf.py

from concurrent.futures import ThreadPoolExecutor

def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def slow_function():
    print("Slow thread started")
    try:
        return find_divisors(100_000_000)
    finally:
        print("Slow thread ended")

def fast_function():
    print("Fast thread started")
    try:
        return find_divisors(50_000_000)
    finally:
        print("Fast thread ended")

def main():
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(slow_function)
        pool.submit(fast_function)

    print("Main thread ended")

if __name__ == "__main__":
    main()



# %%
