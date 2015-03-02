class DataFrameBase:
	def __init__(self):
		self.data = []

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