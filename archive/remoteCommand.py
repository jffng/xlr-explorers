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
	checksum = hex(sum([(int(x, 16)) for x in bytes[3:]]))
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



remoteCommand = '1001' + radioDict[radio] + 'FFFE'+'00'+ messageToHex(message)
remoteCommand = '7E' + length(remoteCommand) + remoteCommand
remoteCommand = remoteCommand + checksum(remoteCommand)

ser = serial.Serial(port, 9600, timeout=2)
ser.write(remoteCommand.decode("hex"))
s = ser.read(50)
print remoteCommand
print binascii.hexlify(s) 