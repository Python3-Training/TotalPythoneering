'''
create a TCP/IP server to echo what is sent to it onto a tkinter screen. Tkinter screen size is 800 by 600. Font size is 42 points. Font face is "STENCIL". Window title is "TOTAL PYTHONEERING," please.
'''
import socket
import threading
import queue
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font as tkFont

# --- Configuration ---
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FONT_SIZE = 42
FONT_FACE = "STENCIL"
WINDOW_TITLE = "TOTAL PYTHONEERING"

# Thread-safe queue for communication between server and GUI
gui_queue = queue.Queue()

def handle_client_connection(conn, addr, text_widget):
    """Handles an individual client connection in a separate thread."""
    print(f"Connected by {addr}")
    try:
        while True:
            # Receive data (decode as utf-8)
            data = conn.recv(4096)
            if not data:
                break
            message = data.decode('utf-8')
            # Add message to the queue for the GUI thread to process
            gui_queue.put(f"[{addr}]: {message}")
            # Echo the message back to the client
            conn.sendall(data)
    except Exception as e:
        gui_queue.put(f"Error with client {addr}: {e}")
    finally:
        print(f"Client {addr} disconnected")
        conn.close()

def start_server(text_widget):
    """Starts the TCP server in a separate daemon thread."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            gui_queue.put(f"Server started, listening on {HOST}:{PORT}")
            while True:
                conn, addr = s.accept()
                client_thread = threading.Thread(
                    target=handle_client_connection, 
                    args=(conn, addr, text_widget),
                    daemon=True # Daemon threads exit when the main program exits
                )
                client_thread.start()
    except Exception as e:
        gui_queue.put(f"Server error: {e}")

def check_queue(text_widget):
    """Periodically checks the queue for new messages and updates the GUI."""
    try:
        while True:
            message = gui_queue.get_nowait()
            text_widget.config(state='normal') # Enable editing
            text_widget.insert(tk.END, message + '\n')
            text_widget.see(tk.END) # Scroll to the bottom
            text_widget.config(state='disabled') # Disable editing
    except queue.Empty:
        pass
    finally:
        # Schedule the next check
        text_widget.after(100, check_queue, text_widget) # Check every 100ms

def main():
    """Sets up the Tkinter GUI and starts the server thread."""
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Configure the font
    try:
        # Check if the "STENCIL" font is available and use it
        available_fonts = list(tkFont.families())
        if FONT_FACE in available_fonts:
            custom_font = tkFont.Font(family=FONT_FACE, size=FONT_SIZE)
        else:
            # Fallback to a generic monospaced font if STENCIL is not found
            custom_font = tkFont.Font(family="Monospace", size=FONT_SIZE)
            print(f"'{FONT_FACE}' font not found, using 'Monospace' instead.")
    except Exception:
        custom_font = tkFont.Font(size=FONT_SIZE) # Fallback if error occurs

    # Create a scrolled text widget for the echo display
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=custom_font, bg='black', fg='lime')
    text_area.pack(expand=True, fill='both')
    text_area.config(state='disabled') # Make read-only initially

    # Start the TCP server in a separate thread
    server_thread = threading.Thread(target=start_server, args=(text_area,), daemon=True)
    server_thread.start()

    # Start the periodic queue check for GUI updates
    check_queue(text_area)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
