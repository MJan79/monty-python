
import socket
import ipaddress
from os import system, name

def clear():
  if name == "nt":
     _ = system('cls')
  else:
    _ = system('clear')

def scan(target,ports):
  for port in range(1, ports + 1):
    scan_port(target,port)

def scan_port(ipaddress,port):
  try:
    soc = socket.socket()
    soc.connect((ipaddress, port))
    soc.settimeout(0.2)
    print(f"[*] Port opened: {port}")
  except:
    print(f"[ ] Port closed: {port}")

clear()

parse_port=False
parse_ip=False
targets_list=[]

while not parse_ip:
  targets = input("Enter target(s) IP addresses separated by ','\n")
  targets_list = targets.split(",")
  try:
    for item in targets_list:
      ipaddress.ip_address(item)
      parse_ip = True
  except:
    clear()
    print("Invalid IP format!")

while not parse_port:
  ports = input("\nEnter how many ports you want to scan\n")
  try:
    ports = int(ports)
    parse_port = True
  except:
    clear()
    print("Enter correct port number!")


for item in targets_list:
    print(f"\nScanning ports for IP: {item}")
    scan(item,ports)



