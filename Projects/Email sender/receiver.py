import socket
try:
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created")
    ip_add = "192.168.169.180"
    port = 45678
    complete_add = (ip_add, port)
    s.bind(complete_add)

    while True:
        message , sender_address = s.recvfrom(1024)

        print("raw message:", message)
        print("sender address:", sender_address)

        decoded_message = message.decode('ascii')
        print("decoded message:", decoded_message)

except Exception as e:
    print("as error occured", e)
