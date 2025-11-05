def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

def primes_up_to(limit: int) -> list[int]:
    """Return a list of all prime numbers up to the given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def greet(name,last_name):
    """Return a simple greeting."""
    return f"Hello, {name},{last_name}!"

def test_greet():
    assert greet("Alice","Johnson") == "Hello, Alice,Johnson!"
    assert greet("Bob","Brown") == "Hello, Bob,Brown!"
    

if __name__ == "__main__":
    print(greet("Ben","Smith"))

    print(is_prime(11))
    print(is_prime(4))
    print(primes_up_to(30))
