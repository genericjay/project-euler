#!/usr/bin/env python3

sum = 0;

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        sum += n;

print(sum);