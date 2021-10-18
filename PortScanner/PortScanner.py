import sys
import time
import socket
import platform
import subprocess


"""
Simple, but inefficient port scanner example in python.
Needs added multi-threading to be faster, right now this
is unusable in any real scenario as it is too slow, but
still serves a good educational purpose.
"""


# Test Connection to target host
def ping(target): 
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    return subprocess.call(['ping', param, '1', target]) == 0

def resolveHostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        print("Can not resolve hostname")
        sys.exit(1)

class portScanner:
    def tcpScan(self, target, portRange):
        for port in portRange:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                if sock.connect_ex((target, port)) == 0: print(f'Port {port} open')             
                sock.close()
            except socket.error:
                print("Can not establish connection to host")
                sys.exit(1)
            except KeyboardInterrupt:
                print("KeyboardInterrupt, exiting...")
                sys.exit(1)
                
def main():
    resolved = resolveHostname('target.example.com')

    if ping(resolved) == False:
        print("ERROR: Can not establish connection to host.")
        sys.exit(1)

    print(f"\nInitiating reconnaissance on host: {resolved}:\n")
    portScanner().tcpScan(resolved, range(20,81))

if __name__ == '__main__':
    main()
    sys.exit(0)



