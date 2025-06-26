import socket

try:
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # DGRAM --> Datagram (UDP)

    print("Socket created")
    ip_add = "192.168.169.180"
    port = 45678
    target_add = (ip_add, port)
    message = input("enter the message:")
    encoding_msg = message.encode('ascii')
    s.sendto(encoding_msg , target_add)
    print("Message sent successfully")
    s.close()

except socket.error as err:
    print("Socket creation failed with error %s" %(err))

    

