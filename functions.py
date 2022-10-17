import random
import secrets
import string
from datetime import datetime
import time as t  # IMPORTS#
import socket
import turtle
import pyfiglet
import psutil
import pyautogui as pg
from colorama import Fore, Style
from tkinter import *
from tkinter import filedialog
import os
import webbrowser as wb


# Code #
def camera_ASCII():
    wb.open('https://danpeled.github.io/camera_to_ASCII/', 0)
    print(f'Opening https://danpeled.github.io/camera_to_ASCII/')


def files():
    def openFile():
        filepath = filedialog.askopenfilename(initialdir="/",
                                              title="Open file okay?",
                                              filetypes=(("text files", "*.txt"),
                                                         ("all files", "*.*")))
        os.startfile(filepath)

    window = Tk()
    window.title = 'Choose a file'
    button = Button(text="Open", command=openFile)
    button.pack()
    window.mainloop()


def clear():
    print('\n' * 100)


def leave():
    pg.keyDown('win')
    pg.press('up')
    pg.keyUp('win')
    pg.moveTo(1891, 13)
    pg.leftClick()


def battery_get():
    battery = psutil.sensors_battery()
    print(f"Battery - {battery.percent}%")


def enter_google(website):
    pg.press("win")
    t.sleep(0.1)
    pg.typewrite("google")
    t.sleep(0.1)
    pg.press("enter")
    t.sleep(0.1)

    t.sleep(0.1)
    pg.typewrite(f"https://{website}")
    pg.press("enter")


def shut_down():
    pg.keyDown('win')
    pg.press('d')
    pg.keyUp('win')
    pg.keyDown('alt')
    pg.press('f4')
    pg.keyUp('alt')
    pg.press('enter')


def desktop():  # Desktop command
    pg.keyDown('win')
    pg.press('d')
    pg.keyUp('win')


# Open#
def open_app(program_to_open):  # Open APP command
    pg.press('win')
    pg.typewrite(program_to_open)
    t.sleep(0.001)
    pg.press('enter')


def _printASCII(text):
    print(pyfiglet.figlet_format(text))


def generate_password():
    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    # fix password length
    pwd_length = 12

    # generate a password string
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    print(f'your generated password - {pwd}')


def re_print(text):
    print(text[::-1])


def ASCII_re_print(text):
    print(pyfiglet.figlet_format(text[::-1]))


def time():
    print(datetime.now().time().strftime("%H:%M:%S"))


def date():
    print(datetime.now().strftime("%Y-%m-%d"))


def roll_dice():
    start = input('Choose a min number : ')
    end = input('Choose a max number : ')
    end = int(end)
    start = int(start)
    print(f'Dice result - {random.randint(start, end)}')


def help_c():  # Help Command
    print(f'{pyfiglet.figlet_format("HELP")}\n',
          """   [1] website / enter a website <website domain> - enters a website of your choice
    [2] open <app name> - opens a app of your choice
    [3] help - opens list of commands
    [4] desk / desktop - opens your desktop
    [5] generate password - generates a 12 characters password
    [6] shut down / power off / power - shut downs the computer
    [7] you can use math equations e.g - 1 + 5 will return 6
    [8] print <text> - prints a text in ASCII
    [9] battery - shows your battery percentage
    [10] revprint <text> - prints a text backwards
    [11] ASCII revprint <text> - print a text backwards in ASCII
    [12] date - returns the current date
    [13] time - returns the current time
    [14] file - opens a file explorer to choose a file to open from
    [15] BIOS - displays the user information, requires password entry
    [16] camera ASCII - opens a webpage of camera to ASCII
    [17] dice - gives a random number between a chosen min and max""")


def display_info():
    while True:
        b_login = input('Enter your password to see BIOS: ')
        if b_login == open('user/password.txt').read():
            print('Opening BIOS')
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print(f'USERNAME : {open("user/username.txt").read()}\n'
                  f'PASSWORD : {open("user/password.txt").read()}\n'
                  f'HOST NAME : {host_name}\n'
                  f'LOCAL IPS : {host_ip}')
            b = input('[1] Change username.\n[2] Change password.\n[3] Go back\n[?] : ')
            if b == '2':
                edit_p = input("Enter new password : ")
                with open('user/password.txt', 'w') as f:
                    f.writelines(edit_p)
                print(f'Password changed to - {edit_p}')
                print("Restart OS to confirm")
                break
            if b == '1':
                edit_n = input("Enter new username : ")
                with open('user/username.txt', 'w') as f:
                    f.writelines(edit_n)
                print(f'Username changed to - {edit_n}')
                print("Restart OS to confirm.")
                break
            if b == '3':
                print('Leaving BIOS')
                break
        else:
            if b_login == 'exit' or b_login == 'leave' or b_login == 'back':
                break
            else:
                continue


def _color(color, text: str = '') -> str:  # Terminal set color command
    return f'{color}{text}{Style.RESET_ALL}'


