from ipaddress import *
ip = ("192.214.116.184")

for mask in range(1, 32):
    i = ip_interface(f'{ip}/{mask}')

