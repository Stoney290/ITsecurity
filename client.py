#commands = view_cwd ,custom_dir , download_file ,remove_file , send_file

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
    if command == "view_cwd":
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

    elif command == "download_file":
            file_path = s.recv(5000)
            file_path = file_path.decode ()
            file = open(file_path, "rb")
            data = file.read ()
            s.send(data.encode())
            print ("")
            print("File has been sent successfully")
            print ("")

    elif command == "remove_file":
            fileanddir = s.recv (6000)
            fileanddir = fileanddir.decode ()
            os.remove (fileanddir)
            print ("")
            print ("Command has been executed successfully")
            print ("")

    elif command == "send_files":
            filename = s.recv (6000)
            print(filename)
            new_file = open(filename, "wb")
            data = s.recv (6000)
            print(data)
            new_file.write (data)
            new_file.close()

    else:
            print ("")
            print ("Command not recognised")
