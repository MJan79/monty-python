program = True
while program == True:
  from os import system, name
  #Definitions
  ip_addr_list = []
  ip_subnet_list = []
  bin_ip_addr_list = []
  bin_subnet_list = []
  ip_class = ""
  ip_range = ""
  cidr = 0
  subnet_bits = 0
  subnet_value = 0
  
  def clear():
		# for windows
	  if name == 'nt':
	    _ = system('cls')
		# for mac and linux(here, os.name is 'posix')
	  else:
	    _ = system('clear')

  def cidr_conversion():
    cidr_to_bin = int(subnet_input[1:])
    subnet_bits = (cidr_to_bin * "1").ljust(32,"0")
    for subnet_bit in range(0, len(subnet_bits),8):   
      ip_subnet_list.append(subnet_bits[subnet_bit:subnet_bit + 8])
    subnet_1octet = ip_subnet_list[0].zfill(8)
    subnet_2octet = ip_subnet_list[1].zfill(8)
    subnet_3octet = ip_subnet_list[2].zfill(8)
    subnet_4octet = ip_subnet_list[3].zfill(8)
   
    dec_subnet_1octet = int(subnet_1octet,2)
    dec_subnet_2octet = int(subnet_2octet,2)
    dec_subnet_3octet = int(subnet_3octet,2)
    dec_subnet_4octet = int(subnet_4octet,2)
    print(f"Subnet mask in decimal:\t {dec_subnet_1octet}.{dec_subnet_2octet}.{dec_subnet_3octet}.{dec_subnet_4octet}")
    print(f"Subnet mask in binary:\t {subnet_1octet}.{subnet_2octet}.{subnet_3octet}.{subnet_4octet}")
    cidr = subnet_input[1:]
    print(f"\nCIDR notation:\t\t\t /{cidr}")
    cidr = int(cidr)
  
#Hosts
    
    host_bits = 32 - (cidr)
    number_of_hosts= (2 ** (host_bits)) - 2
    print(f"Number of hosts:\t\t {number_of_hosts}")
  
