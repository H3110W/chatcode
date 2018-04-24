import socket

import threading

import sys

import pickle



class Cliente():

	"""docstring for Cliente"""

	def __init__(self, host="83.35.226.66", port=1980):

		

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			self.sock.connect((str(host), int(port)))
			#si hace una conexion imprime el mensaje
			print("Conexion satisfactoria")
			msg_recv = threading.Thread(target=self.msg_recv)
			msg_recv.daemon = True
			msg_recv.start()
			#pide un nombre para luego usarlo y enviar al server que lo muestre
			nombre=input("Pon tu nombre ")
			self.send_msg(nombre)
		except:
			#si no conecta al server
			print("No se puede establecer la conexion")
			input()
		while True:

			a=nombre+"-->"

			msg = input('->')

			if msg != 'salir':
				
				self.send_msg(a+msg)

			else:

				self.sock.close()

				sys.exit()



	def msg_recv(self):

		while True:

			try:
				try:
					data = self.sock.recv(1024)
				except:
					print("El servidor esta fuera de linea1")
					input()
				if data:
					try:
						print(pickle.loads(data))
					except:
						print("El servidor esta fuera de linea2")
						input()

			except:

				pass



	def send_msg(self, msg):
		try:
			self.sock.send(pickle.dumps(msg))
		except:
			pritn("El servidor esta desconectado3")
			input()





c = Cliente()