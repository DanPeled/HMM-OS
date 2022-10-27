import time
import os
import functions as fu
import psutil
from datetime import datetime
import platform

device_type = None


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
    if battery is None:
        device_type = 'Desktop'
    else:
        device_type = 'Laptop'
        print(f"Battery level - {battery.percent}%\nLogged in on a {device_type} - {platform.system()} {platform.release()}")
    print("""
    """)
    fu.check_for_answers()
