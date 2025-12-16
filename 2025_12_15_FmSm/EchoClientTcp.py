#!/usr/bin/env python3
'''
Mission:
Weaponize the AI effort into our solution so as to test
a basic echo. Be sure to run ai_rpc_server.py before
using this strategy.

Authon: Randall Nagy
Rev: 2025/12/15, 1.o
File: EchoClient.py
Video: https://youtube.com/shorts/2amN2KmAdko
Project: https://github.com/Python3-Training/TotalPythoneering
Status: Testing Success
'''

import socket
import sys

# Configuration to match the server
PROXY_URL = '127.0.0.1:65432'

def client_echo(message, url=PROXY_URL):
    """Connects to the server and sends user input."""
    try:
        cols = url.strip().split(':')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((cols[0],int(cols[1])))
            # Send data to the server, encoded to bytes
            s.sendall(message.encode('utf-8'))            
            # Receive the echo response back from the server
            return True, s.recv(1024)
    except ConnectionRefusedError:
        return False, f"Error: Connection refused. Is the server running at {HOST}:{PORT}?"
    except Exception as e:
        return False, f"An error occurred: {e}"

if __name__ == "__main__":
    print(client_echo('Testing.'))

