# Basic Euclidean Algorithm - Python implementation

# Function to return GCD (Greatest Common Divisor) of a and b
def basic_euclidean_algorithm(a, b):
    if a == 0:
        return b
    return basic_euclidean_algorithm(b % a, a)


# Driver code
if __name__ == "__main__":
    a = 10
    b = 15
    print("basic_euclidean_algorithm(", a,",", b, ") = ", basic_euclidean_algorithm(a, b))

    a = 35
    b = 10
    print("basic_euclidean_algorithm(", a, ",", b, ") = ", basic_euclidean_algorithm(a, b))

    a = 31
    b = 2
    print("basic_euclidean_algorithm(", a, ",", b, ") = ", basic_euclidean_algorithm(a, b))
