#Exercicio 1.1
def comprimento(lista):
	if not lista:
		return 0
	else:
		return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	if not lista:
		return 0
	else:
		return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if not lista:
		return False
	else:
		if lista[0] == elem:
			return True
		return existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
	if l2 == []:
		return l1
	else:
		return concat(l1 + [l2[0]], l2[1:])

#Exercicio 1.5
def inverte(lista):
	if not lista:
		return []
	else:
		return inverte(lista[1:]) + [lista[0]]

#Exercicio 1.6
def capicua(lista):
	if lista == []:
		return True
	elif lista[0] == lista[-1]:
		return capicua(lista[1:len(lista)-1])
	else:
		return False

#Exercicio 1.7
def explode(lista):
	if not lista:
		return []
	else:
		prev = explode(lista[1:])
		return lista[0] + prev

#Exercicio 1.8
def substitui(lista, original, novo):
	if not lista:
		return []
	else:
		prev = substitui(lista[1:], original, novo)
		if lista[0] == original:
			return [novo] + prev
		return [lista[0]] + prev

#Exercicio 1.9
def junta_ordenado(lista1, lista2):
	if not lista2:
		return lista1
	if not lista1:
		return lista2
	else:
		if lista1[0] < lista2[0]:
			return [lista1[0]] + junta_ordenado(lista1[1:], lista2)
		elif lista2[0] < lista1[0]:
			return [lista2[0]] + junta_ordenado(lista1, lista2[1:])
		else:
			return [lista2[0]] + [lista1[0]] + junta_ordenado(lista1[1:], lista2[1:])

#Exercicio 2.1
def separar(lista):
	if not lista:
		return [],[]
	else:
		lst1, lst2 = separar(lista[1:])
		lst1 = [lista[0][0]] + lst1
		lst2 = [lista[0][1]] + lst2
		return lst1, lst2

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if not lista:
		return [], 0
	else:
		lst, num = remove_e_conta(lista[1:], elem)
		if lista[0] == elem:
			num=num+1
		else:
			lst = [lista[0]] + lst
		return (lst, num)

#Exercicio 3.1
def cabeca(lista):
	pass

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
	if len(l1) != len(l2):
		return None
	if not l1 or not l2:
		return []
	else:
		return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])

#Exercicio 3.4
def menor(lista):
	if len(lista) == 0:
		return None
	else:
		minimo = menor(lista[1:])
		if minimo == None:
			return lista[0]
		if lista[0] < minimo:
			return lista[0]
		return minimo

#Exercicio 3.6
def max_min(lista):
	pass
