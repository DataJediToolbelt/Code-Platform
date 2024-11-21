import socket

def hl7_client():
    # https://www.ascii-code.com/
    # 0B - Data - 1C0D
    # Define the encapsulation values to add
    value_to_add_front = 0x0B
    value_to_add_end1 = 0x1C
    value_to_add_end2 = 0x0D
    # Data
    data = "MSH|^~\&||COCAT|||201504300031||ADT^A08|ATGTADM.1.13881160|P|2.1" + chr(0x0D)
    # Add the value
    complete_data = chr(value_to_add_front) + data + chr(value_to_add_end1) + chr(value_to_add_end2)
    complete_data_encoded = complete_data.encode()
    # Print the result
    print(f"Result: {(complete_data)}")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10125)  # Replace with your server's IP and port
    client_socket.connect(server_address)
    client_socket.send(complete_data_encoded)