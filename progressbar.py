import socket
import os
import math

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 10000)
sock.bind(server_address)

sock.listen(1)

prev_message = ""

# While the socket is running
while True:
	# Accept incoming connections
	connection, client_address = sock.accept()

	try:
		# Receive the data in small chunks and retransmit it
		while True:

			# Accept chunks of 3 bits (enough for 0-100 progress)
			message = connection.recv(3)

			if message:

				perc = int(message.decode("utf-8"))

				done = int(math.floor(float(perc)/10))
				to_go = 10-done

				message = '['
				for i in range(done):
				    message += '\u2588'

				for i in range(to_go):
				    message += ' '

				message += ']'

				if message != prev_message:
					prev_message = message
					# Clear last message and print a new one
					os.system('cls')
					print(message)

			else:
				break

	except e:
		print(e)
			
	finally:
		connection.close()
		break