"""
Peça ao usuário para inserir um número. 
Continue perguntando até que ele insira 5 números e em seguida exiba a mensagem: 
“O último número que você digitou foi: [num]” e pare o programa.
"""

i = 0

while i < 5:
    num = int(input("Digite o {}º número: ".format(i)))

print("O último número que você digitou foi : {}".format(num))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")