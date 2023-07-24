# Cryptography - Algorithms

## AKS: Primality Test

### Implementation
Implementation of the AKS primality test algorithm in python. To test if a number n is prime, type `print(aks(n))`.

Example: `n=1009` $-->$ `print(aks(1009))`.

### Efficiency
Note that this implementation of the algorithm is not as efficient as it could be. This implementation will detect if a number is coprime pretty fast. Although, if it is a prime, it will take quite some time. The main bottleneck is the fastPoly function and, more specifically, the multi function. In  `fast_poly` we have to calculate (x+a)<sup>n</sup>, for multiple a. Currently, I am using fast modular exponentiation for polynomials to do this operation.
