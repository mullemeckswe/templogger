import CHIP_IO.GPIO as GPIO
import time





def readdata(data):
	indata = 0
	GPIO.output("CSID0",0)
	for i in range(8):
		GPIO.output("CSID3",0)
		
		if (data<<i) & 0x80:
			GPIO.output("CSID1",1)
			
		else:
			GPIO.output("CSID1",0)
			
		GPIO.output("CSID3",1)

	for i in range(8):
			GPIO.output("CSID3",0)
			indata = indata + (GPIO.input("CSID2") << (7-i))
			GPIO.output("CSID3",1)
	GPIO.output("CSID0",1)
	return indata

def writedata(adr,data):
	indata = 0
	GPIO.output("CSID0",0)
	for i in range(8):
		GPIO.output("CSID3",0)
		
		if (adr<<i) & 0x80:
			GPIO.output("CSID1",1)
			
		else:
			GPIO.output("CSID1",0)
			
		GPIO.output("CSID3",1)

	for i in range(8):
		GPIO.output("CSID3",0)
		
		if (data<<i) & 0x80:
			GPIO.output("CSID1",1)
			
		else:
			GPIO.output("CSID1",0)
			
		GPIO.output("CSID3",1)
	GPIO.output("CSID0",1)

	return indata


GPIO.setup("CSID0", GPIO.OUT) #CS
GPIO.setup("CSID1", GPIO.OUT) #SDI
GPIO.setup("CSID2", GPIO.IN) #SDO
GPIO.setup("CSID3", GPIO.OUT) #CLK
GPIO.output("CSID3",1)
GPIO.output("CSID0",1)
writedata(0x80,193)
time.sleep(0.3)
datahigh = readdata(1)<<8
datalow = readdata(2)
resistance = ((datahigh+datalow)*428.6)/65532
temp =  -244.83 + 2.3419*resistance + .0010664*resistance*resistance

print resistance
print temp
