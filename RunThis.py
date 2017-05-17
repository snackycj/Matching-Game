import Rpi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(25'change this number to the wire youre using for the button',GPIO.IN, pull_up_down=GPIO.PUD_UP)



try:
    print "This program can generate an infinite number of memory matching games."
    print "Push the button on the GPIO to make a new game."
    print "Click the tiles to flip them.  After a short delay, they will flip back over."
    print "Don't click too fast.  You want to see what you flipped."

    while(True):
        if (GPIO.input(25'again, change this number')==GPIO.HIGH):
            import MemoryGame


except KeyboardInterrupt:
    GPIO.cleanup()
        
