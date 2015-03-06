import xlr, serial

ser = serial.Serial('/dev/cu.usbserial', 9600, timeout=2)

# init a new remote AT command to change the target radio's data rate to the 2nd setting.
# call update() to generate its data frame.
# pass it the serial object and number of bytes to expect from the response.
remote_at_command = xlr.RemoteAT('br02', 'radio1')
remote_at_command.update()
remote_at_command.send(ser, 50)

# init a transmit request, 'hello world'.
# call update() to generate its data frame.
# pass it the serial object and number of bytes to expect from the response.
transmit_request = xlr.Transmit('hello world', 'radio1')
transmit_request.update()
transmit_request.send(ser, 50)

# init a new AT command to change the radio's data rate to the 1st setting.
# call update() to generate its data frame.
# pass it the serial object and number of bytes to expect from the response.
at_command = xlr.ATCommand('br01')