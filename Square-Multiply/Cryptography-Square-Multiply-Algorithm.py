# Square & Multiply Algorithm - Python implementation

x = int(input("Enter x: "))  # base
e = int(input("Enter e: "))  # exponent
m = int(input("Enter m: "))  # modulus

init_x = x

# get the bit representation of the exponent e
bits = [(e >> bit) & 1 for bit in range(e.bit_length() - 1, -1, -1)]
print(f"Exponent {e} in binary representation = {str(bin(e))[2:]}")
del bits[0]  # first bit is not needed for SQ&MUL -> delete it

# create a readable output table
print("Bit \t Operation \t Calculation (mod " + str(m) + ") ")

# one step per bit6
for bit in bits:
    x_alt = x
    x = pow(x, 2, m)  # calculates x^{2} mod m
    # if the bit was a 1, we also need to multiply x^{2} with x
    if bit == 1:
        x = x * init_x
        x = x % m
        print(str(bit) + "\t\t SQ&MUL" + "\t\t x^{2} * x = " + str(x_alt) + "^{2} * " + str(init_x) + " = " + str(x))
    else:
        print(str(bit) + "\t\t SQ" + "\t\t x^{2} = " + str(x_alt) + "^{2} = " + str(x))
