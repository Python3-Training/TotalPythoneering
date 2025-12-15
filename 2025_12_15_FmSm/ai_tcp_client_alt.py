'''
create a TCP/IP server to echo what is sent to it onto a tkinter screen. Tkinter screen size is 800 by 600. Font size is 42 points. Font face is "STENCIL". Window title is "TOTAL PYTHONEERING," please.
'''
'''
How to Run the Code

    Save the code as a Python file (e.g., echo_server_gui.py).
    Run the script from your terminal: python echo_server_gui.py
    The Tkinter window will open with the title "TOTAL PYTHONEERING".
    To test the server, you can use a separate terminal window and a client tool like telnet or nc (netcat), or another Python script.
        Using nc (netcat): nc 127.0.0.1 65432
        Using telnet: telnet 127.0.0.1 65432

Any message typed into the client and sent will be echoed back to the client and displayed on the Tkinter screen.
'''
