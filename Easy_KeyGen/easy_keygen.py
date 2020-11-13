serial = bytes.fromhex('5B134977135E7D13')
key=[0x10,0x20,0x30]
name=''

for i in range(len(serial)):
	name+=chr((serial[i])^key[i%3])
print(name)
