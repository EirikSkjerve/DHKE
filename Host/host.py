from utils import generate_prime, find_generator
import socket
import time

'''Generates a prime P and a generator for the finite group Z(p) 
    (group of all remainders (except 0) of division with p)'''
def generate_p_g(max_prime):
        prime = generate_prime(max_prime//2, max_prime)
        gen = find_generator(prime)
        return f"{prime} {gen}"

def broadcast(clients, message):
     for c, addr in clients:
          print(f"Sending {message} to {addr}")
          c.send(message.encode())

def send_to_client(client, message):
     
     c, addr = client
     print(f"Sending {message} to {addr}")
     c.send(message.encode())

def recieve_from_client(client):
     c, addr = client
     message = c.recv(1024).decode()
     print(f"Recieving {message} from {addr}")
     return message

host = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
HOST = "192.168.1.177"
PORT = 65432

host.bind((HOST, PORT))

clients = []
while len(clients) < 2:
    host.listen()
    c, addr = host.accept()
    clients.append((c, addr))
    
    print(f"Connection recieved from {addr}")

#generate P and g
print("Generating Prime and Generator...")
start = time.time()
P_g = generate_p_g(2**66)
end = time.time()
print(f"Prime and generator generated after {end-start} s")

broadcast(clients, P_g)

A = recieve_from_client(clients[0])
B = recieve_from_client(clients[1])
send_to_client(clients[1], A)
send_to_client(clients[0], B)

host.close()

'''
if __name__ == "__main__":
    import time 
    start = time.time()
    bit_size = 17


    
    # Client objects is to be created at clients side
    Alice = Client("Alice")
    Bob = Client("Bob")

    #Public space
    Pub_generator = P_G_Generator(pow(2,bit_size))

    # generate P and g
    P, g = Pub_generator.generate_p_g()

    # P and g is to be sent to the clients
    Alice.init_p_g(P, g)
    Bob.init_p_g(P, g)

    # clients choose small a 
    Alice.choose_small_a()
    Bob.choose_small_a()

    # host recieves big A and B
    A = Alice.generate_big_A()
    B = Bob.generate_big_A()

    # send clients B and A
    Alice_key = Alice.generate_key(B)
    Bob_key = Bob.generate_key(A)

    print(f"Alice's key : {Alice_key} \nBob's key : {Bob_key}")
    end = time.time()
    print(f"Elapsed time generating key with size 2^{bit_size}: {round(end-start, 3)} s")
    '''