import time


def benchmark(f, print_args, print_res, *fargs):
    # Run function with arguments and record time
    time_start = time.time_ns()
    (res, (num_iter, num_ints)) = f(*fargs)
    time_elapsed = (time.time_ns() - time_start) / 1e6
    # Print results
    print(f'{f.__name__}', end='')
    
    if print_args:
        print(f'{fargs}', end='')

    if print_res:
        print(f' = {res}', end='')

    print(f'{time_elapsed};{num_iter};{num_ints}')
    return res


if __name__ == "__main__":
    benchmark(lambda x: (x + 1, 1), True, True, 2)
