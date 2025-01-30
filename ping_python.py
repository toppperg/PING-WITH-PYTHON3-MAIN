from pythonping import ping


no_to_ping=int(input("Enter how many times you want to ping: "))
set_timeout=int(input("Enter how much time to wait if host is unreachable: "))
ip_addres=str(input("Enter ip address: "))
ping(ip_addres, verbose=True, count=no_to_ping, timeout=set_timeout)