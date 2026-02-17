import symtable

s = open('test.py', encoding = 'utf-8').read()

sym = symtable.symtable(s,'test.py','exec')

print(sym.get_name())
print(sym.get_symbols())
print(sym.get_children())

func_sym = sym.get_children()[0]
print(func_sym.get_name())
print(func_sym.get_symbols())