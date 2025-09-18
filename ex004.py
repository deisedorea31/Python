#Manipulação de string usando método strip

arquivo = open(r'C:\Users\jr\OneDrive\Desktop\PYTHON\Scripts\ex003.py', 'r', encoding='utf-8')
conteudo = arquivo.read()
print('Tipo de conteúdo:', type(conteudo))
print('Conteúdo retornado pelo read:')
print(repr(conteudo))
arquivo.close()