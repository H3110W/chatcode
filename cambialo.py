import pickle
#Quita este registrador y anyade el que tienes
#con un add y luego un commit des pues subelo 
#iniciando sesion con el remote add...
#y luego subelos con el git push.
abrir=open("data","rb+")
fichero=pickle.load(abrir)
fichero["Pedro"]=1234
pickle.dump(fichero,abrir)
abrir.close()