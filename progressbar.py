import socket
import os
import math

def display(data):

	perc = int(data)

	done = int(math.floor(float(perc)/2))
	to_go = 50-done

	message = '['
	for i in range(done):
	    message += '\u2588'

	for i in range(to_go):
	    message += ' '

	message += '] {0}%'.format(perc)

	return message

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 10000)
sock.bind(server_address)

sock.listen(1)

prev_message = ""

print('[                                                  ] 0%')

while True:

	connection, client_address = sock.accept()

	try:

		while True:

			inc_data = connection.recv(1024)

			if inc_data:

				data = inc_data.decode("utf-8")

				if len(data) > 3:

					split_data = [data[i:i+3] for i in range(0, len(data), 3)]

					for data in split_data:
						message = display(data)
						if message != prev_message:
							# Clear last message and print a new one
							print(message)

				else:
					message = display(data)
					if message != prev_message:
						# Clear last message and print a new one
						print(message)

			else:
				break

	except e:
		print(e)
			
	finally:
		connection.close()
		break