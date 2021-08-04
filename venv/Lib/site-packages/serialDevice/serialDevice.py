import time
import serial
import serial.tools.list_ports

class Device():
	'''
		A Class to abstract a device connected by serial
		Attributes:
			name - The name of the device
			baud - The device's data rate
			vid - The device's vendor ID
			port - The device's port (found automatically by VID if none provided)
	'''

	def __init__(self, name=None, vid='0000',
					   port=None, baud='9600', 
					   bytesize=8,parity='N',
					   stopbits=1,timeout=None,
					   xonxoff=False,dsrdtr=False):
		
		self.name, self.vid = name, vid
		self.port, self.baud = port, baud
		self.bytesize, self.parity = bytesize, parity
		self.stopbits, self.timeout = stopbits, timeout
		self.xonxoff, self.dsrdtr = xonxoff, dsrdtr

		self.ser = serial.Serial()
		self.ser.port = self.port
		self.ser.baud = self.baud
		self.ser.bytesize = self.bytesize
		self.ser.parity = self.parity
		self.ser.stopbits = self.stopbits
		self.ser.timeout = self.timeout
		self.ser.xonxoff = self.xonxoff
		self.ser.dsrdtr = self.dsrdtr

	def connect(self, timeout=10):
		t1 = time.time()
		while not self.isOpen():
			t2 = time.time()
			
			if self.port == None:
				self.port = self.find()
				self.ser.port = self.port
			
			try:	
				self.ser.open()
			except:
				pass
			
			if (t2 - t1) > timeout:
				return False, 'Timeout'

		if self.isOpen():
			return True, self.ser.port
		else:
			return False

	def disconnect(self):
		try:
			self.ser.close()
		except:
			pass

		if self.isOpen():
			return False
		else:
			return True

	def find(self):
		# Make a list of all available ports on the system
		available_ports = list(serial.tools.list_ports.comports())
	
		# Sweep all ports
		for port in available_ports:
			for string in port:		# Sweep all strings in a given port list
				if self.vid in string:		# If any of these strings contain the VID
					return port[0]		# Return the first string, which is the port name

		return None

	def isOpen(self):
		return self.ser.isOpen()

	def read(self, length):
		return self.ser.read(length)

	def readline(self):
		return self.ser.readline()

	def write(self, data):
		try:
			self.ser.write(data)
			return True
		except:
			return False