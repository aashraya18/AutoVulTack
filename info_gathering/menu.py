import os

def info_gathering_menu(ipadd='',host='', url=''):
	choice=0
	os.system("figlet -f big Information Gathering") 
	while(choice<1 or choice>5):
		print("1.\tWhatweb")
		print("2.\tNmap")
		print("3.\tWhoIs")
		print("4.\thost")
		print("5.\tDNSEnum")
		print("6.\tExit")
		choice=int(input("Enter your choice: "))
		
		if(choice<1 or choice>6):
			print("Enter a valid choice...")
			continue

		if(choice==1):
			run_whatweb(url)
		elif(choice == 2):
			run_nmap(ipadd)
		elif(choice == 3):
			run_whois(ipadd)
		elif(choice == 4):
			run_host(host)
		elif(choice == 5):
			run_dnsenum(host)
		elif(choice == 6):
			return

		input("Press enter to continue")
		os.system('clear')
		info_gathering_menu(ipadd)

		
def run_dnsenum(host):
	print("dnsenum "+host+" |tee -a output.txt")
	os.system("dnsenum -u g "+host+" -o dnsenum_op.xml")



def run_whatweb(host):
	os.system('whatweb '+host+' -v --color=NEVER |tee -a output.txt')


def run_whois(ipadd):
	os.system("whois "+ipadd+" |tee -a output.txt")


def run_host(host):
	os.system("host "+host+" |tee -a output.txt")
	
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

