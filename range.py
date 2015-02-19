import serial
import sys
import json
import time
import datetime

st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

port = sys.argv[1]

ser = serial.Serial(port, 9600, timeout=2)
ser.flush()
ser.write("+++")
s = ser.read(3) 
# print s

ser.flush()
ser.write("ATBR\r")
br = ser.read(3)

ser.flush()
ser.write('ATDH13A200\r')
s = ser.read(3) 
# print s
ser.flush()
ser.write('ATDL40975703\r')
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

print st + ',' + rangeLevel + ',' + br[0]