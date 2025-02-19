"""
Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
Depois que o loop for interrompido, exiba o total.
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))
somaTotal = num1 + num2

print("\nA soma dos números é: {}".format(somaTotal))
confirmacao = input("Agora, digite se você quer somar mais um número [s/n]: ").lower()

while confirmacao.__eq__("s"):
    num1 = int(input("\nDigite um número: "))
    somaTotal += num1
    confirmacao = input("Você quer somar mais um número [s/n]: ").lower()

print("\nA soma total ficou: {}!!!".format(somaTotal))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")