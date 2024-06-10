from threading import Thread
from queue import Queue
import socket
import time
import sys


timeout = 1.0

def check_port(host: str, port: int, results: Queue):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    if result == 0:
        results.put(port)
    sock.close()

def main():
    if len(sys.argv) - 1 != 3:
        print("Usage: scan host startPort endPort")
        return

    host,startPort,endPort = sys.argv[1:]
    start = time.time()
    threads = []
    results = Queue()
    for port in range(int(startPort), int(endPort)):
        t = Thread(target=check_port, args=(host, port, results))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    while not results.empty():
        print("Port {0} is open".format(results.get()))
    print("Completed scan in {0} seconds".format(time.time() - start))

if __name__ == '__main__':
    main()
