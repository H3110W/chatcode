import pickle
abrir=open("data","rb+")
fichero=pickle.load(abrir)
fichero["Pedro"]=1234
pickle.dump(fichero,abrir)
abrir.close()
cambio