import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = input("Enter IP or Domain Name: ")

q = Queue()

def scan_port(port):
    s = socket.socket()
    s.settimeout(1)
    try:
        result = s.connect_ex((target, port))
    except socket.gaierror:
        return
    except socket.error:
        return

    if result == 0:
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner="no banner"
        print(f"Port {port}: OPEN | {banner}")
    
    s.close()

def threader():
    while True:
        port=q.get()
        scan_port(port)
        q.task_done()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon=True
    t.start()

for port in range(1,1024):
    q.put(port)

q.join()
print("scan complete")
