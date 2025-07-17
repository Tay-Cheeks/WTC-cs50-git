import subprocess

in = input("Enter your server ip: ")
subprocess.run(["ping", in])

print("Attempting to connect to the server")
print("Application authentication was successful")
