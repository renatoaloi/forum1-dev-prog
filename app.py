lista_compras = []

print("### Aplicativo de lista de compras ###")
print(" ")
print("Digite os produtos que deseja adicionar na lista e tecle <ENTER>")
print("Para terminar e imprimir a lista, digite -1 e tecle <ENTER>")
print(" ")
r = input("Digite o primeiro item da lista: ")
while r != "-1":
    lista_compras.append(r)
    r = input("Digite outro item (-1=sair): ")

print(" ")
print(" ")
print("----------- Sua lista de compras -----------------")
print("-"*50)
print(lista_compras)
print("-"*50)
contador = 1
for item in lista_compras:
    print("#{} - {}".format(contador, item))
    contador += 1
print("-"*50)