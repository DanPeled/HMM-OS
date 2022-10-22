import os
import functions as fu
import home as h

user_exits: bool


def start():
        if not os.path.exists('user/password.txt'):
            with open("user/username.txt", 'w') as f:
                f.writelines('')
            with open("user/password.txt", 'w') as f:
                f.writelines('')
        print("""
        ██╗░░██╗███╗░░░███╗███╗░░░███╗  ░█████╗░░██████╗
        ██║░░██║████╗░████║████╗░████║  ██╔══██╗██╔════╝
        ███████║██╔████╔██║██╔████╔██║  ██║░░██║╚█████╗░
        ██╔══██║██║╚██╔╝██║██║╚██╔╝██║  ██║░░██║░╚═══██╗
        ██║░░██║██║░╚═╝░██║██║░╚═╝░██║  ╚█████╔╝██████╔╝
        ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░╚═════╝░""")

        if open('user/username.txt').read() == '':
            print("""[1] Continue with setup.
            """)
            user_exits = False

        else:
            print("""[1] Delete User.
[2] Login.""")
            user_exits = True
        setup = input("[?]: ")
        if not user_exits:
            if setup == '1':
                name = input(str("Please enter a user name : "))
                pas = input(str("Please enter a password : "))
                lines = [name]
                with open("user/username.txt", 'w') as f:
                    f.writelines(lines)
                lines2 = [pas]
                with open("user/password.txt", 'w') as f:
                    f.writelines(lines2)
                print("""
            ░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗
            ██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝
            ██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░
            ██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░
            ╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗
            ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝""")
                login_pass = open('user/password.txt')
                login_name = open('user/username.txt')
                l_p = login_pass.read()
                l_n = login_name.read()
                while True:
                    login = input(f"Enter password {l_n}:  ")
                    if login == l_p:
                        fu.clear()
                        h.run()
                        break
                    else:
                        print("Password incorrect, try again")
            if setup == '2':
                login_pass = open('user/password.txt')
                login_name = open('user/username.txt')
                l_p = login_pass.read()
                l_n = login_name.read()
                while True:
                    login = input(f"Enter password {l_n}:  ")
                    if login == l_p:
                        fu.clear()
                        h.run()
                        break
                    else:
                        print("Password incorrect, try again")
            else:
                start()
        else:
            if setup == '1':
                response = input(f'Are you sure you want to delete this user ? \n[y] Yes\n[n] No\n[?] : ')
                if response.lower() == 'y':
                    os.remove('user/username.txt')
                    os.remove('user/password.txt')
                    print('User DELETED')
                elif response.lower() == 'n':
                    start()
                else:
                    start()
                start()
            if setup == '2':
                if setup == '2':
                    login_pass = open('user/password.txt')
                    login_name = open('user/username.txt')
                    l_p = login_pass.read()
                    l_n = login_name.read()
                    while True:
                        login = input(f"Enter password {l_n}:  ")
                        if login == l_p:
                            fu.clear()
                            h.run()
                            break
                        else:
                            print("Password incorrect, try again")
            else:
                start()
