from OSC import OSCClient, OSCMessage

import mraa
import time

class Counter:
  count = 0

c = Counter()

client = OSCClient()
#client.connect( ("192.168.42.20", 9002) )
client.connect( ("192.168.42.255", 9002) )
#client.send( OSCMessage("/start") )


#In interupt you cannot use 'basic' types so you'll need to use
# objects
def f1(args):
  print("f1")
  msg = OSCMessage()
  msg.setAddress("/finger")
  msg.append(1,"i")
  client.send(msg)
def f2(args):
  print("f2")
  msg = OSCMessage()
  msg.setAddress("/finger")
  msg.append(2,"i")
  client.send(msg)
def f3(args):
  print("f3")
  msg = OSCMessage()
  msg.setAddress("/finger")
  msg.append(3,"i")
  client.send(msg)
def f4(args):
  print("f4")
  msg = OSCMessage()
  msg.setAddress("/finger")
  msg.append(4,"i")
  client.send(msg)


x1 = mraa.Gpio(45)
x2 = mraa.Gpio(46)
x3 = mraa.Gpio(47)
x4 = mraa.Gpio(48)
x1.dir(mraa.DIR_IN)
x2.dir(mraa.DIR_IN)
x3.dir(mraa.DIR_IN)
x4.dir(mraa.DIR_IN)
#x1.mode(mraa.MODE_PULLDOWN)
#x2.mode(mraa.MODE_PULLDOWN)
#x3.mode(mraa.MODE_PULLDOWN)
#x4.mode(mraa.MODE_PULLDOWN)
#x1.isr(mraa.EDGE_RISING, f1, f1)
#x2.isr(mraa.EDGE_RISING, f2, f2)
#x3.isr(mraa.EDGE_RISING, f3, f3)
#x4.isr(mraa.EDGE_RISING, f4, f4)

while True:
  if not x1.read():
    print("f1")
    #f1(0)
  if not x2.read():
    print("f2")
	#f2(0)
  if not x3.read():
    print("f3")
	#f3(0)
  if not x4.read():
    print("f4")
	#f4(0)
  msg = OSCMessage()
  msg.setAddress("/finger")
  msg.append(x1.read(),"i")
  msg.append(x2.read(),"i")
  msg.append(x3.read(),"i")
  msg.append(x4.read(),"i")
  client.send(msg)
  time.sleep(0.1)
