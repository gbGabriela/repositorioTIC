#criar uma lista vazia
lista = []

#criar uma lista com tamanho 10
lista2= [""]*10

#adicionar elemento na lista
lista.append(5)
lista.append(18)
lista.append(3)
lista.append(11)
lista.append(15)
lista.append(4)

#alterar o valor de uma lista
lista[3] = 44

print("Resultado da lista: ", lista)

#calcular o tamanho de uma lista
tamanho = len(lista)
i = 0

#usando while
while i < tamanho:

    #print("Na posição ", i, "tem o valor ", lista[i])
    print("Na posição {} tem o valor {}.".format(i, lista[i]))
    i += 1

print("===================================\n")
#usando o for molesa master foreach
for x in lista:
    print("Valor da lista: ",x)

print("===================================\n")
#uso do for normal
for i in range(len(lista)):
    print("Na posição {} tem o valor {}.".format(i, lista[i]))

print("===================================\n")
#criação de função
def dobro(numero):
    d = numero*2
    print("O dobro de {} é {}.".format(numero, d))
    return d, numero

a, b = dobro(5)
print("Os retornos são: {} e {}.".format(a, b))
