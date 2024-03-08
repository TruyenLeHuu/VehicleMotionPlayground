import QtQuick 2.11
import QtQuick.Controls 2.0

Rectangle
{
    width: 450*mainWindow.scale
    height: 50*mainWindow.scale
    color: "#00000000"
    Label {
        anchors.centerIn: parent
        font.pointSize: 18*mainWindow.scale
        color: "#62ff00"
        text: rectangle0.labelAnnouncement
        // Rectangle
        // {
        //     anchors.fill: parent
        //     color: "#ffffff"
        // }
    }
}

