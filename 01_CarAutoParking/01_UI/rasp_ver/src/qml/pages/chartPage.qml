import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0


//import QtQuick 2.0
import QtCharts 2.3
import "../controls"


Item {

	Text {
		id: title
		text: qsTr("Brake Pressure Measurement Chart")
		anchors.top:  parent.top
		anchors.horizontalCenter: parent.horizontalCenter
		anchors.topMargin: 5
		font.pointSize :18
		color: "#a0a0a0"
	}
	//########## INI CHART VIEW ##############################
	
	ChartView{
        id:cv
        anchors{
            top:title.bottom
            topMargin:10
            left:parent.left
            right:parent.right
            bottom:parent.bottom
            bottomMargin:10
            leftMargin:10
            rightMargin:10
        }
        antialiasing: true
        theme: ChartView.ChartThemeDark

        property int  timcnt: 0
        property double  valueCH1: 0

        //property double  valueTM1: 0        
        property double  periodGRAPH: 30 // Seconds
		property double  startTIME: 0
		property double  intervalTM: 200 // miliseconds

        ValueAxis{
            id:yAxis
            min: 0
            max: 110
            tickCount: 1
            labelFormat: "%d"
        }

        LineSeries {
			name: "BRAKE PRESSURE"
			id:lines1
			//axisX: xAxis
			axisY: yAxis
			width: 2
			color: "#1267D4"
			axisX: 	DateTimeAxis {
					id: eje
					//format: "yyyy MMM"
					format:"HH:mm:ss.z"
					//format:"mm:ss.z"
				}
		}

        ///
        Timer{
			id:tm
			interval: cv.intervalTM
			repeat: true
			running: true
			onTriggered: {
				cv.timcnt = cv.timcnt + 1
				cv.valueCH1 = backend.get_brakePressure()
				
				if (lines1.count>cv.periodGRAPH*1000/cv.intervalTM){
					lines1.remove(0)
					}
				
				lines1.append(cv.startTIME+cv.timcnt*cv.intervalTM ,cv.valueCH1)
				
				lines1.axisX.min = new Date(cv.startTIME-cv.periodGRAPH*1000 + cv.timcnt*cv.intervalTM)
				lines1.axisX.max = new Date(cv.startTIME + cv.timcnt*cv.intervalTM)
			}
		}

    }
    Component.onCompleted: {
		cv.startTIME = backend.get_tiempo()*1000
	}
    

	//########## END CHART VIEW ##############################
	
	Connections{
        target: backend
        
	}
}

