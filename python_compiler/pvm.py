import dis

s = open('test.py', encoding = 'utf-8').read()

g = dis.get_instructions(s)

with open('byte_code.txt', 'w', encoding = 'utf-8') as out:
    for inst in g:
        name = inst.opname.ljust(20)
        value = inst.argval
        print(name, end = ' ')
        print(value)
        out.write(str(name))
        out.write(str(value) + "\n")
        


