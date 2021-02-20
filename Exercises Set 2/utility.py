import random
from math import sqrt

def miller_rabin(num):
    # Find d in d*2^r
    r = 0
    d = num-1
    while d % 2 == 0:
        d //= 2
        r += 1
    a = random.randint(2, num-2)

    result = fast_exponentiation(a, d, num)
    if result == 1 or result == num-1:
        # return prime
        return True

    while d != num-1:
        result = (result*result) % num
        d *= 2
        if result == 1:
            # return composite
            return False
        if result == num-1:
            # return prime
            return True
    
    # return composite
    return False

def fast_exponentiation(base, exp, n):
    """
        Iteratively finds the result of the expression base^exp mod n
    """
    bin_exp = bin(exp)[2:]
    output = 1
    for i in bin_exp:
        output = (output ** 2) % n
        if i == "1":
            output = (output*base) % n
    return output

def get_prime(start=200, end=250):
    # Check for primality of n using probabilistic measure
    n = random.randint(2**start, 2**end)
    while n % 2 == 0:
        n = random.randint(2**start, 2**end)
    if not miller_rabin(n):
        return get_prime(start, end)
    return n

def gcdExtended(a, b):
    if a == 0:
        return b,0,1
    else:
        gcd, x1, y1 = gcdExtended(b % a ,a)
        x = y1 - (b//a) * x1
        y = x1
        return gcd, x, y

def find_modulo_inverse(a, m):
    gcd, inv, __ = gcdExtended(a, m)
    if gcd != 1:
        return None
    else:
        #Handle negatives
        result = (inv % m + m) % m
        return result

def find_root(n):
    phi = n-1
    factors = findPrimeFactors(phi)
    for r in range(2, phi + 1):
        # Iterate through all prime factors of phi.  
        # and check if we found a power with value 1  
        flag = False
        for it in factors:  

            # Check if r^((phi)/primefactors) 
            # mod n is 1 or not  
            if (fast_exponentiation(r, phi // it, n) == 1):  

                flag = True
                break
            
        # If there was no power with value 1.  
        if (flag == False): 
            return r  

    # If no primitive root found  
    return None

def findPrimeFactors(n): 
    s = set()
    # Print the number of 2s that divide n  
    while (n % 2 == 0) : 
        s.add(2)
        n = n // 2

    # n must be odd at this po. So we can   
    # skip one element (Note i = i +2)  
    for i in range(3, int(sqrt(n)), 2):             
        # While i divides n, print i and divide n  
        while (n % i == 0) :     
            s.add(i)  
            n = n // i
        
    # This condition is to handle the case  
    # when n is a prime number greater than 2  
    if (n > 2) : 
        s.add(n)  
    return s