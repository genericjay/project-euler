#!/usr/bin/env python3



def fib(limit):
    """Return the sum of all fib numbers explicitly beneath the given limit"""
    sum = 0;
    
    current = 0; # 1st term will be one
    old = 1;
    while current < limit:
        old_current = current; # backup current
        
        current = current + old;
        
        if current % 2 == 0:
            sum += current;
        
        old = old_current;
        
    return sum;

print(fib(4000000));