import threading

#lock 객체 생성
lock = threading.Lock()

#데이터 영역 : 공유 메모리 공간의 전역 변수 선언
count_global = 0

def thread_main():
    global count_global
    lock.acquire() #lock 획득
    for i in range(100000):
        count_global +=1
    lock.release() #lock 반환
threads = []
for i in range(50):
    th = threading.Thread(target = thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print("count_global : {:,}".format(count_global))

    
