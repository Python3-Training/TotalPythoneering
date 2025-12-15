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

import xmlrpc.client
import time

PROXY_URL = "http://localhost:8000/"

def client_echo(message, url=PROXY_URL):
    try:
        proxy = xmlrpc.client.ServerProxy(url)
        # You can also call built-in methods if registered
        # print(proxy.system.listMethods())
        return True, proxy.echo_message(message)
    except ConnectionRefusedError:
        return False, "Error: Could not connect to the RPC server. Make sure ai_rpc_server.py is running."
    except Exception as e:
        return False, f"An error occurred: {e}"
    return False, '' # Meh - safe coding is no accident?



