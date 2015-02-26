# transmit request: hello world to radio 1
import serial
import sys
import binascii
port = sys.argv[1]
radio = sys.argv[2]
message = sys.argv[3]

radioDict = {
	# Dan
	"radio1": '0013A200409756B8',
	# Jeff
	"radio2": '0013A200409756BD',
	# Kat
	"radio3": '0013A20040975703'
}

def messageToHex(message):
	return binascii.hexlify(message)

def checksum(st):
	bytes = [st[i:i+2] for i in range(0,len(st),2)]
	checksum = sum([(int(x, 16)) for x in bytes[3:]])
	checksum = hex(checksum)
	# Keep only the lowest eight bits
	lowest_eight_bits = [i for i in str(checksum[-2:])]
	lowest_eight_bits = ''.join(lowest_eight_bits)
	# Subtract this from 0xff
	checksum = hex(int('0xff', 16) - int(lowest_eight_bits, 16))
	return str(checksum)[2:]

def length(st):
	bytes = [st[i:i+2] for i in range(0,len(st),2)]
	length_hex = '{0:#0{1}x}'.format(len(bytes),6)
	return length_hex[2:]

def syntax_thing(str):
	new_str = ''
	for idx,char in enumerate(str):
		if idx%2==1:
			new_str += (chr(0x5c) + 'x' + str[idx-1].upper() + str[idx].upper())
	return new_str

transmitRequest = '1001' + radioDict[radio] + 'FFFE' + '0000' + messageToHex(message)
transmitRequest = '7E' + length(transmitRequest) + transmitRequest
transmitRequest = transmitRequest + checksum(transmitRequest)
# print transmitRequest
# print transmitRequest.decode('hex')
# print binascii.unhexlify(transmitRequest)
# binHEx = bin(int(transmitRequest,16))[2:]
# print hex(int(binHEx,2))
# transmitRequest = syntax_thing(transmitRequest);

tx = transmitRequest
ser = serial.Serial(port, 9600, timeout=2)
ser.write(transmitRequest.decode("hex"))
#ser.write("b"+tx)
print transmitRequest.decode("hex")
s = ser.read(50)
print binascii.hexlify(s) 
print type(transmitRequest)
print transmitRequest
print binascii.hexlify(s) 
