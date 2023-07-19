# A port scanner that will take an IP addr 
# and a list of ports as input then test 
# of any response from the listed ports. 
# 

from socket import *

def conScan(tgthost, tgtPort):
    try:
        connection = socket(AF_INET, SOCK_STREAM)
        connection.connection((tgthost, tgtPort))
        print(f'[+]{tgtPort}/tcp open')
        connection.close()
    except:
        print(f'[-]{tgtPort}/tcp closed')

if __name__ == '__main__':

