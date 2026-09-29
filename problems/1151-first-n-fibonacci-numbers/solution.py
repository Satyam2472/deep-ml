def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    
    if n == 0:
        return []

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    else:
        fib_series = first_n_fibonacci(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
