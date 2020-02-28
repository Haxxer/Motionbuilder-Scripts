import socket
import os
import math

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 10000)
sock.bind(server_address)

sock.listen(1)

message = "["
for i in range(50):
	message += ' '
message += '] 0% Done'

print("If you accidentally press this window, you can right click to unpause.")
print("")
print(message)

# While the socket is running
while True:
	# Accept incoming connections
	connection, client_address = sock.accept()

	try:
		# Receive the data in small chunks and retransmit it
		while True:

			# Accept chunks of 3 bits (enough for 0-100 progress)
			percentage = connection.recv(3)

			if percentage:
				done = int(math.floor(float(percentage)/2))
				to_go = 50-done

				message = '['
				for i in range(done):
					message += '\u2588'

				for i in range(to_go):
					message += ' '

				message += '] {0}% Done'.format(int(percentage))

				# Send a reply so that owning script can continue
				connection.sendall(percentage)

				# Clear last message and print a new one
				os.system('cls')
				print("If you accidentally press this window, you can right click to unpause.")
				print("")
				print(message)

			else:
				break

	except e:
		print(e)
			
	finally:
		connection.close()
		break