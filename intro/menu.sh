start(){
clear
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
figlet -f big "AutoVulTack"
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
echo "Automated Vulnerability Assessment and Attack" 
echo "Version = 1.0"
echo "By Mihir Mangesh Pavuskar"
echo "Reg. No.: 18BCE0159"
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
read -r -p "Please Enter 1 for New Project or 2 for Old Project: " a
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
if [ "$a" == 1 ]; then
startup1
elif [ "$a" == 2 ]; then
startup2
else
echo " Type 1 or 2 On Restart"
sleep 2
start
fi
}

startup1(){
read -r -p " 1.	Enter The Project Name (Client name):" company
mkdir workspace/$company
echo workspace -a $company >> workspace/$company/meta-work.rc
echo exit >> workspace/$company/meta-work.rc
#gnome-terminal -- msfconsole -q -r $company/meta-work.rc
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
echo "Metasploit Workspace Created: "$company
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
read -r -p " 2.	Enter the IP file location: " host
read -r -p " 4.	Enter The Path of The Password File: " pass
if [ "$pass" == 0 ]; then
$pass = /usr/share/metasploit-framework/data/john/wordlists/password.lst
fi
#read -r -p " Enter the Username list:" user
#read -r -p " Enter the Password list:" pass
read -r -p " 4.	Enter your IP address: " ip
read -r -p " 5.	Enter MSF-Handler port no: " port
#Starting postgresql
set threads 15
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
echo "Basic Configuration Setup Done"
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
Sleep 5
}

#Starup options 2

startup2(){
clear
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
echo "Current Project Folders"
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
ls -d */
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
echo "Choose Project Folders"
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
read -r -p " Please	Enter The Old Project Name (Client name): " company1
#gnome-terminal -- msfconsole -q -r $company1/meta-work.rc
msfconsole -q -r workspace/$company1/meta-work.rc
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
figlet -f big "Current Project/workspace is" $company1
echo -e "\e[1;32m----------------------------------------------------------\e[00m"
}

   
start

