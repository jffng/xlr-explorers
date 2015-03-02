##################################################
## Send AT Commands to your radio
## By: Dan Melancon, Jeff Ong, and Kat Sullivan
##################################################
import serial
import sys
import binascii

port = sys.argv[1]
message = sys.argv[2]

def atCommandToMessage(message):
	# convert AT command written in ASCII to Hex
	new_str = message[0].encode("hex") + message[1].encode("hex")
	new_str += message[2:4]
	return new_str

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

transmitRequest = '0801' + atCommandToMessage(message)
transmitRequest = '7E' + length(transmitRequest) + transmitRequest
transmitRequest = transmitRequest + checksum(transmitRequest)

tx = transmitRequest
ser = serial.Serial(port, 9600, timeout=2)
ser.write(transmitRequest.decode("hex"))

print transmitRequest.decode("hex")
s = ser.read(50)
print transmitRequest
print binascii.hexlify(s) 
