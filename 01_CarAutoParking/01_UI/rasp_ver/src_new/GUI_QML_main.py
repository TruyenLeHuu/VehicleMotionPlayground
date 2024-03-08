########################################################################
###### STANDAR QT LIBRARIES
########################################################################
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtQml import * 
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import * 
#from PyQt5.QtChart import* #  pip install PyQtChart
#GUI raspberry: 
#sudo apt install python3-pyqt5
#sudo apt-get install qml-module-qtquick-controls
#sudo apt-get install qtquick.control
#sudo apt-get install qtquick.dialogs
#sudo apt-get install qtquick.extras
#sudo apt-get install qtquick.shapes
#sudo apt-get install qml-module-qtcharts

########################################################################
###### SPECIAL LIBRARIES
########################################################################

import random
import rospy
from std_msgs.msg import String
import json
from pynput import keyboard #pip install pynput

########################################################################
###### MAIN CLASS
########################################################################
class MainWindow(QObject):
	
	###### SIGNALS #####################################################

	# Signal Set Name
	setPage = pyqtSignal(str)
	
	# Signal Set Data
	printTime = pyqtSignal(str)
	printDate = pyqtSignal(str)
	valueGauge = pyqtSignal(str)
	printHour = pyqtSignal(str)

	# Signal position for control car by keyboard
	moveCarPosition = pyqtSignal(int, int)

	# Signal create parking slots (input: [{x, y}, {x1, y1}, ...] - x,y: float)
	# createCarParkingSlot = pyqtSignal(list)
	createCarParkingSlot = 0
	
	doneCarParking = 0

	parkingSlots = 0

	isCommand = 0
	
	command = ""
	
	params = 0

	desireBrake = 0

	desireSteering = 0

	isParking = 0

	createParkingSlot = pyqtSignal(list)
	# doneCarParking = pyqtSignal()

	def __init__(self, parent=None):
		super().__init__(parent)
		#### FIRST INIT FOR GUI ##############################################
		self.app = QApplication(sys.argv)
		self.app.setWindowIcon(QIcon("images/png_images/parking.png"))
		self.engine = QQmlApplicationEngine(self)
		# backend = QObject
		self.engine.rootContext().setContextProperty("backend", self)
		#self.engine.load(QUrl("src/qml/main.qml"))
		self.engine.load(QUrl("./qml/main.qml"))

		#### SETUP CUSTOM DATA ##############################################
		self.setupData()

		self.iniClock()

		#### CREATE KEYBOARD LISTENER USING FOR CONTROL CAR #################
		self.keyboard_listener = keyboard.Listener(
			# on_press=self.on_key_press,
			# on_release=self.on_key_release
			)
		self.keyboard_listener.start()
		# create thread for socket client

		self.ros_init()

		# self.client_thread = threading.Thread(target= self.ros_listener)

		# self.client_thread.start()
	
		sys.exit(self.app.exec_())
	
	####################################################################
	###### EVENT TRIGGER FOR KEY PRESS
	####################################################################
	def on_key_press(self, key):
		# print(key)
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
	###### Function to init ros listener and ros publicher
	####################################################################
	def ros_init(self):
		rospy.init_node('ui', anonymous=True)

		rospy.Subscriber("steering", String, self.ros_handle_steering_angle)
		
		rospy.Subscriber("speed", String, self.ros_handle_vehicle_speed)
		
		rospy.Subscriber("brake", String, self.ros_handle_brake_pressure)

		rospy.Subscriber("chatter", String, self.ros_handle_slots_position)

		rospy.Subscriber("control_command", String, self.ros_handle_commands)

		rospy.Subscriber("control_params", String, self.ros_handle_params)

		rospy.Subscriber("done_parking", String, self.ros_handle_done_parking)

		self.pub = rospy.Publisher('chosen_position', String, queue_size=10)

		self.pub_start = rospy.Publisher("start_parking", String, queue_size=10)

	####################################################################
	###### Function to handle msg from talkers
	####################################################################
	def ros_handle_steering_angle(self, message):
		try:
			self.set_steeringAngle(int(message.data))
			#print("Received from server:", message.data)
		except Exception as e:
			print("Error:", str(e))

	def ros_handle_vehicle_speed(self, message):
		try:
			self.set_vehicleSpeed(int(message.data))
			#print("Received from server:", message.data)
		except Exception as e:
			print("Error:", str(e))

	def ros_handle_brake_pressure(self, message):
		try:
			self.set_brakePressure(float(message.data))
			# print("Received from server:", message.data)
		except Exception as e:
			print("Error:", str(e))

	def ros_handle_slots_position(self, message):
		try:
			print(message)
			parse_data = json.loads(message.data)
			msg = parse_data["slots"]
			msg.append(parse_data["init_position"])
			print(msg)
			self.parkingSlots = msg
			# self.createParkingSlot.emit(msg)
			self.createCarParkingSlot = 1
		except Exception as e:
			print("Error:", str(e))

	def ros_handle_commands(self, message):
		try:
			self.command = str(message.data)
			self.isCommand = 1
		except Exception as e:
			print("Error:", str(e))

	def ros_handle_params(self, message):
		try:
			self.params = json.loads(str(message.data))
			# print(self.params)
			self.desireBrake = self.params["brake"]
			self.desireSteering = self.params["steer"]
		except Exception as e:
			print("Error:", str(e))

	def ros_handle_done_parking(self, message):
		try:
			# self.doneCarParking.emit()
			self.isParking = 0
			self.doneCarParking = 1
		except Exception as e:
			print("Error done car parking:", str(e))

			"""parse_data = json.loads(message.data)
			topic = parse_data["topic"]
			if (topic == "vehicle_speed"):
				# json.dumps({"topic": "vehicle_speed", "speed": 134})
				msg = parse_data["speed"]
				self.set_vehicleSpeed(int(msg))
				# print(msg, topic)
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
			# print("Received from server:", json.loads(data.decode('utf-8'))["slots"][0]["x"])"""
		
	def ros_publish_msg(self, message):
		rospy.loginfo(message)
		self.pub.publish(message)
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

