from random import randrange


def tablero():
	# Creación de tablero
	lista = [0 for i in range(8)]
	for i in range(8):
		lista[i] = [0 for i in range(8)]

	reinas = []

	if(n != 8):
		lista[0][6] = 1
		lista[2][2] = 1
		lista[4][5] = 1
		valor = [0,6]
		reinas.append(valor)
		valor = [2,2]
		reinas.append(valor)
		valor = [4,5]
		reinas.append(valor)
		if(n == 4):
			lista[7][3] = 1
			valor = [7,3]
			reinas.append(valor)
		elif(n == 3):
			lista[6][1] = 1
			valor = [6,1]
			reinas.append(valor)
			lista[7][3] = 1
			valor = [7,3]
			reinas.append(valor)

	return lista,reinas


def aleatorio(nuevasr):
	x = randrange(8)
	y = randrange(8)

	if(n==3 or n==4 or n==5):
		if((x==0 and y==6) or (x==2 and y==2) or (x==4 and y==5)):
			return -1,-1
		if(n == 4):
			if(x==7 and y==3):
				return -1,-1
		elif(n == 3):
			if((x==6 and y==1) or (x==7 and y==3)):
				return -1,-1

	for i in range(len(nuevasr)):
		if(x==nuevasr[i][0] and y==nuevasr[i][1]):
			return -1,-1

	return x,y

def validacion(reinas):
	for i in range(8):
		#Validación vertical
		if(reinas[i].count(1)>1):
			return False
		#Validación horizontal
		count = 0
		countdia = 0
		countdia2 = 0
		diax = i-1
		diay = -1
		for j in range(8):
			if(reinas[j][i]==1):
				count += 1
				if(count>1):
					return False
			if(diay<7 and diax<7):
				if(reinas[diax+1][diay+1]==1):
					countdia += 1
					if(countdia>1):
						return False
				if(reinas[diay+1][diax+1]==1):
					countdia2 += 1
					if(countdia2>1):
						return False
				diay += 1
				diax += 1

	for i in range(7,-1,-1):
		countdia = 0
		countdia2 = 0
		diax = 8-i
		diay = -1
		for j in range(8):
			if(diay<7 and diax>0):
				if(reinas[diax-1][diay+1]==1):
					countdia += 1
					if(countdia>1):
						return False
				if(reinas[diay+1][diax-1]==1):
					countdia2 += 1
					if(countdia2>1):
						return False
				diay += 1
				diax -= 1

	return True




n = int(input("Número de reinas aleatorias: "))
r = int(input("Número de repeticiones: "))
solucion = 0

for i in range(r):
	lista,reinas = tablero()
	nuevasr = []

	for j in range(n):
		x,y=-1,-1
		while(x==-1 and y==-1):
			x,y = aleatorio(nuevasr)

		lista[x][y] = 1
		val = [x,y]
		nuevasr.append(val)

	#reinas.extend(nuevasr)
	#print(reinas[:])
	if(validacion(lista)==True):
		"""for k in range(8):
			for l in range(8):
				print(lista[l][k],end='')
				print(" ",end='')
			print("")
		print("")"""
		solucion += 1

print("Número de soluciones: ",solucion)