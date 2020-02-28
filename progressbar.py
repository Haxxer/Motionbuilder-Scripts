import socket
import os
import math

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 10000)
sock.bind(server_address)

sock.listen(1)

last_message = ""

while True:

	connection, client_address = sock.accept()

	try:

		# Receive the data in small chunks and retransmit it
		while True:

			percentage = connection.recv(3)

			if percentage:

				done = int(percentage)
				to_go = 100-done

				message = '['
				for i in range(done):
					message += '\u2588'

				for i in range(to_go):
					message += ' '

				message += '] {0}% Done'.format(int(percentage))

				os.system('cls')
				print(message)

				connection.sendall(percentage)

			else:
				break

	except e:
		print(e)
			
	finally:
		connection.close()
		break