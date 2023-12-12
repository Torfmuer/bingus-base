### BINGUS DATABASE ###
### NETWORKS FINAL ###
### BY HUNTER WILLIAMS AND OWEN FOSTER ###

import socket

### Image option ###
def img_op(client_socket, img_option):
    with open(img_option + '.jpg', 'rb') as file:
        image_data = file.read()

        # Send image size
        image_size = len(image_data)
        client_socket.sendall(image_size.to_bytes(4, byteorder='big'))

        # Send image data
        client_socket.sendall(image_data)

        # Close connection with client
        client_socket.close()
        
# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
# May need some modifications for use on LAN
host = '127.0.0.1'
port = 50001

# Bind to port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

# Waiting for connections
while True:
    client_socket, addr = server_socket.accept()

    print("Got a connection from {}".format(addr))

    # Greeting
    serv_greet = "Hello welcome to Bingus Database, here you may download any and all Binguses that you want? \n Which bingus would you like? \n 1. Standard bingus {bingus} \n 2. Splorngus {splorngus} \n 3. Suit bingus {suit} \n 4. Bingus with belly full {fullbingus} \n 5. Dripped out bingus {drip} \n"
    client_socket.sendall(serv_greet.encode('utf-8'))
    
    # Grab the image option and send
    img_option = client_socket.recv(1024)
    img_op(client_socket,img_option.decode('utf-8'))
        
