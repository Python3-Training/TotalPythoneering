'''
create an rpc server to echo what is sent to it onto a tkinter screen. Tkinter screen size is 800 by 600. Font size is 42 points. Font face is "STENCIL". Window title is "TOTAL PYTHONEERING," please.
'''
import tkinter as tk
import tkinter.font as tkFont
from xmlrpc.server import SimpleXMLRPCServer
import threading
import sys

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("TOTAL PYTHONEERING, please")
root.geometry("800x600")

# Use a Text widget to display messages, as it handles large amounts of text better than a Label
# Configure the font: "STENCIL" family, size 42 points.
# Note: "STENCIL" is a common font name, but might vary by OS.
try:
    custom_font = tkFont.Font(family="STENCIL", size=42)
except tkFont.FontError:
    # Fallback to a generic fixed-width font if Stencil is not available
    custom_font = tkFont.Font(family="TkFixedFont", size=42)
    print("Warning: STENCIL font not found, using TkFixedFont instead.")

text_widget = tk.Text(root, font=custom_font, wrap=tk.WORD, bg="black", fg="lime")
text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
text_widget.insert(tk.END, "RPC Server GUI is running...\nWaiting for messages...\n")

def update_text_gui(message):
    """Safely updates the Tkinter text widget from the RPC thread."""
    # Use root.after to schedule the GUI update in the main Tkinter thread
    root.after(0, _insert_message, message)

def _insert_message(message):
    """Inserts a message into the Text widget and scrolls to the end."""
    text_widget.insert(tk.END, f"\n> {message}")
    text_widget.see(tk.END) # Auto-scroll to the bottom

# --- RPC Server Setup ---
RPC_PORT = 8000

class RpcFunctions:
    def echo_message(self, message):
        """Echoes the received message to the Tkinter GUI."""
        print(f"Received RPC message: {message}")
        update_text_gui(str(message)) # Ensure message is a string for Tkinter
        return f"Message received by server: {message}" # Return a confirmation to the client

def start_rpc_server():
    """Starts the XML-RPC server in its own thread."""
    try:
        server = SimpleXMLRPCServer(("0.0.0.0", RPC_PORT), allow_none=True)
        server.register_instance(RpcFunctions())
        print(f"RPC server listening on port {RPC_PORT}...")
        server.serve_forever() # Blocks this thread
    except Exception as e:
        print(f"Failed to start RPC server: {e}")
        # Consider a graceful way to inform the GUI thread or exit

# Start the RPC server in a separate thread so Tkinter's mainloop can run
rpc_thread = threading.Thread(target=start_rpc_server, daemon=True)
rpc_thread.start()

# --- Run the Tkinter main loop ---
root.mainloop()

# Note: The daemon thread will be terminated when the main loop (and script) exits.

