from utils import generate_prime, find_generator
import random
from rich import print

class Client:
    def __init__(self, name, prime, generator) -> None:
        self.name = name
        self.prime = prime 
        self.generator = generator

    def choose_small_a(self):
        print(f"{self.name} choosing private number...\n")

        self.small_a = random.randrange(2, self.prime-2)

    def generate_big_A(self):
        print(f"{self.name} generating big number...\n")
        big_A = pow(self.generator, self.small_a, self.prime)
        return big_A
    
    def generate_key(self, other_party_pre_key = 3):
        print(f"{self.name} generating the key...\n")
        KEY = pow(other_party_pre_key, self.small_a, self.prime)
        return KEY

class P_G_Generator:
    def __init__(self, max_prime):
        self.max_prime = max_prime

    def generate_p_g(self):
        prime = generate_prime(self.max_prime//2, self.max_prime)
        gen = find_generator(prime)
        return prime, gen

if __name__ == "__main__":
    import time 
    start = time.time()
    bit_size = 18

    #Public space
    Pub_generator = P_G_Generator(pow(2,bit_size))
    P, g = Pub_generator.generate_p_g()

    Alice = Client("Alice", P, g)

    Alice.choose_small_a()
    A = Alice.generate_big_A()

    Bob = Client("Bob", P, g)

    Bob.choose_small_a()
    B = Bob.generate_big_A()


    Alice_key = Alice.generate_key(B)

    Bob_key = Bob.generate_key(A)

    print(f"Alice's key : {Alice_key} \nBob's key : {Bob_key}")
    end = time.time()
    print(f"Elapsed time generating key size 2^{bit_size}: {round(end-start, 3)} s")

