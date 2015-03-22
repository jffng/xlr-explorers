#XLR Python API
API allows for writing structured data frames over serial usb to the XLR radio. 
Currently, there are 3 frame types supported: Remote AT, Trasmit Request and AT Command. 
####Setup
Import the library and define the serial port.

      import xlr,serial
      ser = serial.Serial('/dev/cu.usbserial',9600,timeout=.5)

####Remote AT Example
  
AT command, commands are not case-sensitive and parameters do not require a leading 0

      command = 'br4'  
    
radio address as string

    target = '0013A200409xxxxx' 
    remote_AT = xlr.RemoteAT(command, target)
    remote_AT.update()
    
send function takes the serial port and the amount of expected return bytes  and returns the response status
    
    remote_AT.send(ser, 50)  

####Transmit Request Example
   
Transmit message

    message = 'hello world!'  
    
radio address as string

    target = '0013A200409xxxxx' 
    transmit = xlr.Transmit(message, target)
    transmit.update()
    
send function takes the serial port and the amount of expected return bytes  and returns the response status
    
    transmit.send(ser, 50) 
   
####AT Command Example 

AT command, commands are not case-sensitive

    command = 'my1001'
    AT_Command = xlr.ATCommand(command)
    AT_Command.update()
    
send function takes the serial port and the amount of expected return bytes  and returns the response status
    
    AT_Command.send(ser, 50)
   
### Range_Test.py Example
This script takes three required command line arguments: 1. location 2. target radio address 3. antenna type.

The script executes a set of 5 range tests while cycling through each radio's data rate every five tests.
 
######To Run Range_Test.py 
    python Range_Test.py [location] [targetRadio] [antennaType]
