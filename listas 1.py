nomes = []

while True:
    nome = input("Digite um nome (ou 'sair'): ")
    if nome == "sair":
        break
    nomes.append(nome)

buscar = input("Qual nome você quer contar? ")

print("Quantidade:", nomes.count(buscar))
