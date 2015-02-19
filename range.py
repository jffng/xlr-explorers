import serial
import sys
import json
import time
import datetime

port = sys.argv[1]
loc = sys.argv[2]
radio = sys.argv[3]
iterations = sys.argv[4]
radioDict = {
	"radio1": 'ATDL409756B8\r',
	"radio2": 'ATDL409756BD\r',
	"radio3": 'ATDL40975703\r'
}

def rangeCall():
	myString = "This is a range test"
	ser.write(myString)
	s = ser.read(20) 
	ser.write('+++')
	s = ser.read(3)
	ser.write('ATDB\r')
	rangeLevel = ser.read(3)
	rangeLevel = int(rangeLevel[0:2], 16)
	rangeLevel = str(rangeLevel)
	ser.write('ATCN\r')
	s = ser.read(3) 
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	try:
		print st + ',' + loc + ',' + rangeLevel + ',' + br[0]
	except IndexError:
		print st + ',' + loc +',-,' + br[0]

ser = serial.Serial(port, 9600, timeout=2)
ser.write("+++")
s = ser.read(3) 
ser.write('ATBR\r')
br = ser.read(3)
ser.write('ATDH13A200\r')
s = ser.read(3) 
ser.write(radioDict[radio])
s = ser.read(3) 
ser.write('ATCI11\r')
s = ser.read(3) 
ser.write('ATAC\r')
s = ser.read(3) 
ser.write('ATCN\r')
s = ser.read(3) 

for i in range(int(iterations)):
	rangeCall()

ser.close()


