from time import sleep

select = [LED(26),LED(19),LED(13),LED(6),LED(5)] # pin numbers on which A is connected
# A is MSB, B is LSB they are exchanged
clr = LED(9) # pin on which all the B are connected
red = LED()
side = LED(11) # pin on which all the A are connected

def send_sequence(seq):
	if seq[0] == 1: select[0].on()
	else select[0].off()	
	
	if seq[1] == 1: select[1].on()
	else select[1].off()	
	
	if seq[2] == 1: select[2].on()
	else select[2].off()	
	
	if seq[3] == 1: select[3].on()
	else select[3].off()	
	
	if seq[4] == 1: select[4].on()
	else select[4].off()	
	
			
# off all leds
def off():
	send_sequence([0,1,0,1,0,1])
	


# on all red leds (for battery low?)
def red():
	off()
	red.on()


# blink red leds incase crash is detected
def blinkRed():
	on = red.on
	off = red.off
	for i in range(0,5):
		on()
		sleep(1)
		off()
		sleep(1)


# play some pattern while waiting for connection
def searching():



# play pattern to indicate device connected
def found():



def turnDist(dist,direction,isUturn):
	seq = [
		[1,1,0,1,0,1],
		[1,0,0,1,0,1],
		[1,0,1,1,0,1],
		[1,0,1,0,0,1],
		[1,0,1,0,1,1]
	]
	
	if direction == 'r':
		side.on()
	else
		side.off()
	
	if isUturn:
		clr.on() # set blue
	else
		clr.off()


def turnAngle(ang):
	seq = [
		100101,
		001101,
		011001,
		010011,
		110111,
	]
	
	#set side based on angle 
	# side.on()
	send_sequence(seq[ang])


def led_main(data):
	if data['dist'] > 100:
		return
