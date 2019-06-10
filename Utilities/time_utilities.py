import time
import functools

global_list = list()
global_list.append(0.0)


def calculate_average_time(tries):
    print(f"Total amount of runs: {tries} AND first item in element is: {global_list[0]}")
    print(f"Average of entire run is: {global_list[0] / tries}")


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        global_list.insert(0, global_list[0] + run_time)
        return value
    return wrapper_timer
