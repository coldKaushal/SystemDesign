import time

# Initialize a large and a small cache

small_cache = {}


def large_cache_replacement_test():
    large_cache = {}
    for i in range(10**6):
        large_cache[i] = i
    time_start = time.time()
    large_cache.get(10**6, 0)
    time_end = time.time()
    return time_end - time_start


def small_cache_replacement_test():
    for i in range(10**3):
        small_cache[i] = i
    time_start = time.time()
    small_cache.get(10**6, 0)
    time_end = time.time()
    return time_end - time_start


# Determine cache performance
large_cache_replacement_time = large_cache_replacement_test()
small_cache_replacement_time = small_cache_replacement_test()

# Compare both cache simulations
print("Large Cache Replacement Time: ", large_cache_replacement_time)
print("Small Cache Replacement Time: ", small_cache_replacement_time)