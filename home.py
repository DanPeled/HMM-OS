import platform
from datetime import datetime

import psutil

import functions as fu

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
    print(f"WELCOME {l_n.title()}")
    print("The date & time is : ")
    print(datetime.now().time().strftime("%H:%M:%S"))
    print(datetime.now().strftime("%Y-%m-%d"))
    if battery is None:
        device_type = 'Desktop'
    else:
        device_type = 'Laptop'
        print(f"Battery level - {battery.percent}%\nLogged in on a {device_type} - {platform.system()}")
    print("""
    """)
    fu.check_for_answers()
