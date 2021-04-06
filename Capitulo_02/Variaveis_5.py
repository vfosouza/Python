nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
# prioridade="NÃO"
if idade>=65:
    # prioridade="SIM"
    print("O paciente " + nome + " POSSUI atendimento prioritário? ")
# else:
if idade<65:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")