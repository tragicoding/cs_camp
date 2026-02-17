import ast

s = open('test.py', encoding='utf-8').read()

node = ast.parse(s, 'test.py', 'exec')
g = ast.walk(node)
print(next(g))
print(next(g))
print(next(g))
