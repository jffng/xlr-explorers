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

rg = xlr.Distance(target)
rg.update()
print target,rg.send(ser, 50)