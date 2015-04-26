import xlr, serial

ser = serial.Serial('/dev/cu.usbserial', timeout=.5)

target0 = 'radio1'
target1 = 'radio2'
target2 = 'radio4'

for i in range(3):
	data_rate = 'br4'
	remote_at = xlr.RemoteAT(data_rate, eval('target'+str(i)))
	remote_at.update()
	remote_at.send(ser,50)


at_command = xlr.ATCommand(data_rate)
at_command.update()
at_command.send(ser,50)

for i in range(3):
	rg = xlr.Distance(eval('target'+str(i)))
	rg.update()
	print eval('target'+str(i)),rg.send(ser, 50)