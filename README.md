# Cryptography - Algorithms

In this repository contains cryptography algorithms. In the following, some details about the most complex ones.

## AKS: Primality Test

### Implementation
Implementation of the AKS primality test algorithm in python. To test if a number n is prime, type `print(aks(n))`.

Example: `n=1009` ⟶ `print(aks(1009))`.

### Efficiency
Note that this implementation of the algorithm is not as efficient as it could be. This implementation will detect if a number is coprime pretty fast. Although, if it is a prime, it will take quite some time. The main bottleneck is the fastPoly function and, more specifically, the multi function. In  `fast_poly` we have to calculate $(x+a)^{n}$, for multiple a. Currently, we are using fast modular exponentiation for polynomials to do this operation.

## Quadratic Sieve

It is mainly used to factor very large numbers (**10** digits or more) depending on the sieve interval. The algorithm is single-polynomial version. It factors an integer N, using a chosen factor base of P primes, and a sieve interval. Run `main.py` to begin the execution.
