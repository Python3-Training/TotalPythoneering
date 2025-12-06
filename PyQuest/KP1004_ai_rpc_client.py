'''
Here is an example of a simple RPC client and
server using Python's built-in xmlrpc.client and
xmlrpc.server modules. This demonstrates a basic
remote procedure call where the client invokes a
function defined on the server.
'''
import xmlrpc.client

# Connect to the RPC server
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    # Call the remote 'add' function
    result_add = proxy.add(5, 3)
    print(f"Result of add(5, 3): {result_add}")

    # Call the remote 'multiply' function
    result_multiply = proxy.multiply(4, 6)
    print(f"Result of multiply(4, 6): {result_multiply}")
