import serial
import sys
import json
import time
import datetime


# take in the arguments from the command line
port = sys.argv[1]
loc = sys.argv[2]
radio = sys.argv[3]
iterations = sys.argv[4]

radioDict = {
	# Dan
	"radio1": 'ATDL409756B8\r',
	# Jeff
	"radio2": 'ATDL409756BD\r',
	# Kat
	"radio3": 'ATDL40975703\r'
}

def rangeCall():
	myString = "This is a range test"
	ser.write(myString)
	s = ser.read(20) 
	ser.write('+++')
	s = ser.read(3)
	# command for the RSSI of the last received packet in -dB
	ser.write('ATDB\r')
	rangeLevel = ser.read(3)
	# turn the range level from decimal to hexidecimal
	rangeLevel = int(rangeLevel[0:2], 16)
	rangeLevel = str(rangeLevel)
	# exit command mode
	ser.write('ATCN\r')
	s = ser.read(3) 
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	try:
		print st + ',' + loc + ',' + rangeLevel + ',' + br[0]
	except IndexError:
		print st + ',' + loc +',-,' + br[0]

# open serial connection
ser = serial.Serial(port, 9600, timeout=2)
# enter command mode
ser.write("+++")
s = ser.read(3)
# get the data rate 
ser.write('ATBR\r')
br = ser.read(3)
# destination address high (same for all three radios)
ser.write('ATDH13A200\r')
s = ser.read(3)
# destination address low 
ser.write(radioDict[radio])
s = ser.read(3) 
# set cluster id to 11
ser.write('ATCI11\r')
s = ser.read(3) 
# apply charge
ser.write('ATAC\r')
s = ser.read(3) 
ser.write('ATCN\r')
s = ser.read(3) 

# get range value 10 times as value tends to oscillate
for i in range(int(iterations)):
	rangeCall()

# close the serial connection
ser.close()


