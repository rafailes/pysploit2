from termcolor import colored
import os

print(colored("[*]starting pysploit...", "blue"))

command = input(colored("pycommand> "))

if command == "help":
    print(colored("""listen
    revese_shell
    sessions_listening
    privilege escalation""", "green"))

if command == "listen":
    os.system("pylistener.py")
if command == "reverse_shell":
    print(colored("[*]revsers shell created", "blue"))
