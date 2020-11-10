'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

import math

# Sieve of Eratosthenes Algorithm and For Loop

class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for i in range(n):
            if primes[i]:
                for j in range(i*i, n, i):
                    if j <= n:
                        primes[j] = False
                        
        return sum(primes)


# Sieve of Eratosthenes Algorithm and While Loop

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True for i in range(n)]
        isPrime[0] = isPrime[1] = False
        i = 2
        while n > i*i:
            if isPrime[i]:
                j = 2
                while i * j < n:
                    isPrime[i*j] = False
                    j += 1
            i += 1
        return sum(isPrime)

# Sieve of Eratosthenes Algorithm For Loop and in-built math functions

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True for i in range(n)]
        isPrime[0] = isPrime[1] = False
        for i in range(2, math.ceil(math.sqrt(n))):
            if isPrime[i]:
                for multiples in range(i*i, n, i):
                    isPrime[multiples] = False
        return sum(isPrime)

# Check Custom Input

s = Solution()
answer = s.countPrimes(12) # (2, 3, 5, 7, 11) => 5
print(answer)