# 		self.vehicleSpeed = random.randint(10,200)
		# numTest = "30"
		# self.valueGauge.emit(numTest)
		# print(self.vehicleSpeed)
		self.printTime.emit(formatDate)
		self.printDate.emit(date)
		self.printHour.emit(time)

	######   Just init data ############################################
	def setupData(self):
		self.brakePressure = 0
		self.vehicleSpeed = 0
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

	def set_vehicleSpeed(self, value):
		self.vehicleSpeed = value
		
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
	def get_desireBrakePressure(self):
		return self.desireBrake

	@pyqtSlot(result=float)
	def get_desireSteeringAngle(self):
		return self.desireSteering
	
	@pyqtSlot(result=float)
	def get_vehicleSpeed(self):
		return self.vehicleSpeed
	
	@pyqtSlot(result=float)
	def get_steeringAngle(self):
		return self.steeringAngle

	@pyqtSlot(result=int)
	def get_doneCarParking(self):
		return self.doneCarParking

	@pyqtSlot(result=int)
	def get_createCarParkingSlot(self):
		return self.createCarParkingSlot
	
	@pyqtSlot(result=list)
	def get_slots(self):
		return self.parkingSlots

	@pyqtSlot(result=int)
	def get_isCommand(self):
		return self.isCommand

	@pyqtSlot(result=int)
	def get_isParking(self):
		return self.isParking

	@pyqtSlot(result=str)
	def get_command(self):
		return self.command

	######   Callback function when user choose slot  ##################
	@pyqtSlot('int')
	def chooseSlot(self, value):
		msgChosenSlot =  json.dumps({"topic": "slot_chosen", "slot": value})
		try: 
			self.ros_publish_msg(msgChosenSlot)
		except Exception as e:
			print("Error hosen slot:", str(e))
		print("Driver choosen slot", value)

	@pyqtSlot()
	def send_parking_signal(self):
		try: 
			print("Start parking")
			self.isParking = 1
			self.pub_start.publish("start")
		except Exception as e:
			print("Error:", str(e))


	######   Function Set Car Rotation from Frontend  ##################
	@pyqtSlot('int')
	def setCarRotation(self, value):
		self.car_rotation = value	
	
	@pyqtSlot('int')
	def setDoneCarParking(self, value):
		self.doneCarParking = value	

	@pyqtSlot('int')
	def setCreateCarParkingSlot(self, value):
		self.createCarParkingSlot = value	

	@pyqtSlot('int')
	def setIsCommand(self, value):
		self.isCommand = value	

####################################################################
###### MAIN ROUTINE
####################################################################
if __name__ == '__main__':
	main = MainWindow()













































































