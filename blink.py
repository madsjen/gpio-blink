import RPi.GPIO as GPIO
import sys, time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(11, False)
GPIO.output(13, False)

redPin  = 11
bluePin = 13

def choosePin():
    print 'Which LED would you like to blink?'
    print '1: Red'
    print '2: Blue'
    print '3: Both'
    print '4: Exit'
    led_choice = input('Choose your option: ')
    options[led_choice]()

def blinkOne(pin):
    if pin == 'Exit':
        GPIO.cleanup();
        sys.exit(0)
    count = input('How many times would you like it to blink?: ')
    while count > 0:
        GPIO.output(pin, True)
        time.sleep(0.5)
        GPIO.output(pin, False)
        time.sleep(0.5)
        count = count - 1
    again = raw_input('Go again? y/n: ')
    if(again == 'y'):
        choosePin()
    else:
        GPIO.cleanup();
        sys.exit(0)

def blinkBoth():
    count = input('How many times would you like them to blink?: ')
    while count > 0:
        GPIO.output(redPin, True)
        GPIO.output(bluePin, False)
        time.sleep(0.5)
        GPIO.output(redPin, False)
        GPIO.output(bluePin, True)
        time.sleep(0.5)
        count = count - 1
    GPIO.output(bluePin, False)
    again = raw_input('Go again? y/n: ')
    if(again == 'y'):
        choosePin()
    else:
        GPIO.cleanup();
        sys.exit(0)

def red():
    print 'You picked the red LED'
    blinkOne(11)

def blue():
    print 'You picked the blue LED'
    blinkOne(13)

def both():
    print 'You picked both LEDs'
    blinkBoth()

def exit():
    print 'Invalid option. Exiting'

options = {
    1 : red,
    2 : blue,
    3 : both,
    4 : exit
}

choosePin()

GPIO.cleanup()