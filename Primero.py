#ejercicio 1
lista = [(1,2,44,22,66),(22,3,4,5),(3,4,1,7)]
resultado = list(map(lambda x: (x[0],x[-1]), lista))
print (resultado)


#ejercicio 3
lista = [(1,2,3),(2,3,4,5),(3,4,1,7)]
resultado = list(map(lambda x: max(x), lista))
print (resultado)