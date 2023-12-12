### BINGUS DATABASE ###
### NETWORKS FINAL ###
### BY HUNTER WILLIAMS AND OWEN FOSTER ###

import socket

# Main function, send 
def grab_image(ip):
    # Initialize 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ip
    port = 50001

    # Connect to server
    client_socket.connect((host, port))

    # Receive greeting and send image option
    print(client_socket.recv(1024).decode('utf-8'))
    print('input image option: ')
    img_op = input()
    while img_op not in ["bingus","drip","fullbingus","splorngus","suit"]:
        print("~ Please make sure your choice is valid! ~")
        img_op = input()
    client_socket.send(img_op.encode('utf-8'))
    
    # Receive image size first
    image_size_bytes = client_socket.recv(4)
    image_size = int.from_bytes(image_size_bytes, byteorder='big')

    # Receive image data
    image_data = b''

    while len(image_data) < image_size:
        packet = client_socket.recv(image_size - len(image_data))
        if not packet:
            break
        image_data += packet

    # Write received image data to file
    with open('received_bingus.jpg', 'wb') as file:
        file.write(image_data)

    print("~Image received and saved~")

    # Close connection with server
    client_socket.close()

# MAIN
print("~~~Bingus Database client app~~~\nq - Quit c - connect\n")
while True:
    client_in = input()
    if client_in == 'q':
        break
    elif client_in == 'c':
        grab_image('127.0.0.1') #### EDIT THIS STRING WITH CORRECT IP ####
        print("~ Anything else? (q to quit) (c to connect again!)~")
    else:
        print("~~~InVaLId coMmAnD~~~")
