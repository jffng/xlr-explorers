# transmit request: hello world to radio 1
import serial
import sys
import binascii
port = sys.argv[1]
radio = sys.argv[2]
message = sys.argv[3]

radioDict = {
	# Dan
	"radio1": '0013A200409756B8',
	# Jeff
	"radio2": '0013A200409756BD',
	# Kat
	"radio3": '0013A20040975703'
}
def messageToHex(message):
	return binascii.hexlify(message)

def frameLength():
	length = 13 + len(messageToHex(message))/2
	hexlen = '00'+ hex(length)[2:4]
	return hex(length)

transmitRequest = '7E' + frameLength() + '1001' + radioDict[radio] + 'FFFE'+'00'+ messageToHex(message) 
# + checksum()
print transmitRequest

def syntax_thing(str):
       new_str = ""
       for idx,char in enumerate(str):
               if idx%2==1:
                       new_str += ("\\x" + str[idx-1] + str[idx])
       return new_str

ser = serial.Serial('/dev/cu.usbserial', 9600, timeout=2)
 

# ser.write(tx)
 
# s = ser.read(20)
# print s 


