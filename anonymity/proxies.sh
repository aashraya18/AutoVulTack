cat ./configs/proxychains.txt > ~/../../etc/proxychains.conf
sudo chmod 666 ~/../../etc/proxychains.conf
echo "proxychains config done"
sudo chmod 644 ~/../../etc/proxychains.conf
sudo xterm proxychains firefox www.duckduckgo.com
exit
