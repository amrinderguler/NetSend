import socket

def receive_file():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()

    print("Server is listening...")
    client, addr = server.accept()

    print(f"Accepted connection from {addr}")

    file_name = client.recv(1024).decode('utf-8')
    file_size = client.recv(1024).decode('utf-8')

    try:
        file_size = int(file_size)
    except ValueError:
        print(f"Error: Received invalid file size: {file_size}")

    print(f"Receiving file: {file_name}")
    print(f"File size: {file_size} bytes")

    with open(file_name, "wb") as file:
        for _ in range(file_size):
            bytes_read = client.recv(1024)
            if not bytes_read:    
                break
            file.write(bytes_read)

    print("File received successfully.")
    client.close()
    server.close()