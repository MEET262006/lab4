def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect."""
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_armstrong(n):
    """Check if a number is Armstrong."""
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

def is_palindrome(n):
    """Check if a number is palindrome."""
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    """Check if a number is automorphic."""
    square = n ** 2
    return str(n) == str(square)[-len(str(n)):]

def main():
    num = int(input("Enter a number: "))

    print(f"Is {num} prime? {is_prime(num)}")
    print(f"Is {num} perfect? {is_perfect(num)}")
    print(f"Is {num} Armstrong? {is_armstrong(num)}")
    print(f"Is {num} palindrome? {is_palindrome(num)}")
    print(f"Is {num} automorphic? {is_automorphic(num)}")

if __name__ == "__main__":
    main()

