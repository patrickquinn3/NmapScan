# Simple Nmap scanner
# The goal of this program is find out what ports are open/closed 
# at the target IP address

# Install Nmap library for python: pip install python-nmap

# library
import nmap # nmap is an open source port scanning tool

# port scan range
begin = 1
end = 100

# assign target IP address
target = 'x.x.x.x'

# initiate PortScanner object
scanner = nmap.PortScanner()

for i in range(begin,end+1):
    # scna the target port
    res = scanner.scan(target,str(i))

    # this scanner will be limited to only show open/close status
    res = res['scan'][target]['tcp'][i]['state']

    print(f'port {i} is {res}.')
