#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_series = list()
    
    for n in range(length):
        if n == 0:
            fibonacci_series.insert(n, n)
        elif n == 1:
            fibonacci_series.insert(n, n)
        else:
            fibonacci_series.insert(n, (fibonacci_series[n-2] + fibonacci_series[n-1]))

    print(fibonacci_series) 
    return fibonacci_series