import os
import socket

s=socket.socket()
port=8080
host= input(str("please enter the server address : "))
s.bind((host,port))
print("")
print("Connected to Server successfully", host)
print("")

while 1:
    command = s.recv (1024)
    command = command.decode ()
    print ("Command recieved")
    print ("")
    if command == "view cwd":
            files = os.getcwd()
            files = str(files)
            s.send (files.encode())
            print ("")
            print ("Command has been executed successfully..")
            print ("")

    elif command == "custom_dir":
            user_input - s.recv (5000)
            user_input = user_input.decode ()
            files = os.listdir (user_input)
            files = str(files)
            s.send (files.encode () )
            print ("")
            print ("Command has been executed successfully..")
            print ("")

    else:
            print ("")
            print ("Command not recognised")
