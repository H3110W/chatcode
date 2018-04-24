import pickle
#Quita este registrador y anyade el que tienes
#con un add y luego un commit des pues subelo 
#iniciando sesion con el remote add...
#y luego subelos con el git push.
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
