import os
import time

def restert():
    os.system('clear')
def install_metasploit():
    print("")
    print("")
    print(" \033[1;31m   ███╗   ███╗███████╗████████╗ █████╗            ██╗ ")
    print(" \033[1;31m   ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗           ██║ ")
    print(" \033[1;31m   ██╔████╔██║█████╗     ██║   ███████║█████╗     ██║ ")
    print("  \033[1;31m  ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║╚════╝██   ██║    coded by v33dx-jimmy")
    print("  \033[1;31m  ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║      ╚█████╔╝ ")
    print("  \033[1;31m  ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝       ╚════╝  ")
    print("                                  \033[1;33mThis script for install and fix metasploit  on Termux !!  ")
    print("")
    print("")
    print("\033[1;33m[1] \033[1;32mMetasploit\033[1;32m")
    print("\033[1;33m[2] \033[1;32mFix metasploit\033[1;32m")
    install = input("\033[1;33m[+] \033[1;35mMETA-G@root-# \033[1;35m")
    if install =='1':
        time.sleep(0.3)
        os.system('pkg update && pkg upgrade -y && pkg install wget && pkg install python2 && pkg install ruby && pkg install wget && pkg install curl && pkg install openssh')
        os.system('cd $HOME;wget https://raw.githubusercontent.com/efxtv/Metasploit-in-termux/main/metasploit-6-termux.sh -q;bash metasploit-6-termux.sh')
        restert()
    elif install =='2':
        os.system('bash fix.sh')
install_metasploit()