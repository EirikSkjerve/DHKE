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
'''
import time
start = time.time()
prime = generate_prime(min=2**512, max=2**513)
stop = time.time()
print(f"Time elapsed finding prime {prime}: {stop-start}")'''

'''Finds a (random) generator for Z(p)'''
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
    return generators[random_index]
        
