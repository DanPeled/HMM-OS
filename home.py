import time
import os
import socket
import functions as fu
import psutil
from datetime import datetime


def run():
    battery = psutil.sensors_battery()
    login_name = open('user/username.txt')
    l_n = login_name.read()
    print("""
██╗░░██╗███╗░░░███╗███╗░░░███╗  ░█████╗░░██████╗
██║░░██║████╗░████║████╗░████║  ██╔══██╗██╔════╝
███████║██╔████╔██║██╔████╔██║  ██║░░██║╚█████╗░
██╔══██║██║╚██╔╝██║██║╚██╔╝██║  ██║░░██║░╚═══██╗
██║░░██║██║░╚═╝░██║██║░╚═╝░██║  ╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░╚═════╝░""")
    print(f"WELCOME {l_n}")
    print("The date & time is : ")
    print(datetime.now().time().strftime("%H:%M:%S"))
    print(datetime.now().strftime("%Y-%m-%d"))

    print(f"Battery level - {battery.percent}%")
    print("""
    """)
    fu.check_for_answers()
