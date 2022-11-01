from datetime import datetime as dt
import time as t

holidays = {'12-31': 'New year'}


def upcoming_month(event, year, month):
    if dt.now().date().strftime("%Y.%m") == f"{year}.{month}":
        print(f"{event} is upcoming this month!")


def check_upcoming():
    with open('events/event list.txt') as f:
        read = f.read().split(',')
        for event in read:
            with open(f'events/{event}.txt') as file:
                current_event = file.readlines()
                event_date = current_event[2].replace('starts on - ', '').replace(' ', '').split('.')
                upcoming_month(event=event, year=event_date[0], month=event_date[1])


def check_for_events():
    if dt.now().strftime("%m-%d") in holidays:
        event = holidays[dt.now().strftime("%m-%d")]
        if event != holidays['12-31']:
            print(f'it is {event}')
        else:
            if dt.now().time().strftime("%H:%M:%S") == dt.now().time().strftime("23:59:55"):
                print("""
███████╗
██╔════╝
██████╗░
╚════██╗
██████╔╝
╚═════╝░""")
                t.sleep(1)
                print("""
░░██╗██╗
░██╔╝██║
██╔╝░██║
███████║
╚════██║
░░░░░╚═╝""")
                t.sleep(1)
                print("""
██████╗░
╚════██╗
░█████╔╝
░╚═══██╗
██████╔╝
╚═════╝░""")
                t.sleep(1)
                print("""
██████╗░
╚════██╗
░░███╔═╝
██╔══╝░░
███████╗
╚══════╝""")
                t.sleep(1)
                print("""
░░███╗░░
░████║░░
██╔██║░░
╚═╝██║░░
███████╗
╚══════╝""")
                t.sleep(1)
                print("""
██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ███╗░░██╗███████╗░██╗░░░░░░░██╗  ██╗░░░██╗███████╗░█████╗░██████╗░██╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ████╗░██║██╔════╝░██║░░██╗░░██║  ╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██║
███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██╔██╗██║█████╗░░░╚██╗████╗██╔╝  ░╚████╔╝░█████╗░░███████║██████╔╝██║
██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░  ██║╚████║██╔══╝░░░░████╔═████║░  ░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██╗╚═╝
██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░  ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░  ░░░██║░░░███████╗██║░░██║██║░░██║██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝""")
            if dt.now().time().strftime("%H:%M:%S") == dt.now().time().strftime("23:59:56"):
                print("""
        ░░██╗██╗
        ░██╔╝██║
        ██╔╝░██║
        ███████║
        ╚════██║
        ░░░░░╚═╝""")
                t.sleep(1)
                print("""
        ██████╗░
        ╚════██╗
        ░█████╔╝
        ░╚═══██╗
        ██████╔╝
        ╚═════╝░""")
                t.sleep(1)
                print("""
        ██████╗░
        ╚════██╗
        ░░███╔═╝
        ██╔══╝░░
        ███████╗
        ╚══════╝""")
                t.sleep(1)
                print("""
        ░░███╗░░
        ░████║░░
        ██╔██║░░
        ╚═╝██║░░
        ███████╗
        ╚══════╝""")
                t.sleep(1)
                print("""
        ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ███╗░░██╗███████╗░██╗░░░░░░░██╗  ██╗░░░██╗███████╗░█████╗░██████╗░██╗
        ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ████╗░██║██╔════╝░██║░░██╗░░██║  ╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██║
        ███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██╔██╗██║█████╗░░░╚██╗████╗██╔╝  ░╚████╔╝░█████╗░░███████║██████╔╝██║
        ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░  ██║╚████║██╔══╝░░░░████╔═████║░  ░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██╗╚═╝
        ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░  ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░  ░░░██║░░░███████╗██║░░██║██║░░██║██╗
        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝""")
            if dt.now().time().strftime("%H:%M:%S") == dt.now().time().strftime("23:59:57"):
                print("""
            ██████╗░
            ╚════██╗
            ░█████╔╝
            ░╚═══██╗
            ██████╔╝
            ╚═════╝░""")
                t.sleep(1)
                print("""
            ██████╗░
            ╚════██╗
            ░░███╔═╝
            ██╔══╝░░
            ███████╗
            ╚══════╝""")
                t.sleep(1)
                print("""
            ░░███╗░░
            ░████║░░
            ██╔██║░░
            ╚═╝██║░░
            ███████╗
            ╚══════╝""")
                t.sleep(1)
                print("""
            ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ███╗░░██╗███████╗░██╗░░░░░░░██╗  ██╗░░░██╗███████╗░█████╗░██████╗░██╗
            ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ████╗░██║██╔════╝░██║░░██╗░░██║  ╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██║
            ███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██╔██╗██║█████╗░░░╚██╗████╗██╔╝  ░╚████╔╝░█████╗░░███████║██████╔╝██║
            ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░  ██║╚████║██╔══╝░░░░████╔═████║░  ░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██╗╚═╝
            ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░  ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░  ░░░██║░░░███████╗██║░░██║██║░░██║██╗
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝""")
            if dt.now().time().strftime("%H:%M:%S") == dt.now().time().strftime("23:59:58"):
                print("""
            ██████╗░
            ╚════██╗
            ░░███╔═╝
            ██╔══╝░░
            ███████╗
            ╚══════╝""")
                t.sleep(1)
                print("""
            ░░███╗░░
            ░████║░░
            ██╔██║░░
            ╚═╝██║░░
            ███████╗
            ╚══════╝""")
                t.sleep(1)
                print("""
            ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ███╗░░██╗███████╗░██╗░░░░░░░██╗  ██╗░░░██╗███████╗░█████╗░██████╗░██╗
            ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ████╗░██║██╔════╝░██║░░██╗░░██║  ╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██║
            ███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██╔██╗██║█████╗░░░╚██╗████╗██╔╝  ░╚████╔╝░█████╗░░███████║██████╔╝██║
            ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░  ██║╚████║██╔══╝░░░░████╔═████║░  ░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██╗╚═╝
            ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░  ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░  ░░░██║░░░███████╗██║░░██║██║░░██║██╗
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝""")
            if dt.now().time().strftime("%H:%M:%S") == dt.now().time().strftime("23:59:59"):
                print("""
            ░░███╗░░
            ░████║░░
            ██╔██║░░
            ╚═╝██║░░
            ███████╗
            ╚══════╝""")
                t.sleep(1)
                print("""
            ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ███╗░░██╗███████╗░██╗░░░░░░░██╗  ██╗░░░██╗███████╗░█████╗░██████╗░██╗
            ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ████╗░██║██╔════╝░██║░░██╗░░██║  ╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██║
            ███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██╔██╗██║█████╗░░░╚██╗████╗██╔╝  ░╚████╔╝░█████╗░░███████║██████╔╝██║
            ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░  ██║╚████║██╔══╝░░░░████╔═████║░  ░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██╗╚═╝
            ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░  ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░  ░░░██║░░░███████╗██║░░██║██║░░██║██╗
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝""")
    else:
        pass
