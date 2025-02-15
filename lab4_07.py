import math

def calculate_nCr(n, r):
    return math.comb(n, r)

def calculate_nPr(n, r):
    return math.perm(n, r)

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

nCr = calculate_nCr(n, r)
nPr = calculate_nPr(n, r)

print(f"{n}C{r} (nCr) = {nCr}")
print(f"{n}P{r} (nPr) = {nPr}")

