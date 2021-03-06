def checksum(st):
	bytes = [st[i:i+2] for i in range(0,len(st),2)]
	checksum = sum([(int(x, 16)) for x in bytes[3:]])
	checksum = hex(checksum)
	# Keep only the lowest eight bits
	lowest_eight_bits = [i for i in str(checksum[-2:])]
	lowest_eight_bits = ''.join(lowest_eight_bits)
	# Subtract this from 0xff
	checksum = hex(int('0xff', 16) - int(lowest_eight_bits, 16))
	print str(checksum)[2:]

def length(st):
	bytes = [st[i:i+2] for i in range(0,len(st),2)]
	length_hex = "{0:#0{1}x}".format(len(bytes),6)
	print length_hex[2:]


# want B9
whatWeWant = "7E001017010013A200409756B8FFFE02425201"
# want 13
withoutLength = "10010013A20040975703FFFE000068656c6c6f"
checksum(whatWeWant)
length(withoutLength)