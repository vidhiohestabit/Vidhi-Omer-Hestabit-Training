def generate_primes(n):
    """
    Generate prime numbers between 1 to n.

    Args:
        n (int): Upper limit for prime number generation.

    Returns:
        list: A list of prime numbers.
    """
    # Initialize an empty list to store prime numbers
    primes = []
    
    # Iterate through each number between 1 and n
    for num in range(1, n + 1):
        # Check if the number is greater than 1 (prime numbers are greater than 1)
        if num > 1:
            # Assume the number is prime until proven otherwise
            is_prime = True
            
            # Check divisibility from 2 to the square root of num
            for i in range(2, int(num ** 0.5) + 1):
                # If num is divisible by any number in this range, it's not a prime number
                if num % i == 0:
                    is_prime = False
                    break
            
            # If num is still considered prime, add it to the list of primes
            if is_prime:
                primes.append(num)
    
    # Return the list of prime numbers
    return primes

# Example usage
n = 100
primes = generate_primes(n)
print("Prime numbers between 1 to", n, "are:")
print(primes)

# Print the time complexity of the algorithm
print("Time complexity: O(n*sqrt(n))")