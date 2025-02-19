"""
Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. 
Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
Em seguida, pergunte se ele quer convidar outra pessoa.
Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.
"""

convidado = input("Digite o nome do convidado: ")
print("{} foi adicionado(a) com sucesso no convite!".format(convidado))
contagemConvidados = 1

confirmacao = input("Você deseja convidar mais alguém [s/n]: ").lower()

while confirmacao.__eq__("s"):
    convidado = input("\nDigite o nome do convidado: ")
    print("{} foi adicionado(a) com sucesso no convite!".format(convidado))
    contagemConvidados += 1

    confirmacao = input("Você deseja convidar mais alguém? [s/n]: ").lower()

print("\n{} pessoas foram convidadas para a festa!".format(contagemConvidados))

print("\nFim do programa!")
print("Kaio Gomes do Nascimento Mazza")