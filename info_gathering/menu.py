import os

def info_gathering_menu(ipadd):
	choice=0
	while(choice<1 or choice>4):
		print("1.\tNikto")
		print("2.\tNmap")
		print("3.\tWhoIs")
		print("4.\thost")
		choice=int(input("Enter your choice: "))
		
		if(choice<1 or choice>4):
			print("Enter a valid choice...")
			continue

		if(choice==1):
			run_nikto(ipadd)
		elif(choice == 2):
			continue
		elif(choice == 3):
			run_whois(ipadd)
		elif(choice == 4):
			run_host(ipadd)

		input("Press enter to continue")
		os.system('clear')
		info_gathering_menu(ipadd)

		

def run_nikto(ipadd):
	choice = input("Add extra options? [y/n]")
	base = "nikto -h "+ipadd
	if(choice != 'n'):
		ports = input("Ports\t\t: ").split(' ')
		if(len(ports)>0):
			base +=" -port "
			for i in ports[:-1]:
				base += (i+",")
			base += ports[-1]
		print(base)
		scantime = input("Scan time\t: ")
		if(len(scantime)>0):
			base+=(" -maxtime "+scantime)
		
		if(input("Disable SSL[y/n]\t: ")=='y'):
			base+=" -nossl"
		elif(input("Force SSL[y/n]\t: ")=='y'):
			base=" -ssl"
		
		if(input("Database check[y/n]\t: ")=='y'):
			base+=' -dbcheck'

		print("Tuning")
		print("1   Interesting file")
		print("2   Misconfiguration")
		print("3   Information Disclosure")
		print("4   Injection (XSS/Script/HTML)")
		print("5   Remote File Retrieval – Inside Web Root")
		print("6   Denial of Service")
		print("7   Remote File Retrieval – Server Wide")
		print("8   Command Execution – Remote Shell")
		print("9   SQL Injection")
		print("0   File Upload")
		print("a   Authentication Bypass")
		print("b   Software Identification")
		print("c   Remote Source Inclusion")
		print("x   Reverse Tuning Option")
		tuning = input("Enter tuning option\t: ")
		if(len(tuning)>0):
			base+=" -Tuning "+tuning
		
		base += " |tee -a "+"./output.txt"
		
	os.system(base)


def run_whois(ipadd):
	os.system("whois "+ipadd+" |tee -a output.txt")


def run_host(ipadd):
	os.system("host "+ipadd+" |tee -a output.txt")
	



info_gathering_menu('137.74.187.104')

