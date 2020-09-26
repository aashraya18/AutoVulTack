import os

def intro():
	os.system("bash intro/menu.sh")
	a = int(input('Please Enter 1 for New Project or 2 for Old Project: '))
	if(a==1):
		[ipadd, url, host, workspace] = startup1()
	else:
		[ipadd, url, host, workspace] = startup2()

	return [ipadd, url, host, workspace]
	
def menu():
	choice=0
	while(choice<1 or choice>5):
		os.system('clear')
		os.system("figlet Menu")
		print("Enter what you want to do next")
		print("1.\tAnonimity Configuration")
		print("2.\tInformation Gathering")
		print("3.\tVulnerability Assessment")
		print("4.\tPerform Attack")
		print("5.\tExit")
		choice = int(input("Enter your choice: "))
		if(choice<1 or choice>5):
			print("Please enter a valid choice")
		else:
			os.system('clear')
			return choice


def startup1():
	workspace = input('Enter workspace/project name\t: ')
	print(f'workspace {workspace} create')
	os.system('mkdir workspace/'+workspace)
	ipadd = input('Enter target ip address\t: ')
	url = input('Enter target url\t: ')
	host = input('Enter target host\t: ')
	with open('workspace/'+workspace+'/target.txt', 'w') as fil:
		fil.write(ipadd+'\n')
		fil.write(url+'\n')
		fil.write(host+'\n')
	return [ipadd, url, host, workspace]


def startup2():
	projects = os.listdir('./workspace/')
	print("Current workspaces")	
	for i in projects:
		print(i)
	workspace = input('Choose project\t\t: ')
	with open('workspace/'+workspace+'/target.txt', 'r') as fil:
		ipadd = fil.read()
		url = fil.read()
		host = fil.read()
		ipadd=ipadd[:-1]
		url=url[:-1]
		host=host[:-1]
	return [ipadd, url, host, workspace]
