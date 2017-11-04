def is_prime(n):
    """Skills assessed: math, for loop"""

    # Get the sqrt of n, and remove decimals by converting to int
    m = int(n ** (.5))
    # Trial division up to m + 1 to accomodate 3
    for i in range(2, m + 1):
        # Fail fast
        if (n % i) == 0:
            return False
    return True


# if __name__ == '__main__':
#     is_prime(15);

