"""#인덱스 0부터 1000까지의 정수가 담긴 리스트의 각 요소들에
2를 곱하는 프로세스 생성
"""

list = [i for i in range(1001)]
for idx in range(1001):
    list[idx] *= 2
