"""
Peça ao usuário para inserir um número entre 15 e 20.
Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".
"""

num = 0

while num < 15 or num > 20:
    num = int(input("\nDigite um valor ENTRE 15 e 20: "))

    if num < 15:
        print("Muito baixo!")
    elif num > 20:
        print("Muito alto!")
    else:
        print("Obrigado!")

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")