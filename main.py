import os, time

password = ""
username = "User"
title = "\033[34mPassword Manager v2.0\033[0m"
passwordData = []
passcode = -1
line = "-" * 40

def login():
  global password
  print(title)
  print()
  inpt = input("\033[30m→ Press Enter to Continue \033[0m")
  os.system("clear")
  print(title)
  while True:
    print("\033[30mNote: Please Enter for New Account\033[0m")
    inpt = input("Please input your password: ")
    f = open("data/passdata.accmgr", "r")
    password = f.readline()
    f.close()
    if inpt == password:
        os.system("clear")
        start()
        break
    else: 
      print("\nIncorrect Password! Try Again.")
      time.sleep(2)
      os.system('clear')
      continue

def view():
  os.system("clear")
  print("\033[34mView Account Data\033[0m")
  try:
    f = open("data/accdata.accmgr","r")
    accdata = f.read()
    f.close()
    if accdata:
      print(accdata)
    else:
      print("Empty List. Nothing To See Here !")
      time.sleep(2)
      os.system("clear")
      start()
  except:
    print("\033[32mSorry, an error occurred while retrieving data. Displays temporary data.\033[0m")
    for i in range(len(passwordData)):
      print(f"{i+1}. {passwordData[i][0]:20}")
      print(f"| Username: {passwordData[i][1][0]}")
      print(f"| Password: {passwordData[i][2][0]}")
      if len(passwordData[i][3]) > 0:
         print(f"| Notes: {passwordData[i][3][0]}")
         print(lines)
      time.sleep(10)
      os.system("clear")
      start()
  

def add():
  print("\033[34mAdd Account\033[0m")
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
  f = open("data/accdata.accmgr","a+")
  f.write(f"\n{line} \n Web/App Name: {appadd} \n 1.Username: {useradd} \n 2.Password: {passwordadd} \n 3.Notes {notesadd}")
  f.close()
  print("\033[32mPassword Added Successfully\033[0m")
  time.sleep(2)
  os.system("clear")
  start()


def make():
  os.system("clear")
  print("\033[30mSorry, this Feature are is being construction.\033[0m")
  time.sleep(4)
  os.system("clear")
  start()

def settings():
  global username, password
  while True:
    os.system("clear")
    print("\033[34mSettings\033[0m")
    print("1. Set Username \n2. Set Password \n3. Back to Home \n4. Logout")
    inpt = input("\033[31m→ \033[0m").strip().lower()
    print()
    if inpt == "1":
        f = open("data/userdata.accmgr","w")
        os.system("clear")
        newusername = input("Input your username: ")
        username = newusername
        f.write(newusername)
        f.close()
        time.sleep(2)
        os.system("clear")
        continue
    elif inpt == "2":
        os.system("clear")
        f = open("data/passdata.accmgr","r")
        password = f.readline()
        f.close()
        checkpass = input("Input your old password: ")
        if checkpass == password:
          f = open("data/passdata.accmgr", "w")
          newpass = input("\033[31m→ \033[0mInput your new password: ")
          f.write(newpass)
          print("\033[32mPassword Updated Succesfully.\033[0m")
          f.close()
          time.sleep(2)
          os.system("clear")
        else :
          print("\033[31mYour Password is incorrect. Please try again.\033[0m")
          time.sleep(2)
          continue
    elif inpt == "3":
      os.system("clear")
      start()
    elif inpt == "4":
      os.system("clear")
      logout()


def logout():
  os.system("clear")
  login()

def start():
  os.system("clear")
  print(title)
  print()
  try:
    f = open("data/userdata.accmgr","r")
    username = f.readline()
    print(f"\033[0mWelcome Back, {username} !")
    f.close()
  except:
    print("You use temporary data. An error occurred while loading local data")
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
