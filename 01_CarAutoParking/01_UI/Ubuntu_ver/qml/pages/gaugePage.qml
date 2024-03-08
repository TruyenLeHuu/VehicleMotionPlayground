
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0

import QtQuick 2.12
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.12
import QtQuick.Shapes 1.12
import QtGraphicalEffects 1.0

import "../controls"

Item {
	
	Rectangle {
		
		id: rectangle0
		color: "#090909"
		height: parent.height
		width: (parent.width - 300*mainWindow.scale)
		anchors.top : parent.top
        anchors.left : parent.left

		property int chosenSlotY: 0
		property int chosenSlotX: 0
		property int carX: (width) / 2
        property int carY: (height) / 2
		// property int carX: 0
        // property int carY: 0
        property int carRotation: 0
        property int carSpeed: 0
		property int isChosen: 0

		property int lineW: 10
		property int lineH: 50
		property int distance: 200
		property string labelAnnouncement: "Please choose your parking slot!"
		
		Rectangle {
			id: line0
			height: rectangle0.lineH
			width: rectangle0.lineW
			z: 1
			x: (parent.width-width) /2 - 100*mainWindow.scale
			color: "white"
			SequentialAnimation {
				id: animationLine
				loops: Animation.Infinite
				running: true
				NumberAnimation { target: line0; property: "y"; from: -200*mainWindow.scale; to: 1000*mainWindow.scale; duration: 4000}
			}
		}
		SequentialAnimation {
			id: initLocationCarAnimation
			loops: 1
			running: false
			NumberAnimation { target: rectangle0; property: "carSpeed"; to: 7; duration: 900}
			NumberAnimation { target: rectangle0; property: "carSpeed"; from: 7; to: 0; duration: 500}
		}
		Rectangle {
				id: linet4
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: linet3.y - rectangle0.distance
				x:  line0.x
				color: "white"
		}
		Rectangle {
				id: linet3
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: linet2.y - rectangle0.distance
				x:  line0.x
				color: "white"
		}
		Rectangle {
				id: linet2
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: linet1.y - rectangle0.distance
				x:  line0.x
				color: "white"
		}
		Rectangle {
				id: linet1
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line0.y - rectangle0.distance
				x:  line0.x
				color: "white"
		}
		Rectangle {
				id: line1
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line0.y + rectangle0.distance
				x:  line0.x
				color: "white"
		}
		Rectangle {
				id: line2
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line1.y + rectangle0.distance
				x:  line0.x
				color: "white"
		}
		Rectangle {
				id: line3
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line2.y + rectangle0.distance
				x:  line0.x
				color: "white"
		}
		Rectangle {
				id: linert4
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: linet3.y - rectangle0.distance
				x:  liner0.x
				color: "white"
		}
		Rectangle {
				id: linert3
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: linet2.y - rectangle0.distance
				x:  liner0.x
				color: "white"
		}
		Rectangle {
				id: linert2
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: linet1.y - rectangle0.distance
				x:  liner0.x
				color: "white"
		}
		Rectangle {
				id: linert1
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line0.y - rectangle0.distance
				x:  liner0.x
				color: "white"
		}
		Rectangle {
				id: liner0
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line0.y
				x:  (parent.width-width) /2 + 100*mainWindow.scale
				color: "white"
		}
		Rectangle {
				id: liner1
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line0.y + rectangle0.distance
				x:  liner0.x
				color: "white"
		}
		Rectangle {
				id: liner2
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line1.y + rectangle0.distance
				x:  liner0.x
				color: "white"
		}
		Rectangle {
				id: liner3
				height: rectangle0.lineH
				width: rectangle0.lineW
				z: 1
				y: line2.y + rectangle0.distance
				x:  liner0.x
				color: "white"
		}
		Image 
		{
			id: lane
			// scale: 0.6
			anchors.fill: parent
			source: "../../images/lane.png"
		}
		Image 
		{
			id: bush
			scale: 0.1
			x: -600*mainWindow.scale
			y: linet1.y
			z: 1
			smooth: true
			source: "../../images/png_images/bush.png"

		}
		Rectangle {
        	id: container
			z: 2
			visible:true
    	}
		Image 
		{

			id: car
			width: 446 * 0.3 *mainWindow.car_scale
			height: 850 * 0.3 *mainWindow.car_scale

			x: rectangle0.carX - width/2
			y: rectangle0.carY - height/2
			z: 3

			smooth: true
			source: "../../images/png_images/car-top-view.png"
			rotation: rectangle0.carRotation

			Timer {
                interval: 16  // Update interval in milliseconds (roughly 60 FPS)
                running: true
                repeat: true
                onTriggered: {
                    rectangle0.carY -= rectangle0.carSpeed * Math.cos(rectangle0.carRotation * Math.PI / 180);
                    rectangle0.carX += rectangle0.carSpeed * Math.sin(rectangle0.carRotation * Math.PI / 180);
					car.rotation = rectangle0.carRotation
                }
            }
		}
	}
	Rectangle {
		id: rectangle
		color: "#161616"
		height: parent.height
		width: 300*mainWindow.scale
		anchors.top : parent.top
        anchors.left : parent.left
        anchors.leftMargin: parent.width - width
		// anchors.fill: parent
		property int widthBrakeGauge: 300*mainWindow.gauge_scale
		property int heightBrakeGauge: 300*mainWindow.gauge_scale

		property int widthSpeedGauge: 250*mainWindow.gauge_scale
		property int heightSpeedGauge: 250*mainWindow.gauge_scale

		property int widthSAngleGauge: 250*mainWindow.gauge_scale
		property int heightSAngleGauge: 250*mainWindow.gauge_scale
		
		property int yValueBrakeGauge: 80*mainWindow.gauge_scale
		property bool isTakeSteeringValue: true

	// ############## INI GAUGE 0  #####################################
	Rectangle {
		id:speedRect
		width: parent.widthSpeedGauge
        height: parent.heightSpeedGauge
        anchors.top : parent.top
        anchors.topMargin: 30
        anchors.left : parent.left
        anchors.leftMargin: (parent.width-height)/2
        visible: true
        color: "#00000000"
		
		//###### Shader effect to provide gradient-based gauge #########
		ShaderEffect {
			id: shader0
			anchors.fill: parent
			opacity: 0.85  
			property real angleBase: -pi*0.80
			property real angle: ((1.6*pi*(speedGauge.value)/(speedGauge.maximumValue-speedGauge.minimumValue))+pi*(0.8-(1.6*speedGauge.maximumValue/(speedGauge.maximumValue-speedGauge.minimumValue))))
			// ANGLE= [1.6*PI*(MEASURE)/(MAX-MIN)]+PI*(0.8-(1.6*MAX/(MAX-MIN)))
			readonly property real pi: 3.1415926535897932384626433832795
			vertexShader: "
			uniform highp mat4 qt_Matrix;
			attribute highp vec4 qt_Vertex;
			attribute highp vec2 qt_MultiTexCoord0;
			varying highp vec2 coord;
			
			void main() {
				coord = qt_MultiTexCoord0;
				gl_Position = qt_Matrix * qt_Vertex;
				}"

			fragmentShader: "
			uniform lowp float qt_Opacity;
			uniform highp float angleBase;
			uniform highp float angle;
			varying highp vec2 coord;
			void main() {
				gl_FragColor = vec4(0.0,0.0,0.0,0.0); 
				highp vec2 d=2.0*coord-vec2(1.0,1.0);
				highp float r=length(d);
				if (0.6<=r && r<=0.9) {
					highp float a=atan(d.x,-d.y);
					if (angleBase<=a && a<=angle) {
						highp float p=(a-angleBase)/(angle-angleBase);
						gl_FragColor = vec4(0,0.0,0.4+0.6*p,p) * qt_Opacity;
						}
					}
				}"
			}
		//##### END Shader effect  #####################################
		CircularGauge {
			
			Behavior on value {
				NumberAnimation {
					duration: 900
				}
			}
			id: speedGauge
			width: 0.9*speedRect.width
			height: 0.9*speedRect.width
			maximumValue: 200
			minimumValue: 0
			value: 100
			anchors.centerIn: parent
			style: CircularGaugeStyle {
				id: style2
				labelInset: outerRadius * 0.22
				labelStepSize: 20
				minorTickmarkInset :45
				tickmarkInset : 6
				minorTickmarkCount : 5
				tickmarkStepSize : 20
				function degreesToRadians(degrees) {
					return degrees * (Math.PI / 180);
				}

				background: Canvas {
				
					onPaint: {
						var ctx = getContext("2d");
						ctx.reset();
						/*
						ctx.beginPath();
						ctx.strokeStyle = "#ff8000";
						ctx.lineWidth = outerRadius * 0.1;
						ctx.arc(outerRadius, outerRadius, outerRadius - ctx.lineWidth / 2,degreesToRadians(valueToAngle(20) - 90), degreesToRadians(valueToAngle(50) - 90));
						ctx.stroke();
						ctx.beginPath();
						ctx.strokeStyle = "#ffff00";
						ctx.lineWidth = outerRadius * 0.05;
						ctx.arc(outerRadius, outerRadius, 0.75*outerRadius - ctx.lineWidth / 2,degreesToRadians(valueToAngle(20) - 90), degreesToRadians(valueToAngle(50) - 90));
						ctx.stroke();
						*/
						ctx.beginPath();
						ctx.strokeStyle = "#f0f0f0";
						ctx.lineWidth = outerRadius * 0.02;
						ctx.arc(outerRadius, outerRadius, 1*outerRadius - ctx.lineWidth / 2,degreesToRadians(valueToAngle(0) - 90), degreesToRadians(valueToAngle(speedGauge.maximumValue) - 90));
						ctx.stroke();
						
						ctx.beginPath();
						ctx.strokeStyle = "#f0f0f0";
						ctx.lineWidth = outerRadius * 0.02;
						ctx.arc(outerRadius, outerRadius, 0.67*outerRadius - ctx.lineWidth / 2,degreesToRadians(valueToAngle(0) - 90), degreesToRadians(valueToAngle(speedGauge.maximumValue) - 90));
						ctx.stroke();
						
					}
				}

				
				tickmark: Rectangle {
					visible: styleData.value > 0  //|| styleData.value % 20 == 0  // styleData.value < 3 || 
					implicitWidth: outerRadius * 0.03
					antialiasing: true
					implicitHeight: outerRadius * 0.05
					color: styleData.value <= 50 ? "#ffff00" : "#ffff00"
				}
				

				minorTickmark: Rectangle {
					visible: styleData.value > 0 //styleData.value < 20  //|| styleData.value % 1 == 0
					implicitWidth: outerRadius * 0.05
					antialiasing: true
					implicitHeight: outerRadius * 0.07
					color: styleData.value < speedGauge.value ? "#00ff00" : "#404040"
					
				}

				tickmarkLabel:  Text {
					visible: styleData.value > 0
					font.pixelSize: Math.max(6, outerRadius * 0.12)
					text: styleData.value
					color: styleData.value <= 40 ? "#e0e0e0" : "#e0e0e0"
					antialiasing: true
				}
				//#################
				needle: Canvas {
					property real needleBaseWidth: 10
					property real needleLength: outerRadius
					property real needleTipWidth: 1
					property real needleShort: outerRadius*0.6
					implicitWidth: needleBaseWidth
					implicitHeight: needleLength

					property real xCenter: width / 2
					property real yCenter: height / 2

					onPaint: {
						var ctx = getContext("2d");
						ctx.reset();

						ctx.beginPath();
						ctx.moveTo(xCenter, height-needleShort);
						ctx.lineTo(xCenter - needleBaseWidth / 2, (height-needleShort) - needleBaseWidth / 2);
						ctx.lineTo(xCenter - needleTipWidth / 2, 0);
						//ctx.lineTo(xCenter, yCenter - needleLength-needleShort);
						ctx.lineTo(xCenter, 0);
						ctx.closePath();
						ctx.fillStyle = Qt.rgba(0, 0.9, 0, 0.9);
						ctx.fill();

						
						ctx.beginPath();
						ctx.moveTo(xCenter, height-needleShort)
						ctx.lineTo(width, height-needleShort - needleBaseWidth / 2);
						ctx.lineTo(xCenter + needleTipWidth / 2, 0);
						ctx.lineTo(xCenter, 0);
						ctx.closePath();
						ctx.fillStyle = Qt.lighter(Qt.rgba(0, 0.7, 0, 0.9));
						ctx.fill();
						
					}
				}
				//##################
				foreground: Item {
					Rectangle {
					}
				}

			}
			Rectangle {
				id:rectsg2
				anchors.horizontalCenter: parent.horizontalCenter
				anchors.verticalCenter: parent.verticalCenter 
				//y: 220
				width: 0.26*speedGauge.width
				height: 0.13*speedGauge.width
				color: "#00000000"
				Text {
					id:textspeedGauge
					anchors.horizontalCenter: parent.horizontalCenter
					y: 40
					text: Math.floor(speedGauge.value)
					// text: car.rotation
					font.family: "Helvetica"
					font.pointSize: Math.max(6, parent.width * 0.4)
					color:"#e5e5e5"
				}
			}
			//
			Rectangle {
				id:rectsg2a
				anchors.horizontalCenter: parent.horizontalCenter
				anchors.verticalCenter: parent.verticalCenter 
				//y: 220
				width: 0.26*speedGauge.width
				height: 0.13*speedGauge.width
				color: "#00000000"
				Text {
					id:textspeedGaugea
					anchors.horizontalCenter: parent.horizontalCenter
					y: -10
					text: "Km/h"
					font.family: "Helvetica"
					font.pointSize: Math.max(6, parent.width * 0.4)
					color: "#e5e5e5"
				}
			}
			Label {
                text: "Vehicle Speed"
                color: "#00A5FF"
                font.pointSize: 16
                anchors.bottom: speedGauge.top
                anchors.bottomMargin: 10
                anchors.horizontalCenter: parent.horizontalCenter
            }
		}
	
	}
	// ############## FIN GAUGE 0  #####################################
	// ############## INI GAUGE 1  #####################################
	Rectangle {
		id:brakeRect

		width: parent.widthBrakeGauge	
        height: parent.heightBrakeGauge
        anchors.top : parent.top
        anchors.topMargin: 440
        anchors.left : parent.left
        anchors.leftMargin: (parent.width-height)/2
        visible: true
        color: "#00000000"
		//###### Shader effect to provide gradient-based gauge #########
		ShaderEffect {
			id: shader1
			antialiasing: true
			anchors.fill: parent
			opacity: 0.95  
			property real angleBase: -pi*0.80
			property real angle: ((1.6*pi*(brakeGauge.value)/(brakeGauge.maximumValue-brakeGauge.minimumValue))+pi*(0.8-(1.6*brakeGauge.maximumValue/(brakeGauge.maximumValue-brakeGauge.minimumValue))))
			// ANGLE= [1.6*PI*(MEASURE)/(MAX-MIN)]+PI*(0.8-(1.6*MAX/(MAX-MIN)))
			readonly property real pi: 3.1415926535897932384626433832795
			vertexShader: "
			uniform highp mat4 qt_Matrix;
			attribute highp vec4 qt_Vertex;
			attribute highp vec2 qt_MultiTexCoord0;
			varying highp vec2 coord;
			
			void main() {
				coord = qt_MultiTexCoord0;
				gl_Position = qt_Matrix * qt_Vertex;
				}"

			fragmentShader: "
			uniform lowp float qt_Opacity;
			uniform highp float angleBase;
			uniform highp float angle;
			varying highp vec2 coord;
			void main() {
				gl_FragColor = vec4(0.0,0.0,0.0,0.0); 
				highp vec2 d=2.0*coord-vec2(1.0,1.0);
				highp float r=length(d);
				if (0.45<=r && r<=0.55) {
					highp float a=atan(d.x,-d.y);
					if (angleBase<=a && a<=angle) {
						highp float p=(a-angleBase)/(angle-angleBase);
						gl_FragColor = vec4(0.4+0.6*p,0,0,p) * qt_Opacity;
						}
					}
				}"
			}
		//##### END Shader effect  #####################################
		CircularGauge {
			
			Behavior on value {
				NumberAnimation {
					duration: 100
				}
			}
			id: brakeGauge
			width: 0.72*brakeRect.width
			height: 0.72*brakeRect.width
			maximumValue: 110
			minimumValue: 0
			value: 110
			anchors.centerIn: parent
			style: CircularGaugeStyle {
				id: style1
				labelInset: outerRadius * 0.01
				labelStepSize: 10
				minorTickmarkInset :25
				tickmarkInset : 14
				minorTickmarkCount : 5
				tickmarkStepSize : 10
				function degreesToRadians(degrees) {
					return degrees * (Math.PI / 180);
				}
				needle: Rectangle {
					width: 0.1
					height: 0.1
					color: "red" // Change the color here
					anchors.centerIn: parent
            	}
				background: Canvas {
				
					onPaint: {
						var ctx = getContext("2d");
						ctx.reset();
					}
				}

				
				tickmark: Rectangle {
					visible: styleData.value >= 0  //|| styleData.value % 20 == 0  // styleData.value < 3 || 
					implicitWidth: outerRadius * 0.03
					antialiasing: true
					implicitHeight: outerRadius * 0.24
					color: styleData.value <= 50 ? "#ffff00" : "#ffff00"
				}
				

				minorTickmark: Rectangle {
					visible: styleData.value > 0 //styleData.value < 20  //|| styleData.value % 1 == 0
					implicitWidth: outerRadius * 0.01
					antialiasing: true
					implicitHeight: outerRadius * 0.11
					color: styleData.value <= 40 ? "#00ff00" : "#00ff00"
				}

				tickmarkLabel:  Text {
					visible: styleData.value >= 0
					font.pixelSize: Math.max(6, outerRadius * 0.18)
					text: styleData.value 
					color: styleData.value <= 40 ? "#e0e0e0" : "#e0e0e0"
					antialiasing: true
				}
				foreground: Item {
					Rectangle {
					}
				}

			}
			Rectangle {
				id:rectsg1
				anchors.horizontalCenter: parent.horizontalCenter
				anchors.verticalCenter: parent.verticalCenter 
				//y: 220
				width: 0.26*brakeGauge.width
				height: 0.13*brakeGauge.width
				color: "#00000000"
				Text {
					id:textbrakeGauge
					anchors.horizontalCenter: parent.horizontalCenter
					y: rectangle.yValueBrakeGauge
					text: (brakeGauge.value).toFixed(2)
					font.family: "Helvetica"
					font.pointSize: Math.max(6, parent.width * 0.4)
					color: "#e5e5e5"
				}
			}
			//
			Rectangle {
				id:rectsg1a
				anchors.horizontalCenter: parent.horizontalCenter
				anchors.verticalCenter: parent.verticalCenter 
				//y: 220
				width: 0.26*brakeGauge.width
				height: 0.13*brakeGauge.width
				color: "#00000000"
				Text {
					id:textbrakeGaugea
					anchors.horizontalCenter: parent.horizontalCenter
					y: -10
					text: "Bar"
					font.family: "Helvetica"
					font.pointSize: Math.max(6, parent.width * 0.4)
					color: "#e5e5e5"
				}
			}
			Label {
                text: "Brake Pressure"
                color: "#00A5FF"
                font.pointSize: 16
                anchors.bottom: brakeGauge.top
                anchors.bottomMargin: 10
                anchors.horizontalCenter: parent.horizontalCenter
            }
		}
	
	}
	// ############## FIN GAUGE  1  ####################################
	// ############## INI GAUGE 2  #####################################
	Rectangle {
		id: sAngleRect
        width: parent.widthSAngleGauge
        height: parent.heightSAngleGauge
        anchors.top : parent.top
        anchors.topMargin: 240
        anchors.left : parent.left
        anchors.leftMargin: (parent.width-height)/2
        visible: true
        color: "#00000000"
        CircularSlider {
            id: customSlider
            hideProgress: true
            hideTrack: true
            width: parent.width
            height: parent.height

            handleColor: "#6272A4"
            handleWidth: 32
            handleHeight: 32
            minValue: -540
            maxValue: 540
            interactive: false
            
            Behavior on value {
				NumberAnimation {
					duration: 150
				}
			}

            // Custom progress Indicator
            Item {
                anchors.fill: parent
                anchors.margins: 5
                Rectangle{
                    id: mask
                    anchors.fill: parent
                    radius: width / 2
                    color: "#282A36"
                    border.width: 5
                    border.color: "#44475A"
                }

                Item {
                    anchors.fill: mask
                    anchors.margins: 5
                    layer.enabled: true
                   // rotation: customSlider.value / 10 - 50
				   	rotation: customSlider.value
                    layer.effect: OpacityMask {
                        maskSource: mask
                    }
                    Rectangle {
                        height: parent.height  //customSlider.value / customSlider.maxValue
                        width: parent.width
                        color:"#5B99A6"
                    }
                    Image {
                        id: icon1
						scale: 0.6
                        anchors.fill: parent
                        source: "../../images/svg_images/avion.png"
                    }
                }

                Label {
                    //anchors.centerIn: parent
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 0.1*parent.width-5
                    font.pointSize: 20*mainWindow.scale
                    color: "#ffffff"
                    //text: Number(customSlider.value).toFixed()
                    text: Number(customSlider.value).toFixed()
                }
                Rectangle {
					anchors.horizontalCenter: parent.horizontalCenter
					anchors.verticalCenter: parent.verticalCenter 
					//y: 220
					width: 0.26*parent.width
					height: 0.13*parent.width
					color: "#00000000"
					Text {
						anchors.horizontalCenter: parent.horizontalCenter
						y: parent.width+10
						text: "Degrees"
						font.family: "Helvetica"
						font.pointSize: Math.max(6, parent.width * 0.3)
						// color: "#404040"
						color: "#ffffff"
					}
				}
            }
            Label {
                text: "Steering Angle"
                color: "#00A5FF"
                font.pointSize: 16
                anchors.bottom: customSlider.top
                anchors.bottomMargin: 5
                anchors.horizontalCenter: parent.horizontalCenter
            }
			Image {
            id: imageItem
            width: 370
            height: imageItem.width
			x: -44
			y: -34
            source:  "../../images/png_images/shield.png"

            property real animationDuration: 1500 
            opacity: 0 
			SequentialAnimation {
				id: animationSteering
				loops: 1
				running: false
				NumberAnimation { target: rectangle; property: "isTakeSteeringValue"; to: 0}
				// PauseAnimation { duration: imageItem.animationDuration } // Đợi 1 giây
				NumberAnimation { target: imageItem; property: "opacity"; to: 1; duration: imageItem.animationDuration - 500 } // Hiển thị trong 1 giây
				PauseAnimation { duration: imageItem.animationDuration } // Đợi 1 giây
				NumberAnimation { target: imageItem; property: "opacity"; to: 0; duration: 250 } // Ẩn trong 1 giây
				NumberAnimation { target: rectangle; property: "isTakeSteeringValue"; to: 1}
			}
        }
		}	
    }
	// ############## FIN GAUGE 2  #####################################	/////////
	}
	
	//
	Button {
			id: button1
			text: qsTr("Start Parking")
			y: (parent.height - 50*mainWindow.car_scale) 
			// enabled: true
			font.pointSize: 10*mainWindow.car_scale
			onClicked: {
				var parkingSlot = [{x:rectangle0.carX - 240*mainWindow.car_scale, y:rectangle0.carY + 100*mainWindow.car_scale, id: "null"}, {x:rectangle0.carX + 240*mainWindow.car_scale, y:rectangle0.carY+ 600*mainWindow.car_scale, id: "null"}]
				console.log(rectangle0.carX)
				console.log(rectangle0.carY)
				frontend.onCreateCarParkingSlot(parkingSlot)
			}

			contentItem: Text {
				text: button1.text
				font: button1.font
				opacity: enabled ? 1.0 : 0.3
				color: button1.down ? "#17a81a" : "#21be2b"
				horizontalAlignment: Text.AlignHCenter
				verticalAlignment: Text.AlignVCenter
				elide: Text.ElideRight
			}

			background: Rectangle {
				implicitWidth: 120*mainWindow.car_scale
				implicitHeight: 50*mainWindow.car_scale
				opacity: enabled ? 1 : 0.3
				border.color: button1.down ? "#17a81a" : "#21be2b"
				border.width: 1
				radius: 2
			}
		}
		Button {
			id: button2
			text: qsTr("Done Parking")
			y: (parent.height - 110*mainWindow.car_scale )
			// enabled: true
			font.pointSize: 10*mainWindow.car_scale
			onClicked: frontend.doneCarParking()

			contentItem: Text {
				text: button2.text
				font: button2.font
				opacity: enabled ? 1.0 : 0.3
				color: button2.down ? "#17a81a" : "#21be2b"
				horizontalAlignment: Text.AlignHCenter
				verticalAlignment: Text.AlignVCenter
				elide: Text.ElideRight
			}

			background: Rectangle {
				implicitWidth: 120*mainWindow.car_scale
				implicitHeight: 50*mainWindow.car_scale
				opacity: enabled ? 1 : 0.3
				border.color: button2.down ? "#17a81a" : "#21be2b"
				border.width: 1
				radius: 2
			}
		}
	Timer{
		id:tmgauge
		interval: 20
		repeat: true
		running: true
		onTriggered: {
			brakeGauge.value = backend.get_brakePressure()
			speedGauge.value = backend.get_engineSpeed()
			if (rectangle.isTakeSteeringValue == true)
			customSlider.value = backend.get_steeringAngle()
		}
	}
	//
	
	
	Connections{
		id: frontend
		target: backend
		// function onTriggerTireBlowStatusEvent()
		// {
		// 	animationBlowOut.running = true;
		// 	backgroundColor.color = "#ffcc00"
		// 	carStatus.color = "#000000"
		// 	carStatus.text = "Tire Blow-Out"
        // }
		function onCreateCarParkingSlot(parkingSlots)
		{
			const PARKING_SLOT_WIDTH = 150*mainWindow.car_scale;
			const PARKING_SLOT_HEIGHT = 250*mainWindow.car_scale;
			var parkingSlotComponent = Qt.createComponent("../controls/ParkingSlot.qml");
			var nonParkingSlotComponent = Qt.createComponent("../controls/NonParkingSlot.qml");
			var label = Qt.createComponent("../controls/Announcement.qml");

			animationLine.running = false;
			initLocationCarAnimation.running = true;
			
			car.opacity = 1;

            if (parkingSlotComponent.status === Component.Ready) {
				for (var i = 0; i < parkingSlots.length; ++i) {
					const UIx = parkingSlots[i].x - PARKING_SLOT_HEIGHT / 2;
					const UIy = parkingSlots[i].y - PARKING_SLOT_WIDTH / 2;
					parkingSlots[i].id = parkingSlotComponent.createObject(	container, 
																			{slotNumber: i, 
																			x: UIx, 
																			y: UIy - 295*mainWindow.car_scale, 
																			rotation: (parkingSlots[i].x > rectangle0.carX ? 180 : 0)});
					// nonParkingSlotComponent.createObject(container, {id:"nonParkingSlotR" + toString(i), x: UIx, y: UIy + 180});
					// nonParkingSlotComponent.createObject(container, {id:"nonParkingSlotL" + toString(i), x: UIx, y: UIy - 180});
				}	
				if (label.status === Component.Ready) {
					var labelAnnouncement = label.createObject(container, {x:150, y:0});
				}
        	}
		}
		function doneCarParking()
		{
			const PARKING_SLOT_WIDTH = 150*mainWindow.car_scale;
			const PARKING_SLOT_HEIGHT = 250*mainWindow.car_scale;
			var doneParkingSlotComponent = Qt.createComponent("../controls/DoneParkingSlot.qml");
			if (doneParkingSlotComponent.status === Component.Ready) {
				doneParkingSlotComponent.createObject(container, {	x: rectangle0.chosenSlotX,
																	y: rectangle0.chosenSlotY, 
																	rotation: (rectangle0.chosenSlotX > rectangle0.carX ? 180 : 0)	});
				// car.opacity = 0;
				rectangle0.carRotation = rectangle0.chosenSlotX > rectangle0.carX ? -90 : 90;
				car.rotation = rectangle0.carRotation
				backend.setCarRotation(rectangle0.carRotation)

				rectangle0.carX = rectangle0.chosenSlotX + PARKING_SLOT_HEIGHT/2
				rectangle0.carY = rectangle0.chosenSlotY + PARKING_SLOT_WIDTH/2
				rectangle0.labelAnnouncement = "Done parking"
			}
		}
		function onMoveCarPosition(speed, rotation)
		{
			
           	rectangle0.carSpeed = speed;
			rectangle0.carRotation = rotation;
			if (rectangle0.carRotation < -360) {
				rectangle0.carRotation += 720;
			} else if (rectangle0.carRotation >= 360) {
				rectangle0.carRotation -= 720;
			}
			// speedGauge.value = speed * 5 > 0 ? speed * 5 : -speed * 5;
			// customSlider.value = rectangle0.carRotation/5;
        }

		// function onTriggerToNormalStatusEvent()
		// {
		// 	animationBlowOut.running = false;
		// 	animationToNormal.running = true;
        // }
		//function onValueGauge(value){
        //   slider.value = value/10
        //   progressIndicator.value = value
        //   customSlider.value = value
        //}
	}
}

