import serial, sys, binascii

addresses={
	'radio1': '0013A200409756B8',
	'radio2': '0013A200409756BD',
	'radio3': '0013A20040975703'
}

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

def messageToHex(message):
	return binascii.hexlify(message)

class RemoteAT():
	command_type = '1701'

	def __init__(self, message, radio):
		self.message = message[0].encode("hex") + message[1].encode("hex")
		if len(self.message) == 3:
			self.message += '0' + self.message[2]
		else:
			self.message += self.message[2:4]
		self.address = addresses[radio]

	def update(self):
		request = self.command_type + 'FFFE' + self.message
		print request
		request = '7E' + length(request) + request	
		request = request + checksum(request)
		self.frame = request.decode("hex")

class LocalAT():
	command_type = '0801'

	def __init__(self, name):
		self.name = name

class Transmit():
	command_type = '1001'

	def __init__(self, name):
		self.name = name


# transmitRequest = '1001' + radioDict[radio] + 'FFFE' + '0000' + messageToHex(message)
# transmitRequest = '7E' + length(transmitRequest) + transmitRequest
# transmitRequest = transmitRequest + checksum(transmitRequest)