# noinspection PyUnreachableCode
def snake():
    color_list = [
        'gold',
        'yellow',
        'red',
        'gray',
        'orange',
        'magenta',
        'purple',
        'pink'

    ]

    delay = 0.1

    score = 0

    high_score = 0

    # Creating a window screen

    wn = turtle.Screen()

    wn.title("Snake Game")

    wn.bgcolor("blue")
    # the width and height can be put as user's choice

    wn.setup(width=600, height=600)

    wn.tracer(0)

    # head of the snake

    head = turtle.Turtle()

    head.shape("turtle")

    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    # food in the game

    food = turtle.Turtle()

    shapes = random.choice(['square', 'triangle', 'circle'])

    food.speed(0)
    food.shape(shapes)
    food.color(random.choice(color_list))
    food.penup()

    food.goto(0, 100)

    pen = turtle.Turtle()

    pen.speed(0)

    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()

    pen.goto(0, 250)

    pen.write("Score : 0  High Score : 0", align="center",

              font=("candara", 24, "bold"))

    # assigning key directions

    def group():
        if head.direction != "down":
            head.direction = "up"
            head.settiltangle(90)

    def godown():
        if head.direction != "up":
            head.direction = "down"
            head.settiltangle(-90)

    def goleft():
        if head.direction != "right":
            head.direction = "left"
            head.settiltangle(-180)

    def goright():
        if head.direction != "left":
            head.direction = "right"
            head.settiltangle(0)

    def move():
        if head.direction == "up":
            _y = head.ycor()

            head.sety(_y + 20)

        if head.direction == "down":
            _y = head.ycor()

            head.sety(_y - 20)

        if head.direction == "left":
            _x = head.xcor()

            head.setx(_x - 20)

        if head.direction == "right":
            _x = head.xcor()

            head.setx(_x + 20)

    wn.listen()

    def close():
        wn.bye()

    wn.onkeypress(group, "w")

    wn.onkeypress(godown, "s")

    wn.onkeypress(goleft, "a")
    wn.onkeypress(close, 'p')
    wn.onkeypress(goright, "d")

    segments = []

    # Main Gameplay

    while True:

        wn.update()

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

            t.sleep(1)

            head.goto(0, 0)

            head.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)
            food.color(random.choice(color_list))
            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color(random.choice(color_list))
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        # Checking for head collisions with body segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                t.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()

                score = 0

                delay = 0.1

                pen.clear()

                pen.write("Score : {} High Score : {} ".format(

                    score, high_score), align="center", font=("candara", 24, "bold"))

        t.sleep(delay)

    wn.mainloop()


def check_for_errors(what_to_do):
    if what_to_do == 'open':
        return 'The right usage is \"open <app name>\"'
    elif what_to_do.lower() == 'website' or what_to_do.lower() == 'enter a website':
        return f'The right usage is \"{what_to_do.lower()} <website domain without \"https://\">\"'
    else:
        return None


def calculator(inserted: str = ''):
    print(eval(f'{inserted}'))


def check_for_answers():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    what_to_do = input('[?] : ')
    if what_to_do.lower().startswith('enter a website ') or what_to_do.lower().startswith('website '):
        if what_to_do.lower().startswith('website '):
            print(f'Opening {what_to_do[8:]} on google')
            enter_google(what_to_do[8:])
        elif what_to_do.lower().startswith('enter a website '):
            print(f'Opening {what_to_do[16:]} on google')
            enter_google(what_to_do[16:])
    elif what_to_do.lower() == 'shut down' or what_to_do.lower() == 'power off' or what_to_do == 'power':
        print(f'shutting off...')
        shut_down()
    elif what_to_do.lower() == 'desk' or what_to_do.lower() == 'desktop':
        print(f'Opening desktop')
        desktop()
    elif what_to_do == 'leave':
        leave()
    elif what_to_do.lower().startswith('open '):
        print(f'Opening {what_to_do[5].capitalize() + what_to_do[6:]}')
        open_app(what_to_do[5:])
    elif what_to_do == 'help':
        help_c()
    elif what_to_do == 'snake':
        snake()
    elif what_to_do == 'generate password':
        generate_password()
    elif what_to_do[0] in str(digits):
        calculator(what_to_do)
    elif what_to_do == 'BIOS':
        display_info()
    elif what_to_do.startswith('print '):
        _printASCII(what_to_do[6:])
    elif what_to_do.startswith('ASCII revprint '):
        ASCII_re_print(what_to_do[15:])
    elif what_to_do == 'battery':
        battery_get()
    elif what_to_do.startswith('revprint '):
        re_print(what_to_do[9:])
    elif what_to_do == 'time':
        time()
    elif what_to_do == 'date':
        date()
    elif what_to_do == 'file':
        files()
    elif what_to_do == 'camera ASCII':
        camera_ASCII()
    elif what_to_do == 'dice':
        roll_dice()
    else:
        if check_for_errors(what_to_do) is None:
            print("You have used an un existing  statement, use help for list of commands")
        else:
            print(_color(Fore.RED, check_for_errors(what_to_do)))
    check_for_answers()
