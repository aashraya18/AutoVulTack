import os
proxy = input('apply proxychains [y/n]')
if(proxy != 'n'):
  os.system('qterminal bash ./anonymity/proxies.sh')
macchanger = input('apply macchanger [y/n]')
if(macchanger != 'n'):
  os.system('bash ./anonymity/mac_address.sh')
