###################################################
## By Dan Melacon, Jeff Ong, and Kat Sullivan
###################################################

import serial, sys, binascii

addresses={
	'radio1': '0013A200409756B8',
	'radio2': '0013A200409756BD',
	'radio3': '0013A20040975703',
	'radio4': '0013A200409756E2'
}

responseType = {
	'00' : "OK",
	'01' : "ERROR",
	'02' : "INVALID COMMAND",
	'03' : "INVALID PARAMETER"
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
		message = message.upper()
		new_str = message[0].encode("hex") + message[1].encode("hex")
		if len(message) == 3:
			new_str += '0' + message[2]
		else:
			new_str += message[2:4]
		self.message = new_str

		try:
			self.address = addresses[radio]
		except KeyError:
			self.address = radio

	def update(self):
		request = self.command_type + self.address + 'FFFE' + '01' + self.message
		request = '7E' + length(request) + request	
		request = request + checksum(request)
		# print request
		self.frame = request.decode("hex")

	def send(self, serial, response_length):
		serial.write(self.frame)
		try:
			response = serial.read(response_length)
			response = binascii.hexlify(response)
			response = response[-4:-2]
			return responseType[response]
		except KeyError:
			return 'Invalid response from remote radio'

class Transmit():
	command_type = '1001'

	def __init__(self, message, radio):
		self.message = messageToHex(message)
		try:
			self.address = addresses[radio]
		except KeyError:
			self.address = radio
	
	def update(self):
		request = self.command_type + self.address + 'FFFE' + '0000' + self.message
		request = '7E' + length(request) + request	
		request = request + checksum(request)
		self.frame = request.decode("hex")

	def send(self, serial, response_length):
		serial.write(self.frame)
		try:
			response = serial.read(response_length)
			response = binascii.hexlify(response)
			response = response[-6:-4]
			return responseType[response]
		except KeyError:
			return 'Invalid response from remote radio'

class ATCommand():
	command_type = '0801'
	parameter = True

	def __init__(self, message):
		message = message.upper()
		new_str = message[0].encode("hex") + message[1].encode("hex")
		if len(message) == 3:
			new_str += '0' + message[2]
			self.message = new_str
		elif len(message) == 2:
			self.parameter = False
			self.message = new_str
		else:
			new_str += message[2:4]
			self.message = new_str


	def update(self):
		request = self.command_type + self.message
		request = '7E' + length(request) + request	
		request = request + checksum(request)
		# print request
		self.frame = request.decode("hex")

	def send(self, serial, response_length):
		serial.write(self.frame)
		try:
			if self.parameter:
				response = serial.read(response_length)
				response = binascii.hexlify(response)
				response = response[-4:-2]
				return responseType[response]
			else:
				response = serial.read(response_length)
				response = binascii.hexlify(response)
				status = response[-6:-4]
				data = response[-4:-2]
				data = int(data,16)
				return [ responseType[status], data ]
		except KeyError:
			return 'Invalid response from remote radio'

class Distance():
	command_type = '08015247'

	def __init__(self, radio):
		try:
			self.address = addresses[radio]
		except KeyError:
			self.address = radio

	def update(self):
		request = self.command_type + self.address
		request = '7E' + length(request) + request	
		request = request + checksum(request)
		# print request
		self.frame = request.decode("hex")

	def send(self, serial, response_length):
		serial.write(self.frame)
		try:
			response = serial.read(response_length)
			response = binascii.hexlify(response)
			status = response[-10:-8]
			data = response[-8:-2]
			return [ responseType[status], int(data,16) ]
		except KeyError:
			return 'Invalid response from remote radio'