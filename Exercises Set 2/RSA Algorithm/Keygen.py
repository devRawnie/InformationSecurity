import random
from math import gcd
class Primality:
    def __init__(self, num=None):
        if num is None:
            raise Exception("Invalid number entered")
        if num % 2 == 0:
            self.is_prime = False
        else:
            temp = num-1
            self.n = 0
            while temp % 2 == 0:
                temp //= 2
                self.n += 1
            self.r = temp
    
    def test(self, a):
        if not self.is_prime: 
            return False
        

    @staticmethod
    def miller_rabin(num):
        # Step 1: Find n
        mr_test = Primality(num)
        # Hardcoding value of s = 12
        for i in range(1,13):
            a = random.randint(2, num-2)
            if not mr_test.test(a):
                return False
        return True



class Keygen:
    @staticmethod
    def get_prime(size=256):
        n = random.randint(2**250, 2**size)
        # Check for primality of n using probabilistic measure
        if not Primality.miller_rabin(n):
            return Keygen.get_prime()
        return n

    @staticmethod
    def find_modulo_inverse(a, m):
        return 1

    @staticmethod
    def generate_key(i):
        n1 = 17
        n2 = 11
        n = n1*n2
        phi  = (n1-1)*(n2-1)
        e = None
        d = None
        for i in range(phi):
            if i != n1 and i != n2:
                if gcd(phi, i) == 1:
                    e = i
                    break
        if e is not None:
            d = Keygen.find_modulo_inverse(e, phi)
        else:
            return Keygen.generate_key(i)
        return {"pub":(e,n), "pri":(d,n)}
    
def generate_keys(n=1):
    keys = {}
    for i in range(n):
        keys[i] = Keygen.generate_key(i)

    return keys
        

Keygen.miller_rabin(229)