import pickle
info=open("data","rb")

midiccionario=pickle.load(info)
print(midiccionario)
print(midiccionario.key("pepe")) 
usuario=input("Introduce tu usuario ")
contra=input("Introduce tu contrasenya ")

if midiccionario[usuario]==contra:
	print("Estas dentro")
else:
	print("Estas fuera")
