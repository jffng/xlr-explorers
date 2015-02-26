def checksum(st):
	checksum = 0
	bytes = st.split()
	checksum = sum([(int(x, 16)) for x in bytes[3:len(bytes)-1]])
	checksum = hex(checksum)
	# Keep only the lowest eight bits
	lowest_eight_bits = [i for i in str(checksum[-2:])]
	lowest_eight_bits = ''.join(lowest_eight_bits)
	# Subtract this from 0xff
	checksum = hex(int('0xff', 16) - int(lowest_eight_bits, 16))
	print checksum

st = "7E 00 0A 01 01 50 01 00 48 65 6C 6C 6F B8"
checksum(st)