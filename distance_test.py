import xlr, serial

ser = serial.Serial('/dev/cu.usbserial', timeout=.5)

target = 'radio1'


data_rate = 'br4'
remote_at = xlr.RemoteAT(data_rate, target)
remote_at.update()
remote_at.send(ser,50)

at_command = xlr.ATCommand(data_rate)
at_command.update()
at_command.send(ser,50)
dataArray = []

for i in range(20):
	rg = xlr.Distance(target)
	rg.update()
	data = rg.send(ser, 50)[1]
	print "Distance: ",data

	if type(data) == int and data <100000:
		dataArray.append(data)

for i in range(1000):
	rg = xlr.Distance(target)
	rg.update()
	data = rg.send(ser, 50)[1]
	print "Distance: ",data
	dataArray.append(data)
	dataArray = dataArray[1:len(dataArray)]
	totalVal = 0;
	for i in dataArray:
		totalVal += i
	avgVal = totalVal/len(dataArray)
	print "Avg Distance: ",avgVal