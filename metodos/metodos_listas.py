lista = list(["Hola", "Dalto", 35,36,37,True])
print(lista)
resultado = len(lista)
print(resultado)

lista.append("Nuevo elemento")
print(lista)

lista.insert(2, "Elemento en posición 3")
print(lista)

lista.extend(["Otro elemento", 123])
print(lista)    

lista.pop(0)
lista.pop(-1)
lista.pop(-2)
print(lista)

lista.remove("Dalto")
print(lista)

lista.clear()
print(lista)

lista = list([1,8,3,6,35,36,37,4,2,7,5])
lista.sort()
print(lista)    
#lista.sort(reverse=True)
lista.reverse()
print(lista)

#print(dir(lista))
#print(dir(('a', 5)))

elemento_encontrado = lista.index(35)
print(elemento_encontrado)