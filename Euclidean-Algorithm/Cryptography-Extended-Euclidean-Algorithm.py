# Extended Euclidean Algorithm - Python implementation

# Function for Extended Euclidean Algorithm
def extended_euclidean_algorithm(a, b):
    # base case
    if a == 0:
        return b, 0, 1
    gcd, x_1, y_1 = extended_euclidean_algorithm(b % a, a)
    # update x and y using results of recursive call
    x = y_1 - (b // a) * x_1
    y = x_1
    return gcd, x, y


# Driver code
if __name__ == "__main__":
    a, b = 35, 15
    g, x, y = extended_euclidean_algorithm(a, b)
    print("extended_euclidean_algorithm(", a, ",", b, ") = ", g)

    a, b = 10, 56
    g, x, y = extended_euclidean_algorithm(a, b)
    print("extended_euclidean_algorithm(", a, ",", b, ") = ", g)
