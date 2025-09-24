# Formatação de Strings - f-strings

from datetime import datetime

frutas = ['Jabuticaba', 'Laranja', 'Uva', 'Banana']
for fruta in frutas:
    minha_fruta = f'Nome: {fruta:12} - Número de letras: {len(fruta): 3}' #fruta:12 imprime a fruta em um campo com 12 caracteres e len(fruta):3 imprime o número de letras, alinhado à direita
    print(minha_fruta)

print()

pi = 3.1415
meu_numero = f'O número PI é: {pi:.1f}' #Mostra PI com uma cada decimal - f formato de float
meu_numero_deslocado = f'O número PI deslocado é: {pi:6.1f}' # largura mínima de 6 caracteres, com uma casa decimal - o número vai ser empurrado para a direita se ocupar menos de 6 caracteres
meu_numero_preciso = f'O número PI mais preciso é: {pi:.4f}'
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f'A data de hoje é {data}' #Imprime a data completa com hora e formatada
minha_data_formatada = f'A data de hoje formatada é {data:%d/%m/%Y}'
print(minha_data)
print(minha_data_formatada)




