def checksum(st):
	checksum = 0
	bytes = st.split()
	checksum = sum([(int(x, 16)) for x in bytes[3:]])
	checksum = hex(checksum)
	# Keep only the lowest eight bits
	lowest_eight_bits = [i for i in str(checksum[-2:])]
	lowest_eight_bits = ''.join(lowest_eight_bits)
	# Subtract this from 0xff
	checksum = hex(int('0xff', 16) - int(lowest_eight_bits, 16))
	print checksum

st = "7E 00 10 17 01 00 13 A2 00 40 97 56 B8 FF FE 02 42 52 01"
whatWeWant = "7E 00 10 17 01 00 13 A2 00 40 97 56 B8 FF FE 02 42 52 01"
checksum(whatWeWant)