import xlr, serial

ser = serial.Serial('/dev/cu.usbserial', timeout=.5)

rg = xlr.Distance('radio2')
rg.update()
print rg.send(ser, 50)