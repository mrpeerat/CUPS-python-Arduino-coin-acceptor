#! /usr/bin/python
import RPi.GPIO as GPIO
import time,os,cups,time,subprocess,glob
import sys, tty, termios
import lcddriver
#from time import *
lcd = lcddriver.lcd()
noend = 1
coin=0
main = 1
value=0
alltimes=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)
while (noend <=10):
        check=0
        coin=0
        main=1
        value=0
        alltime=0
        code=""
        i=1
        ch=""
        lcd.lcd_clear()
        lcd.lcd_display_string('Enter your code : ',1)
        while (i <= 4):
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                code=(code+ch)
                lcd.lcd_display_string('%s'%code,2)
                print '\nchar is\'' + ch + '\'\n'
                i+=1
        ############################################
 lcd.lcd_clear()
        add=("/var/www/html/upload/myfiles/%s/"%code)
        textname=("%s.txt"%code)
        try:
                pageadd=(add+textname)
                os.chdir(add)
                for file in glob.glob("*.pdf"):
                        alltimes+=1
                filenames=(add+file)
                page=open(pageadd,'r')
                num = (page.read())
                x=int(num)
                lcd.lcd_display_string('Name:%s'%file,1)
                print "File name : ",file
                lcd.lcd_display_string('Price:%s Bath'%x,2)
                print "Number of page/price : ",x
                lcd.lcd_display_string('Press 1 for continue',3)
                lcd.lcd_display_string('Press AnyKey to exit',4)
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                print '\nchar is\'' + ch + '\'\n'
                if(ch!="1"):
                   x=value;
                   filenames=""

                test=0
        except:
 except:
                lcd.lcd_clear()
                lcd.lcd_display_string('Enter Number Again!',1)
                raw_input("Enter Number again!")
                lcd.lcd_clear()
        try:
                lcd.lcd_clear()
                while (value < x):
                        os.system('clear')
                        if GPIO.input(7):
                                print '1 bath'
                                coin+=1;
                                time.sleep(0.7)
                        if GPIO.input(11):
                                print '1 bath'
                                coin+=1;
                                time.sleep(0.7)
                        if GPIO.input(13):
                                print '5 bath'
                                coin+=5;
                                time.sleep(0.7)
                        if GPIO.input(15):
                                print '10 bath'
                                coin+=10;
                                time.sleep(0.7)
                        value+=coin
                        coin=0
                        lcd.lcd_display_string('Enter a money !',1)
                        print "Enter the money !"
                        lcd.lcd_display_string('now have : %s'%value,2)
                        print 'now have : ',value
                        lcd.lcd_display_string('Price is : %s'%x,3)
                        print "Price is : ",x
                        time.sleep(0.2)
 except:
                        lcd.lcd_clear()
        os.system('clear')
        try:
                lcd.lcd_clear()

                print ("Now printer is printing")
                while main ==1:
                        conn = cups.Connection()
                        printers = conn.getPrinters()
                        for printer in printers:
                                print printer,
                                printers[printer]['device-uri']
                        printer_name = printers.keys()[0]
                        time.sleep(0.1)
                        filename = filenames
                        printid = conn.printFile(printer_name,filename,'Python_status_print',{})
                        time.sleep(5)
                        stop = 0
                        TIMEOUT = 5
                        lcd.lcd_display_string('Now Printer is',1)
                        lcd.lcd_display_string('Printing',2)
                        while str(subprocess.check_output(['lpstat'])).find(str(printid)) > 0 and stop < TIMEOUT:
                                stop+- 1
                                time.sleep(0.5)
 if stop < TIMEOUT:
                                lcd.lcd_display_string('Print Success',3)
                                print 'Print Success'
                        else:
                                lcd.lcd_display_string('Print Falure',3)
                                print 'Print Falure'
                        time.sleep(1)
                        lcd.lcd_display_string('Thank you',4)
                        fd = sys.stdin.fileno()
                        old_settings = termios.tcgetattr(fd)
                        tty.setraw(sys.stdin.fileno())
                        ch = sys.stdin.read(1)
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

                        main = 0
                        os.remove(filename)
                        os.remove(pageadd)
                        os.system('clear')
        except:
                print ""
        #os.remove(filenames)
        #os.remove(pageadd)
        os.system('clear')
