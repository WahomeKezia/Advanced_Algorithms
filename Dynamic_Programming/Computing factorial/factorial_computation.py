'''1. Implement factorial computation using memoization. Test the program on n such that 4<= n < 1,000,00 

2. Implement factorial computation using tabulation technique (bottom up).  Test the program on n such that 4 <= n < 1,000,000

3. Identify the algorithm that works the best as the number gets big.'''

def factorial_memo(n, memo={}):
    # Check if the result for n is already in the memoization table
    if n in memo:
        return memo[n]
    
    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: calculate factorial and store result in memo table
    result = n * factorial_memo(n - 1, memo)
    memo[n] = result
    return result

def factorial_tabulation(n):
    # Create a table to store solutions to subproblems
    table = [0] * (n + 1)
    table[0] = 1
    
    # Fill in the table iteratively
    for i in range(1, n + 1):
        table[i] = i * table[i - 1]
    
    # Return the final result
    return table[n]

def main():
    # Test memoization
    print("Memoization:")
    for n in range(4, 10):
        print(f"Factorial of {n}: {factorial_memo(n)}")

    # Test tabulation
    print("\nTabulation:")
    for n in range(4, 10):
        print(f"Factorial of {n}: {factorial_tabulation(n)}")

    # Test performance for larger values of n
    n_values = [10**5, 10**6, 10**7]
    for n in n_values:
        start_time_memo = time.time()
        _ = factorial_memo(n)
        end_time_memo = time.time()
        print(f"Memoization - n = {n}, Time taken: {end_time_memo - start_time_memo:.6f} seconds")

        start_time_tabulation = time.time()
        _ = factorial_tabulation(n)
        end_time_tabulation = time.time()
        print(f"Tabulation - n = {n}, Time taken: {end_time_tabulation - start_time_tabulation:.6f} seconds")

if __name__ == "__main__":
    import time
    main()
