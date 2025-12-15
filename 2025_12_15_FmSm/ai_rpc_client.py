'''
create an rpc server to echo what is sent to it onto a tkinter screen. Tkinter screen size is 800 by 600. Font size is 42 points. Font face is "STENCIL". Window title is "TOTAL PYTHONEERING," please.
'''
import xmlrpc.client
import time

PROXY_URL = "http://localhost:8000/"

# Create a proxy object to connect to the RPC server
proxy = xmlrpc.client.ServerProxy(PROXY_URL)

print(f"Connecting to RPC server at {PROXY_URL}...")

# Example calls
try:
    response1 = proxy.echo_message("Hello, TOTAL PYTHONEERING!")
    print(f"Server response 1: {response1}")
    time.sleep(1)

    response2 = proxy.echo_message("This is a second message with a number: 42")
    print(f"Server response 2: {response2}")
    time.sleep(1)

    response3 = proxy.echo_message("Sending data from the client side.")
    print(f"Server response 3: {response3}")

    # You can also call built-in methods if registered
    # print(proxy.system.listMethods())

except ConnectionRefusedError:
    print("Error: Could not connect to the RPC server. Make sure rpc_server_gui.py is running.")
except Exception as e:
    print(f"An error occurred: {e}")

