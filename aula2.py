import math

#Exercicio 4.1
impar = lambda y : False if y % 2 == 0 else True

#Exercicio 4.2
positivo = lambda y : True if y > 0 else False

#Exercicio 4.3
comparar_modulo = lambda z, w : True if abs(z) < abs(w) else False

#Exercicio 4.4
cart2pol = lambda z,w : (math.sqrt(z*z + w*w), math.atan2(w,z))

#Exercicio 4.5
ex5 = lambda f, g, h : lambda x, y, z: h ( f(x, y), g(y, z) )

#Exercicio 4.6
def quantificador_universal(lista, f):
    h = lambda x, y : False if [False for m in x if y(m) != True] == True else True
    return h(lista, f)

#Exercicio 4.9
def ordem(lista, f):
    for x in range(0,len(lista)-1):
        if f(lista[x], lista[x+1]):
            save = lista[x]
    return save

#Exercicio 4.10
def filtrar_ordem(lista, f):
    for x in range(0,len(lista)-1):
        if f(lista[x], lista[x+1]):
            save = lista[x]
    for x in lista:
        if x == save:
            lista.remove(x)
    return (save, lista)

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    lst = []
    for y in range(0, len(lista)):
        print(lista)
        for x in range(0,len(lista)-1):
            print("\t " + str(x))
            if ordem(lista[x], lista[x+1]):
                lst.append(lista[x])
                lista.remove(lista[x])
                break
    return lst