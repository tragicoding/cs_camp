from tokenize import tokenize
from io import BytesIO

#test.py 열고 읽기. 인코딩은 utf-8
s = open('test.py',encoding='utf-8').read()

#토큰 결과를 한줄 씩 읽어서 g 에 저장
g = tokenize(BytesIO(s.encode('utf-8')).readline)

#결과 저장 및 출력
with open('test_token', 'w', encoding='utf-8') as out:
    for token in g:
        out.write(str(token) + '\n')
        print(token)