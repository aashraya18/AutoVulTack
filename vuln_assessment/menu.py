import os

def info_gathering_menu(ipadd='',host='',url=''):
	choice=0
	os.system("figlet -f big Vulnerability Assessment") 
	while(choice<1 or choice>5):
		print("1.\tNikto")
		print("2.\tNmap")
		print("3.\tWapiti")
		print("4.\tExit")
		choice=int(input("Enter your choice: "))
		
		if(choice<1 or choice>6):
			print("Enter a valid choice...")
			continue

		if(choice==1):
			run_nikto(ipadd)
		elif(choice == 2):
			run_nmap(ipadd)
		elif(choice == 3):
			run_wapiti(url)
		elif(choice == 4):
			return

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

def run_wapiti(url):
	base = 'wapiti -u '+url

	choice = input("Add extra options?[y/n]\t: ")
	if(choice != 'n'):
		print("Scope\npage\nfolder\ndomain\nurl\npunk")
		scope = input("Enter scope\t: ")
		if(len(scope)>0):
			base+=' --scope '+scope
		os.system('wapiti --list-modules')
		modules=input('Enter modules(cs)\t: ')
		if(len(modules)>0):
			base+=' -m '+modules
		base+=' -f txt -o wapiti_report.txt'
	print(base)
	os.system(base)


def run_nmap(ipadd):
	if(input('Edit ip address[y/n]\t: ')=='y'):
		ipadd = input("IP address\t: ")

	base = 'nmap'
	choice = input("Add extra options?[y/n]\t: ")
	if(choice != 'n'):

		print("Scan type\t")
		print("TCP Connect Scan\t-sT")
		print("TCP SYN scan(Silent scan) -sS")
		print("UDP scan\t\t-sU ")
		print("No ping scan\t\t-Pn ")
		print("Host Discovery(no ports) -sn ")
		print("Version Scan\t\t-sV ")
		print("OS Detection\t\t-o ")
		scan = input("Enter scan type\t:")
		base += " " + scan
		
		ports = input('Ports(nmap format)\t: ')
		if(ports=='-F'):
			base+=' -F'
		else:		
			base += (' -p '+ports)

	base += " "+ipadd+" |tee -a output.txt"
	os.system(base)

info_gathering_menu('137.74.187.102')
