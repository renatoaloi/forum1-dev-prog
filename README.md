# forum1-dev-prog
Lista é uma estrutura de dados do tipo sequencial que possui como principal característica ser mutável. Ou seja, novos valores podem ser adicionados ou removidos da sequência. Sabendo disso, desenvolva um código em Python, para um problema da sua escolha, que possua lista como estrutura de dados e o for como estrutura de repetição.

## Criador de lista numérica

Criei um programa para que o usuário possa inserir números em uma lista e depois ter todos os números somados. Para sair do modo de inserção da lista, o usuário precisa digitar a letra "X"

## Código

```
lista_compras = []
print("### Aplicativo de lista de compras ###")
print("Digite os produtos que deseja adicionar na lista e tecle <ENTER>")
print("Para terminar e imprimir a lista, digite -1 e tecle <ENTER>")
r = input("Digite o primeiro item da lista: ")
while r != -1:
  lista_compras.append(r)
  r = input("Digite outro item (-1=sair): ")
print(lista_compras)
```
