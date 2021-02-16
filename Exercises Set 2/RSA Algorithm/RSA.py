import random
from math import gcd

class Primality:
    is_even = False
    def __init__(self, num=None):
        if num is None:
            raise Exception("Invalid number entered")
        if num % 2 == 0:
            self.is_even = True
        else:
            self.num = num
            self.r = 0
            self.d = num-1
            while self.d % 2 == 0:
                self.d //= 2
                self.r += 1
    
    def test(self, a):
        if self.is_even: 
            return False
        result = RSA.fast_exponentiation(a, self.d, self.num)
        if result != 1 or result != self.num - 1:
            return False
        for i in range(1,self.s):
            result = (result**2) % self.num
            if result == self.num-1:
                return False
        return True


    @staticmethod
    def miller_rabin(num):
        # Step 1: Find n
        mr_test = Primality(num)
        # Hardcoding value of s = 12
        for i in range(1,13):
            a = random.randint(2, num-2)
            if not mr_test.test(a):
                print("a: {}".format(a))
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
class RSA:
    def generate_key_pool(self):
        names = ["Alice", "Bob", "Janice"]
        pool = {}
        self.users = {}
        keys = generate_keys(len(names))
        for i in range(len(names)):
            user = User(names[i], keys[i]["pri"], keys[i]["pub"])
            pool[names[i]] = user.key
            self.users[names[i]] = user

        return pool

    @staticmethod
    def encrypt(text, key):
        e, n = key
        output = []
        for char in text:
            temp = RSA.fast_exponentiation(ord(char), e, n)    
            output.append(temp)

        return ":".join(map(str, output))
    
    @staticmethod
    def decrypt(text, key):
        cipher = list(map(int, text.split(":")))
        d, n = key
        output = []
        for val in cipher:
            temp = RSA.fast_exponentiation(val, d, n)    
            output.append(chr(temp))

        return "".join(output)

    @staticmethod
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

class User:
    def __init__(self, id=None,name=None, k_pri=None, k_pub=None):
        if id is None or id < 1:
            raise Exception("Invalid Id argument")
        self.id = id

        if name is None:
            raise Exception("Invalid name argument")
        self.name = name
        
        if k_pri is None:
            raise Exception("Invalid Private Key argument")
        self.k_pri = k_pri

        if k_pub is None:
            raise Exception("Invalid Public Key argument")
        self.k_pub = k_pub
    
    @property
    def key(self):
        return self.k_pub

    def __str__(self):
        return "ID: {}\nName: {}\nPublic Key: {}".format(self.id, self.name, self.k_pub)

