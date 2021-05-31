#!/usr/bin/env python3

import socket
import threading
import queue
import time

def portscan(server, port, q):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Connecting to {server} on port {port}...')
    try:
        s.settimeout(3)
        s.connect((server,port))
        s.close()
        q.put(port)

    except:
        q.put('')



if __name__ == '__main__':
    target = '40.74.127.249'
    q = queue.Queue()
    ports, threads = [], []
    start = time.perf_counter()
    # Multi-threading to simultaneous port sweep network target
    for i in range(1000, 5700):
        t = threading.Thread(target=portscan, args=(target, i, q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
        ports.append(q.get())
    end = time.perf_counter()

    print(f'Discovered open ports: {list(filter(None, ports))}')
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)} secs')
