
#this function decodes both Transmit Request and Remote AT Command Responses
def decodeResponse(response):
	responseType = {
		'00' : 'OK',
		'01' : 'ERROR',
		'02' : "INVALID COMMAND",
		'03' : "INVALID PARAMETER"
	}
	response = response[-6:-4]
	return responseType[response]

#this function decodes AT Command Response
def decodeAtCommandResponse(response):
	responseType = {
		'00' : 'OK',
		'01' : 'ERROR',
		'02' : "INVALID COMMAND",
		'03' : "INVALID PARAMETER"
	}
	response = response[-4:-2]
	return responseType[response]


