#!usr/bin/python
import xlr, serial, sys, datetime, time, csv

loc = sys.argv[1]
target = sys.argv[2]
antenna = sys.argv[3]

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

		with open('test.csv', 'a') as fp:
			a = csv.writer(fp, delimiter=',')
			row = [st, loc, i, antenna , response[1]]
			a.writerow(row)

		print st + ' , ' + loc + ' , ' + data_rates[str(i)] + ' , ' + antenna + ' , ' +  str(response[1])