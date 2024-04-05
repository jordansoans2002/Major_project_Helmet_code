from  bluetooth import BluetoothSocket, RFCOMM, PORT_ANY, advertise_service, HEADSET_CLASS, HEADSET_PROFILE, OBEX_UUID
from led_controller import searching, found, led_main
import json


def init():
	# try to turn on discoverable from here 
	server_socket = BluetoothSocket(RFCOMM)
	server_socket.bind(("",PORT_ANY))
	server_socket.listen(1)
	port = server_socket.getsockname()[1]
	uuid = "00001101-0000-1000-8000-00805f9b34fb"
	advertise_service(server_socket, "helmet", service_id = uuid, service_classes = [uuid, HEADSET_CLASS], profiles = [HEADSET_PROFILE], protocols = [OBEX_UUID])

def accept_connection(server_socket):
	searching()
	# TODO turn off helmet after some time
	client_socket, address = server_socket.accept()
	found()
	print("Accepted connection from ",address)
	return client_socket

def get_message(client_socket):                  
        loads = json.loads
        while True:
			try:
				recvd_msg = client_socket.recv(1024).decode('utf-8')
				data = loads(recvd_msg)
				if 'cmd' in data:
					if data['cmd'] == 'TURN_OFF':
						# shutdown pi and switch off battery
					elif data['cmd'] == 'DISCONNECT':
						client_socket.close()
						server_socket.close()
					# manage other commands like fetch vid, delete data etc
				elif 'nav' in data:
					led_main(data[nav])

			except Exception as e:
				# catch connection reset seperatly and close the sockets there
				print(str(e))
				
def send_message(client_socket,msg):
	try
		client_socket.send(msg)
	except Exception as e:
		print(str(e))
		# if required close socket
	
	
