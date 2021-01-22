"""
    Loop for
    
    loop -> estrutura de repeticao
    for -> uma dessa estruturas 

Java
    for(i = 0; i < 10; i++){
        //execucao do loop
    }


python
    for item in interavel:
        //execucao do loop


utilizamos loop para iterar sobre sequencias ou sobre valores iteraveis

"""

# Exemplo de for 1

nome = 'Igor Pereira Dutra'
lista = [1, 2, 4, 5, 6]
numeros = range(1, 10)

#iterando em uma string
for letra in nome:
    print(letra, end='')

#iterando sobre uma lista
for numero in lista:
    print(numero, end='')

#exemplo de for 3 iterando sobre um range
for numero in range(1, 10):
    print(numero)

for i, letra in enumerate(nome):
    print(nome[i])

for valor in enumerate(nome):
    print(valor)

qtd = int(input("quantas vezes esse loop deve rodar?"))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')