from  gpiozero import LED
from signal import pause
from time import sleep

a = [LED(26),LED(19),LED(13),LED(6),LED(5)] # pin numbers on which A is connected
# B is MSB, C is LSB they are exchanged
b = LED(9) # pin on which all the C are connected
c = LED(11) # pin on which all the B are connected

def all_off():
    for i in range(0, 5):
        if i%2 == 0:
            a[i].off()
        else:
            a[i].on()
            
def turn(turn):
    if turn['dir'] == 'l':
        b.on()
    elif turn['dir'] == 'r':
        b.off()
    
    c.off()
        
    # c=0 green, c=1 blue
    # use blue to indicate user is not on selected path
    # show directions back to path in blue
    
    for i in range(0, turn['dist']):
        a[i].toggle()

def test():
    b.off()
    c.off()
    a[0].off()
    a[1].on()

    a[2].on()
    a[3].off()

    a[4].off()    

all_off()
#test()
for i in range(0,6):
    all_off()
    turn_data = {'dir':'r','dist':i,'angle':90}
    turn(turn_data)
    sleep(2)

pause()