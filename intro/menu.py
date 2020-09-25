import os

def intro():
    os.system("bash menu.sh")
    os.system("clear")
    os.system("figlet Menu")
    choice=0
    while(choice<1 or choice>4):
        print("Enter what you want to do next")
        print("1.\tAnonimity Configuration")
        print("2.\tInformation Gathering")
        print("3.\tVulnerability Assessment")
        print("4.\tPerform Attack")
        choice = int(input("Enter your choice: "))
        if(choice<1 or choice>4):
            print("Please enter a valid choice")
        else:
            return choice

intro()
