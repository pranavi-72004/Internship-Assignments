import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter IP Address: ")

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        if sock.connect_ex((target, port)) == 0:
            print(f"Port {port} OPEN")

        sock.close()

    except:
        pass

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan, range(1, 1025))

print("Scan Completed")
