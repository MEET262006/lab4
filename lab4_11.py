import math

def calculate_sin(x, n_terms=4):
    sin_x = 0
    for i in range(n_terms):
        sign = (-1) ** i
        term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sin_x += sign * term
    return sin_x

x = float(input("Enter the radian value: "))
n_terms = int(input("Enter the number of terms (default=4): ") or 4)

calculated_sin = calculate_sin(x, n_terms)
print(f"Calculated sin({x}) = {calculated_sin}")

# Compare with math library's sin function
math_sin = math.sin(x)
print(f"math.sin({x}) = {math_sin}")
