'''
create a TCP/IP server to echo what is sent to it onto a tkinter screen. Tkinter screen size is 800 by 600. Font size is 42 points. Font face is "STENCIL". Window title is "TOTAL PYTHONEERING," please.
'''
import socket
import sys

# Configuration to match the server
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def start_client():
    """Connects to the server and sends user input."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"Connected to {HOST}:{PORT}")
            print("Type a message and press Enter. Type 'exit' to quit.")

            while True:
                # Get input from the user
                message = input("Send> ")
                
                if message.lower() == 'exit':
                    print("Disconnecting...")
                    break
                
                if not message:
                    continue # Skip sending empty messages

                # Send data to the server, encoded to bytes
                s.sendall(message.encode('utf-8'))
                
                # Receive the echo response back from the server
                data = s.recv(1024)
                
                print(f"Recv> {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print(f"Error: Connection refused. Is the server running at {HOST}:{PORT}?")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_client()

