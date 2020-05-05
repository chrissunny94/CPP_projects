from pynput.keyboard import Key, Listener
from copy import copy
import socket

import arduinoserial

#import serial

baud = 9600
usb_dev ='ttyUSB0'


class Connect_Bot:
    def __init__(self, baud, usb_dev , mode = "Normal"):
        self.arduino = arduinoserial.SerialPort('/dev/' + usb_dev, baud)

        self.arduino.write('D:500')
        self.arduino.write('D:-500')
        self.key_status = []
        self.pre_key_status = []
        self.key_list = ['Key.up', 'Key.down', 'Key.left', 'Key.right', 'Key.space']
        for i in range(0, len(self.key_list)):
            self.key_status.append(0)
            self.pre_key_status.append(9)

        self.speed_status_up = 0
        self.speed_status_down = 0
        # Collect events until released

        if mode =="Normal":
            with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
                listener.join()


    def update(self):
        key = Key
        with self.listner(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
                listener.join()
        listener.stop


    # Function changes the key_status variable active/deactive 1/0
    def key_status_toggle(self,i, status):

        if status == 0:
            if self.key_status[i] == 0:
                self.key_status[i] = 1
        else:
            if self.key_status[i] == 1:
                self.key_status[i] = 0

    def key_response(self,key_status):
        # print key_status
        # stop
        if key_status == [0, 0, 0, 0, 0]:
            return 'S'
        # move forward
        elif key_status == [1, 0, 0, 0, 0]:
            return 'F'
        # move backward
        elif key_status == [0, 1, 0, 0, 0]:
            return 'B'


        # move left forward
        elif key_status == [1, 0, 1, 0, 0]:
            return 'l'
        # move left backward
        elif key_status == [0, 1, 1, 0, 0]:
            return 15
        # left turn 90deg
        elif key_status == [0, 0, 1, 0, 0]:
            return 'L'



        # move right forward
        elif key_status == [1, 0, 0, 1, 0]:
            return 'r'
        # move right backward
        elif key_status == [0, 1, 0, 1, 0]:
            return 16
        # right turn 90deg
        elif key_status == [0, 0, 0, 1, 0]:
            return 'R'


        else:
            return 'S'

    # Function Checks the key and decides to send the status to the network or not
    def key_status_change(self,key, status):


        key_to_str = str(key)

        if key_to_str in self.key_list:
            self.key_status_toggle(self.key_list.index(key_to_str), status)

            if self.pre_key_status != self.key_status:
                Key_status = self.key_status
                self.arduino.write(self.key_response(Key_status))

                pre_key_status = copy(self.key_status)
                print (self.key_status)


            else:

                print ("Key status already sent")

        else:
            print ("Please press: UP - Forward , DOWN - Reverse , LEFT - Turn Left , RIGHT - Turn Right, SPACE - Stop")

    def speed_status_change(self,up_down):
        self.arduino.write(up_down)
        print (up_down)

    def on_press(self,key):


        try:
            if key.char == '-':
                self.speed_status_down = 1
            elif key.char == '+':
                self.speed_status_up = 1
            else:
                self.key_status_change(key, 0)

        except AttributeError:
            self.key_status_change(key, 0)

    def on_release(self,key):

        try:
            if key.char == '-':
                if self.speed_status_down == 1:
                    self.speed_status_change('k')
                    self.speed_status_down = 0
                else:
                    print ("- is not pressed")

            elif key.char == '+':
                if self.speed_status_up == 1:
                    self.speed_status_change('i')
                    self.speed_status_up = 0
                else:
                    print ("+ is not pressed")

            else:
                self.key_status_change(key, 1)

        except AttributeError:
            self.key_status_change(key, 1)

    def move_bot(self , Input ):
        print ("Bot Instruction" , Input)
        if Input == 'F':
            self.sock.sendto(str(9), (self.UDP_IP, self.UDP_PORT))
        elif Input =='B':
            self.sock.sendto(str(13), (self.UDP_IP, self.UDP_PORT))
        elif Input =='L':
            self.sock.sendto(str(3), (self.UDP_IP, self.UDP_PORT))
        elif Input =='R':
            self.sock.sendto(str(4), (self.UDP_IP, self.UDP_PORT))
        elif Input =="FL":
            self.sock.sendto(str(7), (self.UDP_IP, self.UDP_PORT))
        elif Input =='BL':
            self.sock.sendto(str(15), (self.UDP_IP, self.UDP_PORT))
        elif Input =="FR":
            self.sock.sendto(str(8), (self.UDP_IP, self.UDP_PORT))
        elif Input =='B':
            self.sock.sendto(str(16), (self.UDP_IP, self.UDP_PORT))
        elif Input =='S':
            self.sock.sendto(str(0), (self.UDP_IP, self.UDP_PORT))
        elif Input =='u':
            self.sock.sendto(str(18), (self.UDP_IP, self.UDP_PORT))
        elif Input =='d':
            self.sock.sendto(str(17), (self.UDP_IP, self.UDP_PORT))


if __name__ == "__main__":
	connect_bot = Connect_Bot(baud , usb_dev , mode="Normal")






