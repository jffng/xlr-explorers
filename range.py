import serial
import sys
import json
import time
import datetime

port = sys.argv[1]
loc = sys.argv[2]
radio = sys.argv[3]

{
	"radio1": 'ATDL409756B8\r',
	"radio2": 'ATDL409756BD\r',
	"radio3": 'ATDL40975703\r'
}

ser = serial.Serial(port, 9600, timeout=2)
ser.flush()
ser.write("+++")
s = ser.read(3) 
# print s

ser.flush()
ser.write('ATBR\r')
br = ser.read(3)
# print br

ser.flush()
ser.write('ATDH13A200\r')
s = ser.read(3) 
# print s
ser.flush()
ser.write('ATDL409756B8\r')
s = ser.read(3) 
# print s
ser.flush()
ser.write('ATCI11\r')
s = ser.read(3) 
# print s
ser.flush()
ser.write('ATAC\r')
s = ser.read(3) 
# print s
ser.flush()
ser.write('ATCN\r')
s = ser.read(3) 
# print s

myString = "This is a range test"

ser.flush()
ser.write(myString)
s = ser.read(20) 
# print s

ser.flush()
ser.write("+++")
s = ser.read(3)

ser.flush()
ser.write("ATDB\r")
rangeLevel = ser.read(3) 
rangeLevel = int(rangeLevel[0], 16)
rangeLevel = str(rangeLevel)
# print "range: " , rangeLevel

ser.flush()
ser.write("ATCN\n")
s = ser.read(3) 
# print s
ser.close()


st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

try:
	print st + ',' + loc + ',' + rangeLevel + ',' + br[0]
except IndexError:
	print st + ',' + loc +',-,' + br[0]
