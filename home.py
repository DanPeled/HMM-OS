import platform
from datetime import datetime
import event_functions as efu
import psutil

import functions as fu

global device_type


def run():
    global device_type
    battery = psutil.sensors_battery()
    login_name = open('user/username.txt')
    l_n = login_name.read()
    print("""
    ██╗░░██╗███╗░░░███╗███╗░░░███╗  ░█████╗░░██████╗
    ██║░░██║████╗░████║████╗░████║  ██╔══██╗██╔════╝
    ███████║██╔████╔██║██╔████╔██║  ██║░░██║╚█████╗░
    ██╔══██║██║╚██╔╝██║██║╚██╔╝██║  ██║░░██║░╚═══██╗
    ██║░░██║██║░╚═╝░██║██║░╚═╝░██║  ╚█████╔╝██████╔╝
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░╚═════╝░\n""")
    print(f"WELCOME {l_n.title()}")
    print("The date & time is : ")
    print(datetime.now().time().strftime("%H:%M:%S"))
    print(datetime.now().strftime("%Y-%m-%d"))
    if battery is None:
        device_type = 'Desktop'
    else:
        device_type = 'Laptop'
        print(f"Battery level - {battery.percent}%\nLogged in on a {platform.system()} {device_type}")
    print("""
    """)
    efu.check_upcoming('m')
    efu.check_upcoming('d')
    fu.check_for_answers()
