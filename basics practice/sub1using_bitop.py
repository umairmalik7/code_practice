num = int(input("Enter an integer: "))
def int_to_bits(n):
    return bin(n)[2:]  # Remove '0b' prefix

# Example usage
binary = int_to_bits(num)
print(f"Binary of {num} is {binary}")
