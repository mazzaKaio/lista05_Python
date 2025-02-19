"""
Faça um programa que leia os números digitados pelo usuário, a cada número digitado, ele deve ser somado ao anterior e a cada soma deve ser exibida na tela. 
Quando a soma for superior a 50 ele deve exibir a mensagem “O total é: [total]” e parar o programa.
"""

somaTotal = 0

while somaTotal < 50:
    num = int(input("Digite um número para a soma: "))
    somaTotal += num

print("A soma total é: {}".format(somaTotal))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")