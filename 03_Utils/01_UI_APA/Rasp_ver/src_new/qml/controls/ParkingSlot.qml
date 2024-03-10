import QtQuick 2.11

Rectangle {
    width: 250*mainWindow.car_scale
    height: 150*mainWindow.car_scale

    color: "green"

    radius: width / 40
    rotation: 180
    
    z: 3
    property int slotNumber: 0

    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        hoverEnabled: true
        onClicked: {
            if(mouse.button === Qt.LeftButton) {
                imageAnimation.running = true
                rectangle0.labelAnnouncement = "Please wait for parking slot " + slotNumber + "..."
                rectangle0.isChosen = 1
                rectangle0.chosenSlotX = parent.x
                rectangle0.chosenSlotY = parent.y
                backend.chooseSlot(slotNumber)
            }
        }
        onEntered: {
            parent.color = "orange"
            carImage.opacity = 0.6 
            if (!rectangle0.isChosen)
                rectangle0.labelAnnouncement = "You are choosing slot number " + slotNumber 
        }
        onExited: {
            parent.color = "green"
            carImage.opacity = 0
            if (!rectangle0.isChosen)
                rectangle0.labelAnnouncement = "Please choose your parking slot!"
        }
    }
    Image {
        id: parkingImage
        scale: 0.25*mainWindow.car_scale
        rotation: 270
        opacity:0.5
        source: "../../images/png_images/parking_ground.png"
        anchors.centerIn: parent
    }
    Image {
        id: carImage
        width: 446 * 0.3 *mainWindow.car_scale
        height: 850 * 0.3 *mainWindow.car_scale
        z: 1
        opacity:0
        source: "../../images/png_images/car-top-view.png"
        rotation: 90
        anchors.centerIn: parent
        SequentialAnimation {
                id: imageAnimation
				loops: Animation.Infinite
				running: false
				NumberAnimation { target: carImage; property: "opacity"; from:0.3; to: 0.9; duration: 800 } // Hiển thị trong 1 giây
				NumberAnimation { target: carImage; property: "opacity"; from:0.9; to: 0.3; duration: 800 } 
	
			}
    }
}
