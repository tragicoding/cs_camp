"""
인덱스 0부터 1000까지 리스트의 모든 요소를 2배 하는 프로세스
250개 씩 4개로 나누어 4개의 멀티 스레드의 실행을 구현하는 것이 목표
"""

import threading

#li를 offset개씩 쪼개서 연산될 함수
def thread_main(li,i):
    for k in range(offset*i, offset*(i+1)):
        li[k]


num_elem = 1000 #연산될 총 정수 개수
num_thread = 4 #스레드 개수

#각 스레드 별 250개씩 실행
offset = num_elem//num_thread

li = [i+1 for i in range(num_elem)]

#thread 객체 생성
threads = []
for i in range(num_thread):
    th = threading.Thread(target=thread_main,args=(li,i))
    threads.append(th)

#실행 대기 상태로 만든다.
for th in threads:
    th.start()

#실행종료 까지 기다린다.
for th in threads:
    th.join()