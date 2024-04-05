from  bluetooth import *
import json
server_socket = BluetoothSocket(RFCOMM)

# port = 1
server_socket.bind(("",PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
uuid = "00001101-0000-1000-8000-00805f9b34fb"
advertise_service(server_socket, "helmet", service_id = uuid, service_classes = [uuid, HEADSET_CLASS], profiles = [HEADSET_PROFILE], protocols = [OBEX_UUID])

while True:
    
    client_socket, address = server_socket.accept()
    print("Accepted connection from ",address)
                  
    try:
        loads = json.loads
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
#             d = data[data.find('\"')+1:data.rfind('\"')]
            d = loads(data)
            print(d)
            if d['dist'] == 5:
                client_socket.send("CRASH")
    except Exception as e:
        print(str(e))
    except KeyboardInterrupt:
        print("disconnected")
        
        client_socket.close()
        server_socket.close()
        print("clean up")
                  
        break