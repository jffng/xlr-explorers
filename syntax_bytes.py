def syntax_thing(str):
	new_str = ""
	for idx,char in enumerate(str):
		if idx%2==1:
			new_str += (chr(0x5c) + 'x' + str[idx-1].upper() + str[idx].upper())
	print new_str

syntax_thing('7E000B0001000000000000000000FE')