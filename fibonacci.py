def fibonacci(n):
    """
    Calculate the nth Fibonacci number using memoization.
    
    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The nth Fibonacci number.
    """
    memo = {}

    def fib_helper(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib_helper(n - 1) + fib_helper(n - 2)
        return memo[n]

    return fib_helper(n)

# 👇 Call the function
print(f"The 10th Fibonacci number is {fibonacci(10)}")
