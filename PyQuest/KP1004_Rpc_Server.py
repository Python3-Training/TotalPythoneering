#!/usr/bin/env python3
'''
Mission:
Integrate the AI effort into our solution so as to test
the superset. Be sure to run this server before
running the test case (KP1004_rpc_client.py).

Authon: Randall Nagy
Rev: 2025/12/06, 1.o
File: KP1004_rpc_server.py
Video: https://youtube.com/shorts/NJMR5nsYG_0
Project: https://github.com/Python3-Training/TotalPythoneering/edit/main/PyQuest/
Status: Testing Success
'''

import KP1004
from xmlrpc.server import SimpleXMLRPCServer

# Define a function to be exposed via RPC
def add(x, y):
    print(f"Server received add({x}, {y})")
    return x + y

def multiply(x, y):
    print(f"Server received multiply({x}, {y})")
    return x * y


# Create an XML-RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

# Register the functions to be available for remote calls
server.register_function(add, "add")
server.register_function(multiply, "multiply")
server.register_function(KP1004.calc_area, "calc_area")

# Start the server's main loop
server.serve_forever()
