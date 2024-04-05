sudo bluetoothctl <<EOF
agent on
discoverable on
pairable on
EOF

sudo python phone_connection.py