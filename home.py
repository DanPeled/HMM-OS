import time
import os
import socket
import functions as fu
import psutil
import datetime


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
    print(str(datetime.datetime.now()))
    print(f"Battery level - {battery.percent}%")
    print("""
    """)
    fu.check_for_answers()
