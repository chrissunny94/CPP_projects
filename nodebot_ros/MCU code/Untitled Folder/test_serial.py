import Tkinter as tk
import arduinoserial

#import serial

baud = 9600
usb_dev ='ttyUSB0'

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=400,  height=400)

        self.label = tk.Label(self, text="last key pressed:  ", width=20)
        self.label.pack(fill="both", padx=100, pady=100)

        self.label.bind("<w>", self.on_w)
        self.label.bind("<a>", self.on_a)
        self.label.bind("<s>", self.on_s)
        self.label.bind("<d>", self.on_d)
	self.label.bind("<i>", self.on_i)
	self.label.bind("<k>", self.on_k)
	#self.on_S()
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('S')
        # give keyboard focus to the label by default, and whenever
        # the user clicks on it
        self.label.focus_set()
        self.label.bind("<1>", lambda event: self.label.focus_set())

    def on_wasd(self, event):
        self.label.configure(text="last key pressed: " + event.keysym);
    def on_w(self, event):
	self.label.configure(text="last key pressed: " + event.keysym);
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('F')
    def on_a(self, event):
	self.label.configure(text="last key pressed: " + event.keysym);
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('l')
    def on_s(self, event):
	self.label.configure(text="last key pressed: " + event.keysym);
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('B')
    def on_d(self, event):
	self.label.configure(text="last key pressed: " + event.keysym);
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('r')


    def on_i(self, event):
	self.label.configure(text="last key pressed: " + event.keysym);
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('i')
    def on_k(self, event):
	self.label.configure(text="last key pressed: " + event.keysym);
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('k')
    def on_S():
	#self.label.configure(text="last key pressed: " + event.keysym);
	arduino = arduinoserial.SerialPort('/dev/'+usb_dev, baud)
	arduino.write('S')

    


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
