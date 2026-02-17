import token

tok = token.tok_name
with open('python_token.txt', 'w', encoding='utf-8') as out:
    for k in sorted(tok):
        line = f"{k}\t{tok[k]}"
        print(line)
        out.write(line + "\n")