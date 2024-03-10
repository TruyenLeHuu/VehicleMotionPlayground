import "../controls"
import QtQuick.Window 2.11
import QtQuick.Controls 2.2
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtQml 2.11

import QtQuick 2.11
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.11
import QtQuick.Shapes 1.11
import QtGraphicalEffects 1.0

Item {
    Rectangle {
        id: rectangle
        color: "#2c313c"
        anchors.fill: parent

        Rectangle {
            id: rectangleVisible
            color: "#1d2128"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 40
            anchors.rightMargin: 50
            anchors.leftMargin: 50
            anchors.topMargin: 10

            Label {
                id: labelTextName
                y: 8
                height: 25
                color: "#0ed145"
                text: qsTr("Team members")
                anchors.left: parent.left
                anchors.right: parent.right
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.leftMargin: 10
                anchors.rightMargin: 10

                font.pointSize: 25
            }

            // Label {
            //     id: labelDate
            //     y: 40
            //     height: 25
            //     color: "#55aaff"
            //     text: qsTr("Date")
            //     anchors.left: parent.left
            //     anchors.right: parent.right
            //     horizontalAlignment: Text.AlignHCenter
            //     verticalAlignment: Text.AlignVCenter
            //     anchors.rightMargin: 10
            //     anchors.leftMargin: 10
            //     font.pointSize: 12
            // }

            ScrollView {
                id: scrollView
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                clip: true
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                anchors.bottomMargin: 10
                anchors.topMargin: 10

                /*
                Text {
					id: textHome
					color: "#a9b2c8"
					text:"Bienvenido"
					//text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">GNU GENERAL PUBLIC LICENSE</span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version 3, 29 June 2007</p>\n<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (c) 2020 <span style=\" font-weight:600;\">Wanderson M. Pimenta</span></p>\n<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#55aaff;\">Attention</span>: this project was created with the Open Souce tools from Qt Company,</p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this project can be used for studies or personal non-commercial projects. </p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">If you are going to use it for </span><span style=\" font-weight:600; color:#55aaff;\">commercial use</span><span style=\" font-weight:600;\">, you need to purchase a license at &quot;https://www.qt.io&quot;.</span></p></body></html>"
					anchors.fill: parent
					font.pixelSize: 12
					textFormat: Text.RichText
				}
				*/
                /* Anh Phuong */
                Rectangle {
					color: "#00000000"
					anchors.fill: parent
                    Rectangle {
                        width: 1400*0.2*0.8
                        height: 950*0.295*0.8
                        anchors.top : parent.top
                        anchors.topMargin: 50
                        anchors.left : parent.left
                        anchors.leftMargin: 150
                        visible: true
                        color: "#00000000"
                        Rectangle{
                            id: mask1
                            anchors.fill: parent
                            radius: width / 2
                            color: "#282A36"
                            border.width: 5
                            border.color: "#44475A"
                        }
                        Item {
                            anchors.fill: mask1
                            anchors.margins: 5
                            layer.enabled: true
                            layer.effect: OpacityMask {
                                maskSource: mask1
                            }
                            // Image {
                            //     id: icon2
                            //     scale: 1
                            //     anchors.fill: parent
                            //     source: "../../images/APhuong.jpg"
                            //     opacity: 1
                            // }
                        }
                        Label {
                            y: 240
                            height: 25
                            color: "#ffffff"
                            text: qsTr("Dao Van Sang")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                        Label {
                            y: 280
                            height: 25
                            color: "#ffffff"
                            text: qsTr("(MS/EAS11-CC)")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                    }
				}
                /* Anh Phong */
                Rectangle {
					color: "#00000000"
					anchors.fill: parent
                    Rectangle {
                        width: 1400*0.2*0.8
                        height: 950*0.295*0.8
                        anchors.top : parent.top
                        anchors.topMargin: 50
                        anchors.left : parent.left
                        anchors.leftMargin: 500
                        visible: true
                        color: "#00000000"
                        Rectangle{
                            id: mask2
                            anchors.fill: parent
                            radius: width / 2
                            color: "#282A36"
                            border.width: 5
                            border.color: "#44475A"
                        }
                        Item {
                            anchors.fill: mask2
                            anchors.margins: 5
                            layer.enabled: true
                            layer.effect: OpacityMask {
                                maskSource: mask2
                            }
                            // Image {
                            //     id: icon3
                            //     scale: 1
                            //     anchors.fill: parent
                            //     source: "../../images/APhong.jpg"
                            //     opacity: 1
                            // }
                        }
                        Label {
                            y: 240
                            height: 25
                            color: "#ffffff"
                            text: qsTr("Nguyen Vinh Loi")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                        Label {
                            y: 280
                            height: 25
                            color: "#ffffff"
                            text: qsTr("(MS/EAS11-CC)")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                    }
				}
                /* Anh Long */
                Rectangle {
					color: "#00000000"
					anchors.fill: parent
                    Rectangle {
                        width: 1400*0.2*0.8
                        height: 950*0.295*0.8
                        anchors.top : parent.top
                        anchors.topMargin: 50
                        anchors.left : parent.left
                        anchors.leftMargin: 850
                        visible: true
                        color: "#00000000"
                        Rectangle{
                            id: mask3
                            anchors.fill: parent
                            radius: width / 2
                            color: "#282A36"
                            border.width: 5
                            border.color: "#44475A"
                        }
                        Item {
                            anchors.fill: mask3
                            anchors.margins: 5
                            layer.enabled: true
                            layer.effect: OpacityMask {
                                maskSource: mask3
                            }
                            // Image {
                            //     id: icon4
                            //     scale: 1
                            //     anchors.fill: parent
                            //     source: "../../images/ALong.jpg"
                            //     opacity: 1
                            // }
                        }
                        Label {
                            y: 240
                            height: 25
                            color: "#ffffff"
                            text: qsTr("Tran Viet Phuong")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                        Label {
                            y: 280
                            height: 25
                            color: "#ffffff"
                            text: qsTr("(MS/EAS62-CC)")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                    }
				}
                /* Anh Trung */
				Rectangle {
					color: "#00000000"
					anchors.fill: parent
                    Rectangle {
                        width: 1400*0.2*0.8
                        height: 950*0.295*0.8
                        anchors.top : parent.top
                        anchors.topMargin: 50
                        anchors.left : parent.left
                        anchors.leftMargin: 1200
                        visible: true
                        color: "#00000000"
                        Rectangle{
                            id: mask4
                            anchors.fill: parent
                            radius: width / 2
                            color: "#282A36"
                            border.width: 5
                            border.color: "#44475A"
                        }
                        Item {
                            anchors.fill: mask4
                            anchors.margins: 5
                            layer.enabled: true
                            layer.effect: OpacityMask {
                                maskSource: mask4
                            }
                            // Image {
                            //     id: icon4
                            //     scale: 1
                            //     anchors.fill: parent
                            //     source: "../../images/Truyen.jpg"
                            //     opacity: 1
                            // }
                        }
                        Label {
                            y: 240
                            height: 25
                            color: "#ffffff"
                            text: qsTr("Tran Cong Trung")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                        Label {
                            y: 280
                            height: 25
                            color: "#ffffff"
                            text: qsTr("(MS/EAS11-CC)")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                    }
				}
                /* A Nghiem */
				Rectangle {
					color: "#00000000"
					anchors.fill: parent
                    Rectangle {
                        width: 1400*0.2*0.8
                        height: 950*0.295*0.8
                        anchors.top : parent.top
                        anchors.topMargin: 450
                        anchors.left : parent.left
                        anchors.leftMargin: 150
                        visible: true
                        color: "#00000000"
                        Rectangle{
                            id: mask5
                            anchors.fill: parent
                            radius: width / 2
                            color: "#282A36"
                            border.width: 5
                            border.color: "#44475A"
                        }
                        Item {
                            anchors.fill: mask5
                            anchors.margins: 5
                            layer.enabled: true
                            layer.effect: OpacityMask {
                                maskSource: mask5
                            }
                            // Image {
                            //     id: icon5
                            //     scale: 1
                            //     anchors.fill: parent
                            //     source: "../../images/Truyen.jpg"
                            //     opacity: 1
                            // }
                        }
                        Label {
                            y: 240
                            height: 25
                            color: "#ffffff"
                            text: qsTr("Nguyen Huy Nghiem")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                        Label {
                            y: 280
                            height: 25
                            color: "#ffffff"
                            text: qsTr("(MS/EAS11-CC)")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                    }
				}
                /* Truyen */
				Rectangle {
					color: "#00000000"
					anchors.fill: parent
                    Rectangle {
                        width: 1400*0.2*0.8
                        height: 950*0.295*0.8
                        anchors.top : parent.top
                        anchors.topMargin: 450
                        anchors.left : parent.left
                        anchors.leftMargin: 500
                        visible: true
                        color: "#00000000"
                        Rectangle{
                            id: mask6
                            anchors.fill: parent
                            radius: width / 2
                            color: "#282A36"
                            border.width: 5
                            border.color: "#44475A"
                        }
                        Item {
                            anchors.fill: mask6
                            anchors.margins: 5
                            layer.enabled: true
                            layer.effect: OpacityMask {
                                maskSource: mask6
                            }
                            // Image {
                            //     id: icon6
                            //     scale: 1
                            //     anchors.fill: parent
                            //     source: "../../images/Truyen.jpg"
                            //     opacity: 1
                            // }
                        }
                        Label {
                            y: 240
                            height: 25
                            color: "#ffffff"
                            text: qsTr("Le Huu Truyen")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                        Label {
                            y: 280
                            height: 25
                            color: "#ffffff"
                            text: qsTr("(MS/EAS7-CC)")
                            anchors.left: parent.left
                            anchors.right: parent.right
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10

                            font.pointSize: 18
                        }
                    }
				}
            }
        }
    }
    Connections{
        target: backend

        function onSetName(name){
            labelTextName.text = name
        }

        function onPrintTime(time){
            labelDate.text = time
        }

        function onIsVisible(isVisible){
            rectangleVisible.visible = isVisible
        }
    }

}

