import random
from rich import print
import socket

class Client:
    def __init__(self, name) -> None:
        self.name = name

    def init_p_g(self, prime, generator):
        self.prime = prime
        self.generator = generator

    def choose_small_a(self):
        print(f"{self.name} choosing private number... \n")
        self.small_a = random.randrange(2, self.prime-2)
        print(f"Secret unique number: {self.small_a}")

    def generate_big_A(self):
        print(f"{self.name} generating big number... \n")
        big_A = pow(self.generator, self.small_a, self.prime)
        return big_A
    
    def generate_key(self, other_party_pre_key = 3):
        print(f"{self.name} generating the key...\n")
        KEY = pow(other_party_pre_key, self.small_a, self.prime)
        return KEY


if __name__ == "__main__":
    #HOST = "127.0.0.1"
    HOST = input("Hostname here:\n")
    PORT = 65432

    client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

    client.connect((HOST, PORT))
    #username = input("Welcome to a diffie hellman key exchange. What is your name? \nType it here please: ")
    username = "USER"
    User = Client(username)
    print("Please hold while your prime and generator is being generated... \n")
    data = client.recv(1024).decode()
    data = data.split()
    prime, generator = int(data[0]), int(data[1])

    print(f"Prime: {prime}, generator {generator}")
    User.init_p_g(prime, generator)

    User.choose_small_a()
    big_A = User.generate_big_A()
    client.send(str(big_A).encode())

    big_B = int(client.recv(1024).decode())
    KEY = User.generate_key(big_B)

    print(f"Key is: {KEY}")



    client.close()
    