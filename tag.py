import nxppy
import time
from OSC import OSCClient, OSCMessage

mifare = nxppy.Mifare()

client = OSCClient()
client.connect( ("255.255.255.255", 9001) )

old_val = 0
# Print card UIDs as they are detected
while True:
    try:
        uid = mifare.select()
        if uid:
			dec_val = long(uid, 16);
			if old_val != dec_val:
				old_val = dec_val
				print(dec_val)
				#mifare.read_block(1)
				msg = OSCMessage()
				msg.setAddress("/uid")
				msg.append(dec_val/10,"f")
				client.send(msg)
				a4 = int(dec_val & 0xff)
				a3 = int((dec_val >> 8) & 0xff)
				a2 = int((dec_val >> 16) & 0xff)
				a1 = int(dec_val >> 24)
				msg2 = OSCMessage()
				msg2.setAddress("/rgba")
				msg2.append(a1,"i")
				msg2.append(a2,"i")
				msg2.append(a3,"i")
				msg2.append(a4,"i")
				client.send(msg2)
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    #time.sleep(1)