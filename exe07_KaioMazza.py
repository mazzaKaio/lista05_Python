"""
Escreva um programa que permaneça em laço lendo números inteiros. 
O laço termina quando for digitado 0 (zero).
Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
Ao final exiba a lista e a quantidade de elementos que ela contém.
"""
num = 1
numeros = []

while num != 0:
    num = int(input("Digite um número: "))
    
    if num not in numeros:
        numeros.append(num)
        print("\nNúmero adicionado!")
    else:
        print("\nNúmero já está na lista!")

print("\nDentro da lista há {} números!".format(len(numeros)))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")