#Subnets
    if cidr == 8 or cidr == 16 or cidr == 24:
      subnet_bits = 0
    elif cidr > 24:
      subnet_bits = cidr - 24
    elif cidr > 16 and cidr < 24:
      subnet_bits = cidr - 16
    elif cidr > 8 and cidr < 16:
      subnet_bits = cidr - 8
    number_of_subnets = 2 ** subnet_bits
    print(f"Number of subnets:\t\t {number_of_subnets}")
  
    print("\nNetwork addresation available only for up to 10 class C networks")
  
    network_nr = 1
    ip_net_addr = 0
    ip_1st_use_addr = 0
    ip_last_use_addr = 0
    ip_broadcast = 0
   
    while ip_class == "C" and network_nr <= number_of_subnets and network_nr < 10:
      print(f"\nNetwork #{network_nr}")
      if ip_class == "C":
        print(f"Network address: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_net_addr}")
        ip_1st_use_addr += ip_net_addr + 1
        
        print(f"First usable IP: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_1st_use_addr}")
  
        ip_last_use_addr = ip_net_addr + number_of_hosts
        print(f"Last usable IP: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_last_use_addr}")
        ip_broadcast = ip_1st_use_addr + number_of_hosts
        print(f"Broadcast address: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_broadcast}")
        
      network_nr += 1
      ip_net_addr = ip_broadcast + 1
      ip_1st_use_addr = 0
      ip_last_use_addr  = 0
      ip_broadcast = 0
    
  def ip_mask():
    #subnet added to ip_subnet list
    ip_subnet_list = subnet_input.split(".")
    #print(ip_subnet_list)
    #subnet octets decimal

    subnet_1octet = int(ip_subnet_list[0])
    subnet_2octet = int(ip_subnet_list[1])
    subnet_3octet = int(ip_subnet_list[2])
    subnet_4octet = int(ip_subnet_list[3])
    print(f"Subnet mask in decimal:\t {subnet_1octet}.{subnet_2octet}.{subnet_3octet}.{subnet_4octet}")
      #subnet octets binary
    bin_subnet_1octet = bin(subnet_1octet)[2:].zfill(8)
    bin_subnet_2octet = bin(subnet_2octet)[2:].zfill(8)
    bin_subnet_3octet = bin(subnet_3octet)[2:].zfill(8)
    bin_subnet_4octet = bin(subnet_4octet)[2:].zfill(8)
    print(f"Subnet mask in binary:\t {bin_subnet_1octet}.{bin_subnet_2octet}.{bin_subnet_3octet}.{bin_subnet_4octet}\n")
    
    #subnet octet binary list
    bin_subnet_list = [bin_subnet_1octet,bin_subnet_2octet,bin_subnet_3octet,bin_subnet_4octet]
   
    #CIDR notation
    cidr=0
    for octet in range(0,len(bin_subnet_list)):
      for bit in bin_subnet_list[octet]:
        bit=int(bit)
        if bit == 1:
          cidr += 1
    print(f"CIDR notation:\t\t\t /{cidr}")
  
      #Hosts
    # cidr = 24
    host_bits = 32 - (cidr)
    number_of_hosts= (2 ** (host_bits)) - 2
    print(f"Number of hosts:\t\t {number_of_hosts}")
  
      #Subnets
    if cidr == 8 or cidr == 16 or cidr == 24:
      subnet_bits = 0
    elif cidr > 24:
      subnet_bits = cidr - 24
    elif cidr > 16 and cidr < 24:
      subnet_bits = cidr - 16
    elif cidr > 8 and cidr < 16:
      subnet_bits = cidr - 8
    number_of_subnets = 2 ** subnet_bits
    print(f"Number of subnets:\t\t {number_of_subnets}")
  
    print("\nNetwork addresation available only for up to 10 class C networks")
  
    network_nr = 1
    ip_net_addr = 0
    ip_1st_use_addr = 0
    ip_last_use_addr = 0
    ip_broadcast = 0
   
    while network_nr <= number_of_subnets and network_nr < 10:
      print(f"\nNetwork #{network_nr}")
      if ip_class == "C":
        print(f"Network address: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_net_addr}")
        ip_1st_use_addr += ip_net_addr + 1
        
        print(f"First usable IP: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_1st_use_addr}")
  
        ip_last_use_addr = ip_net_addr + number_of_hosts
        print(f"Last usable IP: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_last_use_addr}")
        ip_broadcast = ip_1st_use_addr + number_of_hosts
        print(f"Broadcast address: \t\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_broadcast}")
        
      network_nr += 1
      ip_net_addr = ip_broadcast + 1
      ip_1st_use_addr = 0
      ip_last_use_addr  = 0
      ip_broadcast = 0 
  
  #program start
  clear()
  print("Subnet calculator v 1.0\n")
  #Input validation
  parseIP = False
  parseSUB = False
  
  while not parseIP:
  #IP Input 
    ip_input=input("Enter the IP address in x.x.x.x format\n")
    if ip_input.find(".",0,4) != -1:
      try: 
        ip_addr_list = ip_input.split(".")
        ip_1octet = int(ip_addr_list[0])
        ip_2octet = int(ip_addr_list[1])
        ip_3octet = int(ip_addr_list[2])
        ip_4octet = int(ip_addr_list[3])
        parseIP = True
        if ip_1octet > 255 or ip_2octet > 255 or ip_3octet > 255 or ip_4octet > 255:
              clear()
              print("Invalid IP range!")
              parseIP = False
     
      except:
        clear()
        print("This is not a valid IP address format!")
      
        parseIP = False
        
    else:
      clear()
      print("This is not a valid IP address format!")
      parseIP = False
  ParseIP = True    

  while not parseSUB:

    #Subnet input
    subnet_input=input("Enter the subnet in x.x.x.x OR /x (CIDR) format\n")
    if subnet_input.find("/",0,1) != -1:
      try:
        
        subnet_value = int(subnet_input[1:])
        parseSUB = True
        if subnet_value < 8 or subnet_value > 30:
          clear()
          print("This is not a valid CIDR value!")
          parseSUB = False
      except:
        clear()
        print("This is not a valid subnet mask!")
      
        parseSUB = False
          
    elif subnet_input.find(".",0,4) != -1:
      try:
        ip_subnet_list = subnet_input.split(".")
        sub_1octet = int(ip_subnet_list[0])
        sub_2octet = int(ip_subnet_list[1])
        sub_3octet = int(ip_subnet_list[2])
        sub_4octet = int(ip_subnet_list[3])
        print(ip_subnet_list)
        parseSUB = True
        if sub_1octet > 255 or sub_2octet > 255 or sub_3octet > 255 or sub_4octet > 255:
              clear()
              print("This is not a valid subnet mask!")
              parseSUB = False
      except:
        clear()
        print("This is not a valid subnet mask!")
      
        parseSUB = False
          
    else:
      clear()
      print("This is not a valid subnet mask!")
      parseSUB = False
  parseSUB = True  
        
  clear()
  print("\nNETWORK INFORMATION")
  print(f"\nIp address in decimal:\t {ip_1octet}.{ip_2octet}.{ip_3octet}.{ip_4octet}")

  #IP octets binary
  bin_1octet = bin(ip_1octet)[2:].zfill(8)
  bin_2octet = bin(ip_2octet)[2:].zfill(8)
  bin_3octet = bin(ip_3octet)[2:].zfill(8)
  bin_4octet = bin(ip_4octet)[2:].zfill(8)
  print(f"Ip address in binary:\t {bin_1octet}.{bin_2octet}.{bin_3octet}.{bin_4octet}\n")
  
  #IP octets binary list
  bin_ip_addr_list = [bin_1octet,bin_2octet,bin_3octet,bin_4octet]
  
  #IP class A
  
  if ip_1octet in range(1,127):
    ip_class = "A"
    if ip_1octet == 10:
      ip_range = "Private"
    else:
      ip_range = "Public"
  
  #IP class B
  if ip_1octet in range(128,191):
    ip_class = "B"
    if ip_1octet == 172 and ip_2octet in range(16,31):
      ip_range = "Private"
    else:
      ip_range = "Public"
  
  #IP class C
  if ip_1octet == 127:
    ip_class = "Special"
  elif ip_1octet in range(192,223):
      ip_class = "C"
  if ip_1octet == 192 and ip_2octet == 168:
        ip_range = "Private"
  else:
      ip_range = "Public"
      
  print(f"IP class \t\t\t\t {ip_class}") 
  print(f"IP range \t\t\t\t {ip_range}\n")  

  if subnet_value > 0:
    cidr_conversion()
  else:
    ip_mask()
  
  end = input("\nDo you want to check a different IP / subnet ?\nY/N\n").lower()
  if end == "y":
    program = True
  else:
    clear()
    program = False
      
  
  
  
  
  
  
  
      
  
  
    



