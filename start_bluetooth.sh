sudo bluetoothctl <<EOF
agent on
discoverable on
pairable on
EOF

sudo python bluetooth_server.py
