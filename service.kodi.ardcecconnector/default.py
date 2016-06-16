import xbmc
import xbmcgui
import xbmcaddon
import time
import serial
import threading
 
class XBMCPlayer(xbmc.Player):
    def __init__(self, *args):
        pass
 
player = XBMCPlayer()
__settings__ = xbmcaddon.Addon(id='service.kodi.ardcecconnector')
comport = __settings__.getSetting("serialport")
#xbmcgui.Dialog().ok("ArdCEC Serial Port", comport)
serConnection = serial.Serial(comport, 115200)
serConnection.setTimeout(0.01)

 
def fire(action):
	xbmc.executebuiltin( "XBMC.Action(" + action + ")" )

def fireWindow(name):
	xbmc.executebuiltin( "XBMC.ActivateWindow(" + name + ")" )

def handleKey138(key):	#0x8A
	key = int(key)
	if key == 145:
		fire("Back")
	elif key == 150:
		fireWindow("TVChannels")
		
def handleKey65(key):	#0x41
	key = int(key)
	if key == 36:
		fire("Play")
	elif key == 37:
		fire("Pause")

def handleKey66(key):	#0x42
	key = int(key)
	if key == 3:
		fire("Stop")
	
def handleKey68(key):	#0x44
	key = int(key)
	if key == 0:
		fire("Select")
	elif key == 1:
		fire("Up")
	elif key == 2:
		fire("Down")
	elif key == 3:
		fire("Left")
	elif key == 4:
		fire("Right")
	#elif key == 5:
		#fire("RightUp")
	#elif key == 6:
		#fire("RightDown")
	#elif key == 7:
		#fire("LeftUp")
	#elif key == 8:
		#fire("Left-Down")
	elif key == 9:
		fire("Menu")
	elif key == 10:
		fire("Menu")
	elif key == 11:
		fire("Queue")
	elif key == 12:
		fireWindow("Favourites")
	elif key == 13:
		fire("Exit")
	#elif key == 14:
		#fire("Reserved 0x0E")
	#elif key == 15:
		#fire("Reserved 0x0F")
	#elif key == 16:
		#fire("Reserved 0x10")
	#elif key == 17:
		#fire("Reserved 0x11")
	#elif key == 18:
		#fire("Reserved 0x12")
	#elif key == 19:
		#fire("Reserved 0x13")
	#elif key == 20:
		#fire("Reserved 0x14")
	#elif key == 21:
		#fire("Reserved 0x15")
	#elif key == 22:
		#fire("Reserved 0x16")
	#elif key == 23:
		#fire("Reserved 0x17")
	#elif key == 24:
		#fire("Reserved 0x18")
	#elif key == 25:
		#fire("Reserved 0x19")
	#elif key == 26:
		#fire("Reserved 0x1A")
	#elif key == 27:
		#fire("Reserved 0x1B")
	#elif key == 28:
		#fire("Reserved 0x1C")
	#elif key == 29:
		#fire("Reserved 0x1D")
	#elif key == 30:
		#fire("Reserved 0x1E")
	#elif key == 31:
		#fire("Reserved 0x1F")
	elif key == 32:
		fire("Number0")
	elif key == 33:
		fire("Number1")
	elif key == 34:
		fire("Number2")
	elif key == 35:
		fire("Number3")
	elif key == 36:
		fire("Number4")
	elif key == 37:
		fire("Number5")
	elif key == 38:
		fire("Number6")
	elif key == 39:
		fire("Number7")
	elif key == 40:
		fire("Number8")
	elif key == 41:
		fire("Number9")
	#elif key == 42:
		#fire("Dot")
	elif key == 43:
		fire("Enter")
	elif key == 44:
		fire("Delete")
	#elif key == 45:
		#fire("Reserved 0x2D")
	#elif key == 46:
		#fire("Reserved 0x2E")
	elif key == 47:
		fire("Next Favorite")
	elif key == 48:
		fire("PageUp")
	elif key == 49:
		fire("PageDown")
	#elif key == 50:
		#fire("Previous Channel")
	#elif key == 51:
		#fire("Sound Select")
	#elif key == 52:
		#fire("Input Select")
	#elif key == 53:
		#fire("Display Information")
	#elif key == 54:
		#fire("Help")
	elif key == 55:
		fire("PageUp")
	elif key == 56:
		fire("PageDown")
	#elif key == 57:
		#fire("Reserved 0x39")
	#elif key == 58:
		#fire("Reserved 0x3A")
	#elif key == 59:
		#fire("Reserved 0x3B")
	#elif key == 60:
		#fire("Reserved 0x3C")
	#elif key == 61:
		#fire("Reserved 0x3D")
	#elif key == 62:
		#fire("Reserved 0x3E")
	#elif key == 63:
		#fire("Reserved 0x3F")
	#elif key == 64:
		#fire("Power")
	elif key == 65:
		fire("VolumeUp")
	elif key == 66:
		fire("VolumeDown")
	elif key == 67:
		fire("Mute")
	elif key == 68:
		fire("Play")
	elif key == 69:
		fire("Stop")
	elif key == 70:
		fire("Pause")
	elif key == 71:
		fire("Record")
	elif key == 72:
		fire("Rewind")
	elif key == 73:
		fire("FastForward")
	elif key == 74:
		fire("Eject")
	elif key == 75:
		fire("Forward")
	elif key == 76:
		fire("Backward")
	#elif key == 77: #This should stop registration. => Stop or Record. Which one?
		#fire("Stop-Record")
	#elif key == 78: #This should pause registration. => Pause or Record. Which one?
		#fire("Pause-Record")
	#elif key == 79:
		#fire("Reserved 0x4F")
	#elif key == 80:
		#fire("Angle")
	#elif key == 81:
		#fire("Sub Picture")
	#elif key == 82:
		#fire("Video On Demand")
	elif key == 83:
		fireWindow("TVGuide")
	#elif key == 84:
		#fire("Timer programming")
	#elif key == 85:
		#fire("Initial Configuration")
	#elif key == 86:
		#fire("Reserved 0x56")
	#elif key == 87:
		#fire("Reserved 0x57")
	#elif key == 88:
		#fire("Reserved 0x58")
	#elif key == 89:
		#fire("Reserved 0x59")
	#elif key == 90:
		#fire("Reserved 0x5A")
	#elif key == 91:
		#fire("Reserved 0x5B")
	#elif key == 92:
		#fire("Reserved 0x5C")
	#elif key == 93:
		#fire("Reserved 0x5D")
	#elif key == 94:
		#fire("Reserved 0x5E")
	#elif key == 95:
		#fire("Reserved 0x5F")
	#elif key == 96:
		#fire("Play Function")
	#elif key == 97:
		#fire("Pause-Play Function")
	#elif key == 98:
		#fire("Record Function")
	#elif key == 99:
		#fire("Pause-Record Function")
	#elif key == 100:
		#fire("Stop Function")
	#elif key == 101:
		#fire("Mute Function")
	#elif key == 102:
		#fire("Restore Volume Function")
	#elif key == 103:
		#fire("Tune Function")
	#elif key == 104:
		#fire("Select media Function")
	#elif key == 105:
		#fire("Select A/V Input Function")
	#elif key == 106:
		#fire("Select Audio input Function")
	#elif key == 107:
		#fire("Power Toggle Function")
	#elif key == 108:
		#fire("Power Off Function")
	#elif key == 109:
		#fire("Power On Function")
	#elif key == 110:
		#fire("Reserved 0x6E")
	#elif key == 111:
		#fire("Reserved 0x6F")
	#elif key == 112:
		#fire("Reserved 0x70")
	elif key == 113:
		fireWindow("TVChannels")
	elif key == 114:
		fireWindow("MyVideos")
	elif key == 115:
		fireWindow("MyMusic")
	elif key == 116:
		fireWindow("MyPictures")
	#elif key == 117:
		#fire("F5")
	#elif key == 118:
		#fire("Data")
	#else:
		#xbmcgui.Dialog().ok("Function not assigned to this key", str(key))
monitor = xbmc.Monitor()
 
while True:
    #if monitor.waitForAbort(0): # Sleep/wait for abort for 1 second.
    #   break # Abort was requested while waiting. Exit the while loop.
	
	data_raw = serConnection.readline()
	#xbmc.log("ArdCEC-Command: " + data_raw)
	if "KEY:68:" in data_raw:
		handleKey68(data_raw.rsplit(":", 1)[1])
	elif "KEY:138:" in data_raw:
		handleKey138(data_raw.rsplit(":", 1)[1])
	elif "KEY:65:" in data_raw:
		handleKey65(data_raw.rsplit(":", 1)[1])
	elif "KEY:66:" in data_raw:
		handleKey66(data_raw.rsplit(":", 1)[1])