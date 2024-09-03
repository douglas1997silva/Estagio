
#1 - questão 
print('1 - questão  ')
indice = 13
soma = 0
k = 0

if k < indice:
    k = k +1
    soma = soma + k
    print(soma)


#2 - questão 
print('2 - questão  ')
numero = 20
soma_anterior = 0

for mais in range(0, numero + 1):
    soma_atual = soma_anterior + mais
    print(soma_atual)
    soma_anterior = soma_atual


#3 - questão 
print('3 - questão  ')
faturamento_diario = [1000, 850, 1500, 900, 720, 1100, 2000, 500, 950, 780]


soma_total = sum(faturamento_diario)

maior = max(faturamento_diario)
menor = min(faturamento_diario)
media_mensal = soma_total / len(faturamento_diario)


dias_acima_da_media = 0

for faturamento in faturamento_diario:
    if faturamento > media_mensal:
        dias_acima_da_media += 1

print(f'o maior valor foi : {maior}')
print(f'o menor valor foi : {menor}')
print(f"O número de dias com faturamento superior à média mensal foi: {dias_acima_da_media}")

#4 - questão 
print('4 - questão  ')

valores = {
    'SP': 67.83643,
    'RJ':36.67866,
    'MG':29.22988,
    'OUTROS':19.84953

}   

total_distribuitora = sum(valores.values())

porcetagem = 100 *( len(valores) / total_distribuitora )
print(porcetagem)
print(total_distribuitora)




#5 - questão 
print('5 - questão  ')


string = input('Digite um Texto:')


nova_string = ""


for i in range(len(string) - 1, -1, -1):
  
    nova_string += string[i]


print(nova_string)
