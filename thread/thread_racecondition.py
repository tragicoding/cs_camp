import threading

count_global = 0

def thread_main():
    global count_global
    for i in range(100000):
        count_global +=1

threads = []
for i in range(50):
    th = threading.Thread(target = thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print("count_global : {:,}".format(count_global))
    

