import random
from primality import primality

def generate_prime(min=0, max=10)->tuple:
    #random.seed(13)
    diff = max-min
    if min % 2 == 0:
        min += 1

    if max % 2 == 0:
        max += 1
    counter = 0
    random_number = random.randrange(min, max,2)
    while True:
        
    
        if primality.isprime(random_number):
            print(f"Prime {random_number} found at iteration {counter + 1}")
            return random_number
        
        random_number += 2
        counter += 1
        if counter == diff:
            print("Nothing found")
            return


'''Under: ChatGPT's solution'''
def fast_factor(n):
    # find the prime factors of n using trial division
    factors = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def gcd(a, b):
    # find the greatest common divisor of a and b using Euclid's algorithm
    while b:
        a, b = b, a%b
    return a
    
def find_generator(p):
    # find the prime factors of p-1
    factors = fast_factor(p-1)

    # check each number from 2 to p-1 for being a generator
    for g in range(2, p):
        # check if g is relatively prime to p-1
        if gcd(g, p-1) != 1:
            continue
        # check if g generates Z(p)
        is_generator = True
        for factor in factors:
            if pow(g, (p-1)//factor, p) == 1:
                is_generator = False
                break
        if is_generator:
            return g

    # no generator found
    return None


'''
import time
start = time.time()
prime = generate_prime(1,1000)
print(prime)
generator = find_generator(269)
stop = time.time()
print(f"Time elapsed finding generator {generator}: {stop-start}")'''

'''# Finds a (random) generator for Z(p)
def find_generator(prime):
    print(f"Finding generator for {prime}...")
    random.seed(4000)

    group = [x for x in range (1, prime)]
    generators = []
    for i in range(1, len(group)):
        res = []

        for j in range(len(group)):
            res.append(pow(i,j,prime))
            
        if sorted(res) == group:
            generators.append(i)
        if len(generators) > 10:
            break

    random_index = random.randrange(0, len(generators))
    print(f"Generator {generators[random_index]} found")
    return generators[random_index]
        
'''