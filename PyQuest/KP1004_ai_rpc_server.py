'''
Here is an example of a simple RPC client and
server using Python's built-in xmlrpc.client and
xmlrpc.server modules. This demonstrates a basic
remote procedure call where the client invokes a
function defined on the server.
'''
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

# Start the server's main loop
server.serve_forever()
