#!/usr/bin/env python3

def is_palindrome(number):
    text = str(number);
    return text == text[::-1]; # Step backwards

def largest_palindrome(lower, upper):
    """Returns the largest palindrome between lower (inclusively) and upper (exclusively) """
    largest = 0;
    for i in range(lower, upper):
        for j in range(lower, upper):
            if (i * j > largest and is_palindrome(i * j)):
                largest = i * j;
    
    return largest;

print (largest_palindrome(100, 1000));
