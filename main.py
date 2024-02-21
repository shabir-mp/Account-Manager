import os, time

password = ""
username = "User"
title = "\033[34mPassword Manager v1.0\033[0m"
passwordData = []
passcode = -1


def login():
  print(title)
  print()
  inpt = input("\033[30m→ Press Enter to Continue \033[0m")
  os.system("clear")
  start()

def view():
  os.system("clear")
  print(title)
  print()
  if len(passwordData) == 0:
    print("Empty List. Nothing To See Here !")
    time.sleep(2)
    os.system("clear")
    start()
  else:
    for i in range(len(passwordData)):
      print(f"{i+1}. {passwordData[i][0]:20}")
      print(f"| Username: {passwordData[i][1][0]}")
      print(f"| Password: {passwordData[i][2][0]}")
      if len(passwordData[i][3]) > 0:
        print(f"| Notes: {passwordData[i][3][0]}")
      print("-" * 40)
    time.sleep(10)
    os.system("clear")
    start()


def add():
  global passcode
  passcode += 1
  os.system("clear")
  print(title)
  print()
  appadd = input("App/Website Name : ")
  useradd = input("Username : ")
  passwordadd = input("Password : ")
  notesadd = input("Add Notes (optional) : ")
  passwordData.append([appadd, [useradd], [passwordadd], [notesadd]])
  print("\033[32mPassword Added Successfully\033[0m")
  time.sleep(2)
  os.system("clear")
  start()

def settings():
  os.system("clear")
  print("Sorry, this Feature are is being construction.")
  time.sleep(4)
  os.system("clear")
  start()


def make():
  os.system("clear")
  print("Sorry, this Feature are is being construction.")
  time.sleep(4)
  os.system("clear")
  start()

def start():
  os.system("clear")
  print(title)
  print()
  print(f"\033[0mWelcome Back, {username} !")
  print()
  print("""
1. View Password List
2. Add Password List
3. Make Password
4. User Settings
""")
  print()
  inpt = input("\033[31m → \033[0m").strip().lower()
  if inpt == "1":
    view()
  elif inpt == "2":
    add()
  elif inpt == "3":
    make()
  elif inpt == "4":
    settings()


login()
