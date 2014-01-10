Problem 004 - First Attempt (Programming solution)
=============
Finding the smallest number evenly divisible by 1 to 20 allows for some short cuts, the first thing I will do is find all of the prime factors of the numbers largest to smallest until all of the numbers that need to be checked are crossed off.

Numbers:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

20 => 5, 2, 2
19 => 19
18 => 2 * 3 * 3
17 => 17
16 => 2 * 2 * 2 * 2
15 => 3 * 5
14 => 7 * 2
13 => 13
12 => 3 * 2 * 2
11 => 11
10 => 5 * 2
9 => 3 * 3 * 3
8 => 2 * 2 * 2
7 => 7
6 => 3 * 2
5 => 5
4 => 2 * 2
3 => 3
2 => 2

The numbers 19, 17, 13, 11 can only be represented by checking if what we're checking is divisible by 19, 17, 13, and 11 so there is no shortcuts for those. So far we must check: [11, 13, 17, 19]

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ~~11~~, 12, ~~13~~, 14, 15, 16, ~~17~~, 18, ~~19~~, 20

Next I'll choose the largest numbers and cross off what they cover.

20 checks 2, 4, 5, 10, and 20

1, ~~2~~, 3, ~~4~~, ~~5~~, 6, 7, 8, 9, ~~10~~, ~~11~~, 12, ~~13~~, 14, 15, 16, ~~17~~, 18, ~~19~~, ~~20~~

18 checks 6, 9, and 18

1, ~~2~~, 3, ~~4~~, ~~5~~, ~~6~~, 7, 8, ~~9~~, ~~10~~, ~~11~~, 12, ~~13~~, 14, 15, 16, ~~17~~, ~~18~~, ~~19~~, ~~20~~

16 checks 2, 4, 8, and 16

1, ~~2~~, 3, ~~4~~, ~~5~~, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, ~~11~~, 12, ~~13~~, 14, 15, ~~16~~, ~~17~~, ~~18~~, ~~19~~, ~~20~~

15 checks 3, 5, and 15

1, ~~2~~, ~~3~~, ~~4~~, ~~5~~, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, ~~11~~, 12, ~~13~~, 14, ~~15~~, ~~16~~, ~~17~~, ~~18~~, ~~19~~, ~~20~~

14 checks 2, 7 and 14

1, ~~2~~, ~~3~~, ~~4~~, ~~5~~, ~~6~~, ~~7~~, ~~8~~, ~~9~~, ~~10~~, ~~11~~, 12, ~~13~~, ~~14~~, ~~15~~, ~~16~~, ~~17~~, ~~18~~, ~~19~~, ~~20~~

12 checks 2, 3, 4, 6, and 12

1, ~~2~~, ~~3~~, ~~4~~, ~~5~~, ~~6~~, ~~7~~, ~~8~~, ~~9~~, ~~10~~, ~~11~~, ~~12~~, ~~13~~, ~~14~~, ~~15~~, ~~16~~, ~~17~~, ~~18~~, ~~19~~, ~~20~~

So if we check [11, 13, 17, 19] (the primes) and [12, 14, 15, 16, 18, 20] we will have checked if the number is divisible by one to twenty, the entire list we need to check is:

[11, 12, 13, 14, 15, 16, 17, 18, 19, 20], which happens to be from 11 to 20 (both inclusively)

The code that this yielded was:

```
factors = range(11, 21);

number = -1;
current = 20; # Smallest number can be twenty
while number == -1:
    if all(current % factor == 0 for factor in factors):
        number = current;
    current += 1;
    if current % 1000 == 0:
        print(current);

print(number);
```

This took way too long to run, and I didn't bother to let it keep going, then I realized that because the answer needs to also be a multiple of 20 we can increment by 20 instead then I managed to get a solution in a reasonable amount of time

Problem 004 - Second Attempt (Right!)
=============
I wrote a quick program to find me all of the prime factors of each number 2-20 and I got
```
2 => [2]
3 => [3]
4 => [2, 2]
5 => [5]
6 => [2, 3]
7 => [7]
8 => [2, 2, 2]
9 => [3, 3]
10 => [2, 5]
11 => [11]
12 => [2, 2, 3]
13 => [13]
14 => [2, 7]
15 => [3, 5]
16 => [2, 2, 2, 2]
17 => [17]
18 => [2, 3, 3]
19 => [19]
20 => [2, 2, 5]
```

Now we take out the primes from earlier,

```
2 => [2]
3 => [3]
4 => [2, 2]
5 => [5]
6 => [2, 3]
7 => [7]
8 => [2, 2, 2]
9 => [3, 3]
10 => [2, 5]
12 => [2, 2, 3]
14 => [2, 7]
15 => [3, 5]
16 => [2, 2, 2, 2]
18 => [2, 3, 3]
20 => [2, 2, 5]
```

Now we need to go from the lowest number to the highest number, adding any factors its missing, for example from 2 to 3 we're missing both a 2 and 3 so now we have 2 * 3, going from 3 to 4 we're missing only one 2 so now we have 2 * 2 * 3

The final result of this process is: 

2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19  = 232792560
