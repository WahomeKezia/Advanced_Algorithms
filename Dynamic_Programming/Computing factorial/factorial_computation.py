import sys
import timeit

def factorial_memo(n, memo={}):
    """
    Compute the factorial of a number using memoization.

    Parameters:
    - n: The input number.
    - memo: A dictionary to store memoized results.

    Returns:
    The factorial of the input number.
    """
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    result = n * factorial_memo(n - 1, memo)
    memo[n] = result
    return result

def factorial_tabulation(n):
    """
    Compute the factorial of a number using tabulation (bottom-up).

    Parameters:
    - n: The input number.

    Returns:
    The factorial of the input number.
    """
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(1, n + 1):
        table[i] = i * table[i - 1]
    return table[n]

def test_performance():
    n_values = [10, 100, 1000, 10000 , 10**5 , 10**6, 10**7 , 10**8]  # Adjust these values as needed

    print("Memoization:")
    for n in n_values:
        try:
            sys.setrecursionlimit(10**6)  # Set a higher recursion limit
            time_taken = timeit.timeit(lambda: factorial_memo(n), number=1000) / 1000
            print(f"n = {n}, Time taken: {time_taken:.9f} seconds")
        except RecursionError as e:
            print(f"Memoization - n = {n}, RecursionError: {e}")

    print("\nTabulation:")
    for n in n_values:
        try:
            start_time = timeit.default_timer()
            factorial_tabulation(n)
            time_taken = timeit.default_timer() - start_time
            print(f"n = {n}, Time taken: {time_taken:.9f} seconds")
        except Exception as e:
            print(f"Tabulation - n = {n}, Error: {e}")

if __name__ == "__main__":
    test_performance()