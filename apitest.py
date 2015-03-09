import xlr, serial, sys, datetime, time

loc = sys.argv[1]
target = sys.argv[2]

ser = serial.Serial('/dev/cu.usbserial', 9600, timeout=.5)

data_rates = {
	'0': '9.38kbps',
	'1': '28.14kbps',
	'2': '65.66kbps',
	'3': '140.7kbps',
	'4': '290.8kbps',
	'5': '590.9kbps',
	'6': '1.191Mbps',
	'7': '2.392Mbps',
	'8': '3.189Mpbs'
}

for i in range(9):
	data_rate = 'br' + str(i)
	
	remote_at = xlr.RemoteAT(data_rate, target)
	remote_at.update()
	remote_at.send(ser,50)

	at_command = xlr.ATCommand(data_rate)
	at_command.update()
	at_command.send(ser,50)

	for b in range(5):
		tx = xlr.Transmit('star wars reference', target)
		tx.update()
		tx.send(ser, 50)

		at_command = xlr.ATCommand('db')
		at_command.update()
		response = at_command.send(ser,50)

		st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

		# with open('test.csv', 'a') as fp:
		# 	a = csv.writer(fp, delimiter=',')
		# 	row = [st, loc, i, rangeLevel, br[0]]
		# 	a.writerow(row)

		print st + ' , ' + loc + ' , ' + data_rates[str(i)] + ' , ' + str(response[1])

# init a new remote AT command to change the target radio's data rate to the 2nd setting.
# call update() to generate its data frame.
# pass it the serial object and number of bytes to expect from the response.
# remote_at_command = xlr.RemoteAT('pl02', 'radio1')
# remote_at_command.update()
# res = remote_at_command.send(ser, 50)

# print res

# init a transmit request, 'hello world'.
# call update() to generate its data frame.
# pass it the serial object and number of bytes to expect from the response.
# transmit_request = xlr.Transmit('hello world', 'radio2')
# transmit_request.update()
# res = transmit_request.send(ser, 50)

# print res

# init a new AT command to change the radio's data rate to the 1st setting.
# call update() to generate its data frame.
# pass it the serial object and number of bytes to expect from the response.
at_command = xlr.ATCommand('db')
at_command.update()
res = at_command.send(ser, 50)

print res