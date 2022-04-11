####################################
#
#    IPsec between UE and UPF
#    Abdul Aziz/Hussaini/Ezekiel
#    Carleton University
#
####################################

from scapy.all import * 
from scapy.config import conf 


sock = conf.L3socket(iface='eth0') 
 
# Creating Packet 
p = IP(src='192.187.3.254', dst='192.187.3.253') 
p /= UDP(sport=45012, dport=80) 
p /= Raw('username_password') 
p = IP(raw(p)) 

print("*** Sending Username and Password using Plaintext ***") 
print("Packet:") 
print(p.show(dump=True)) 
print("Sending Packet from UE1...") 
print("Packet sent successfully.") 

sock.send(p) # Sending Packet 


# Encrypting Packet with IPSec 

sa = SecurityAssociation(ESP, spi=0x222, 

                         crypt_algo='NULL', crypt_key=None, 

                         auth_algo='NULL', auth_key=None) 

e = sa.encrypt(p)

print("*** Sending Username and Password using IPSec ***") 
print("Packet:") 
print(e.show(dump=True)) 
print("Sending Packet from UE1...") 
print("Packet sent successfully.") 

sock.send(e) # Sending Packet 
