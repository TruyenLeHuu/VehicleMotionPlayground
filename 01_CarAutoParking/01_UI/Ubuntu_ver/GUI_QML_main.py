########################################################################
###### STANDAR QT LIBRARIES
########################################################################
import sys
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtQml import * 
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import * 
from PyQt5.QtChart import* #  pip install PyQtChart

########################################################################
###### SPECIAL LIBRARIES
########################################################################

import random
import socket
import threading
import json
from pynput import keyboard #pip install pynput

########################################################################
###### MAIN CLASS
########################################################################
class MainWindow(QObject):
	
	###### SIGNALS #####################################################
	# Signal Set Name
	setName = pyqtSignal(str)
	
	# Signal Set Name
	setPage = pyqtSignal(str)
	
	# Signal Set Port selected
	setCom = pyqtSignal(str)
	
	# Signal Set Data
	printTime = pyqtSignal(str)
	printDate = pyqtSignal(str)
	valueGauge = pyqtSignal(str)
	printHour = pyqtSignal(str)
	
	# Server parameters
	serverIp = '127.0.0.1'  # Replace with the IP address of the server
	serverPort = 12345

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	
	
	# Signal Visible
	isVisible = pyqtSignal(bool)

	# Open File To Text Edit
	readText = pyqtSignal(str)

	# Signal position for control car by keyboard
	moveCarPosition = pyqtSignal(int, int)

	# Signal create parking slots (input: [{x, y}, {x1, y1}, ...] - x,y: float)
	createCarParkingSlot = pyqtSignal(list)

	def __init__(self, parent=None):
		super().__init__(parent)
		#### FIRST INIT FOR GUI ##############################################
		self.app = QApplication(sys.argv)
		self.app.setWindowIcon(QIcon("images/png_images/parking.png"))
		self.engine = QQmlApplicationEngine(self)
		self.engine.rootContext().setContextProperty("backend", self)
		self.engine.load(QUrl("./qml/main.qml"))
		
		#### SETUP CUSTOM DATA ##############################################
		self.setupData()

		self.iniClock()

		#### CREATE KEYBOARD LISTENER USING FOR CONTROL CAR #################
		self.keyboard_listener = keyboard.Listener(
			on_press=self.on_key_press,
			on_release=self.on_key_release)
		self.keyboard_listener.start()
		# create thread for socket client

		# self.client_thread = threading.Thread(target= self.handle_server)

		# self.client_thread.start()
	
		sys.exit(self.app.exec_())
	
	####################################################################
	###### EVENT TRIGGER FOR KEY PRESS
	####################################################################
	def on_key_press(self, key):
		try:
			if key == keyboard.Key.up and key == keyboard.Key.left:
				self.car_speed += 1
				self.car_rotation -= 5
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
			elif key == keyboard.Key.down and key == keyboard.Key.left:
				self.car_speed -= 1
				self.car_rotation -= 5
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
			elif key == keyboard.Key.up and key == keyboard.Key.right:
				self.car_speed += 1
				self.car_rotation += 5
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
			elif key == keyboard.Key.down and key == keyboard.Key.right:
				self.car_speed -= 1
				self.car_rotation += 5
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
			elif key == keyboard.Key.up:
				self.car_speed += 1
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
			elif key == keyboard.Key.down:
				self.car_speed -= 1
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
			elif key == keyboard.Key.left:
				self.car_rotation -= 5
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
			elif key == keyboard.Key.right:
				self.car_rotation += 5
				self.moveCarPosition.emit(self.car_speed, self.car_rotation)
				# print(self.car_speed, self.car_rotation)
		except AttributeError:
			pass
	####################################################################
	###### EVENT TRIGGER FOR KEY RELEASE
	####################################################################
	def on_key_release(self, key):
		if key == keyboard.Key.up or key == keyboard.Key.down:
			self.car_speed = 0
			self.moveCarPosition.emit(self.car_speed, self.car_rotation)

	####################################################################
	###### Function to handle server connection
	####################################################################
	def handle_server(self):
		try:
		# Connect to the server
			self.client_socket.connect((self.serverIp, self.serverPort))
			
			while True:
				# Receive data from the server
				data = self.client_socket.recv(1024)
				parse_data = json.loads(data.decode('utf-8'))
				topic = parse_data["topic"]
				if (topic == "vehicle_speed"):
					# json.dumps({"topic": "vehicle_speed", "speed": 134})
					msg = parse_data["speed"]
					self.set_engineSpeed(int(msg))
					print(msg, topic)
				elif (topic == "steering_angle"):
					# json.dumps({"topic": "steering_angle", "angle": -134})
					msg = parse_data["angle"]
					self.set_steeringAngle(msg)
				elif (topic == "brake_pressure"):
					# json.dumps({"topic": "brake_pressure", "pressure": 89.12})
					msg = parse_data["pressure"]
					self.set_brakePressure(msg)
				elif (topic == "slots_position"):
					# json.dumps({"topic": "slots_position", "slots": [{"x": 120, "y": 770}, {"x": 600, "y": 1070}]})
					msg = parse_data["slots"]
					self.createCarParkingSlot.emit(msg)
				print("Received from server:", parse_data)
				# print("Received from server:", json.loads(data.decode('utf-8'))["slots"][0]["x"])
		
		except Exception as e:
			print("Error:", str(e))
		finally:
			# Close the socket
			self.client_socket.close()

	####################################################################
	###### CLOCK TIME
	####################################################################
	def iniClock(self):
		self.timer = QTimer()
		self.timer.timeout.connect(lambda: self.setTime())
		self.timer.start(1000)
	
	def setTime(self):
		current_time = QTime.currentTime()
		time = current_time.toString('HH:mm:ss')
		date =  QDate.currentDate().toString(Qt.ISODate)
		formatDate= 'Now is '+date+' '+time
		
		numTest = str(random.randint(10,100))
		self.valueGauge.emit(numTest)
		self.printTime.emit(formatDate)
		self.printDate.emit(date)
		self.printHour.emit(time)

	######   Just init data ############################################
	def setupData(self):
		self.brakePressure = 0
		self.engineSpeed = 0
		self.steeringAngle = 0
		self.car_speed = 0
		self.car_rotation = 0
	
	######   Function Set Name To Page #################################
	@pyqtSlot(str)
	def namePage(self, pagex):
		self.setPage.emit(pagex)

	####################################################################
	# API SET VALUE FOR GUI - FRONTEND
	####################################################################
	def set_steeringAngle(self, value):
		self.steeringAngle = value

	def set_engineSpeed(self, value):
		self.engineSpeed = value
		
	def set_brakePressure(self, value):
		self.brakePressure = value

	####################################################################
	# REFERENCE TIME FOR GRAPHICS : VOLATILE CHART
	####################################################################
	@pyqtSlot(result=int)
	def get_tiempo(self):
		date_time = QDateTime.currentDateTime()
		unixTIME = date_time.toSecsSinceEpoch()
		return unixTIME
	
	####################################################################
	# SEND DATA FROM PYTHON TO GUI - FRONTEND
	####################################################################
	@pyqtSlot(result=float)
	def get_brakePressure(self):
		return self.brakePressure
	
	@pyqtSlot(result=float)
	def get_engineSpeed(self):
		return self.engineSpeed
	
	@pyqtSlot(result=float)
	def get_steeringAngle(self):
		return self.steeringAngle

	######   Callback function when user choose slot  ##################
	@pyqtSlot('int')
	def chooseSlot(self, value):
		msgChosenSlot =  json.dumps({"topic": "slot_chosen", "slot": value})
		try: 
			self.client_socket.sendall(msgChosenSlot.encode('utf-8'))
		except Exception as e:
			print("Error:", str(e))
		print("Driver choosen slot", value)

	######   Function Set Car Rotation from Frontend  ##################
	@pyqtSlot('int')
	def setCarRotation(self, value):
		self.car_rotation = value	

####################################################################
###### MAIN ROUTINE
####################################################################
if __name__ == '__main__':
	main = MainWindow()



















































































