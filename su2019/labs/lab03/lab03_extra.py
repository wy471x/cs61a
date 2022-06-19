""" Optional problems for Lab 3 """

def prime_helper(divisor, n):
    if divisor == n:
        return True
    if not (n % divisor):
        return False
    return prime_helper(divisor + 1, n)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    divisor = 2
    return prime_helper(divisor, n)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    smaller, larger = min(a, b), max(a, b)
    if larger % smaller == 0:
        return smaller
    else:
        return gcd(smaller, larger % smaller)

def ten_pairs_helper(digit, n):
    count = 0
    while n > 0:
        if digit == n % 10:
            count += 1
        n //= 10
    return count

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    digit = n % 10
    return ten_pairs_helper(10 - digit, n // 10) + ten_pairs(n // 10)

