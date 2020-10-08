import os
import intro.menu as intro
import anonymity.anonymity as anonymity
import info_gathering.menu as inf
import vuln_assessment.menu as vuln
import exploit.menu as exploit

os.system('bash setup/setup.sh')
[ipadd, url, host, workspace] = intro.intro()
choice = 1
while(choice!=-1):
	choice = intro.menu()
	if(choice==1):
		anonymity.anonymity()
	elif(choice==2):
		inf.info_gathering_menu(ipadd, host, url)
	elif(choice==3):
		vuln.vuln_menu(ipadd, host, url)
	elif(choice==4):
		exploit.exploit_menu()
	elif(choice==5):
		os.system('mousepad output.txt')
	elif(choice==6):
		os.system('figlet -f big thank you')
		os.system(f'mv output.txt workspace/{workspace}/')
		break
	


print(ipadd, url, host, choice)


