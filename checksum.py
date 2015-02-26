def checksum(st):
	checksum = 0
	bytes = st.split()
	# add all thr bytes of the packet excluding the frame delimiter 7E and the length
	# (the 2nd and 3rd bytes)
	for idx, byte in enumerate(bytes):
		if idx > 2 and idx != len(bytes)-1:
			checksum += int(bytes[idx], 16)
	checksum = hex(checksum)
	# Keep only the lowest eight bits
	lowest_eight_bits = [i for i in str(checksum[-2:])]
	lowest_eight_bits = ''.join(lowest_eight_bits)
	# Subtract this from 0xff
	checksum = hex(int('0xff', 16) - int(lowest_eight_bits, 16))
	print checksum

st = "7E 00 0A 01 01 50 01 00 48 65 6C 6C 6F B8"
checksum(st)