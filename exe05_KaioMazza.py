"""
Crie uma variável chamada “adivinha” e defina o valor como 50. 
Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, 
diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".
"""

advinha = 50
num = 0

while num != advinha:
    num = int(input("Advinhe o número definido pela máquina: "))

    if num > advinha:
        print("\nNúmero {} é MAIOR que número estabelecido!".format(num))
    elif num < advinha:
        print("\nNúmero {} é MENOR que número estabelecido!".format(num))
    else:
        print("\nVocê acertouuu!!!\nUm beijo e um abraço")
        break

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")