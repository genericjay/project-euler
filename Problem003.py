#!/usr/bin/env python3
import math;

primes = [2, 3, 5, 7, 11, 13];

def is_prime(number):
    if number in primes:
        return True;
    
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if (number % i == 0):
            return False;
    return True;

def max_factor(number):
    """Determines the largest prime factor of the given number"""
    largest = 0;
    i = 2;
    while i <= number:
        if number % i == 0:
            number /= i;
            if i > largest and is_prime(i): # the current i will always be greater than or equal to largest, if i is the same we can skip it though
                largest = i;
        else: # i may be divisible by the same number multiple times, so we only increment if we haven't found a prime
            i += 1;
    return largest;

#Testing some sample data from the problem description
assert(is_prime(2));
assert(is_prime(7));
assert(is_prime(13));
assert(is_prime(29));

assert(not is_prime(6));
assert(not is_prime(12));


assert(max_factor(10) == 5);
assert(max_factor(13195) == 29);

# Print answer

print (max_factor(600851475143));