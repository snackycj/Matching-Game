import Rpi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



try:
    print "Push the button on the GPIO to start a game."
    print "Click the tiles to flip them.  After a short delay, they will flip back over."
    print "Don't click too fast.  You want to see what you flipped."

    while(True):
        if (GPIO.input(6)==GPIO.HIGH):
            import MemoryGame


except KeyboardInterrupt:
    GPIO.cleanup()
        
