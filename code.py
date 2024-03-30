import concurrent.futures
import time

def leibniz_gregory_partial(start, end):
    partial_sum = 0.0
    sign = 1
    for i in range(start, end):
        partial_sum += sign * 4.0 / (2 * i + 1)
        sign *= -1
    return partial_sum

def leibniz_gregory_multi_threaded(n, num_threads=4):
    chunk_size = n // num_threads

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(lambda x: leibniz_gregory_partial(x * chunk_size, (x + 1) * chunk_size), range(num_threads))

    # Sum the partial results
    pi_approx = sum(results)
    return pi_approx

def main():
    # Number of iterations for a more precise approximation
    iterations = int(input("Number of iterations: "))

    start_time = time.time()
    approx_pi = leibniz_gregory_multi_threaded(iterations)
    end_time = time.time()

    execution_time = end_time - start_time

    print(" --> Approximation of pi with {} iterations in {:.6f} seconds: {:.100f}".format(iterations, execution_time, approx_pi))

if __name__ == "__main__":
    main()
