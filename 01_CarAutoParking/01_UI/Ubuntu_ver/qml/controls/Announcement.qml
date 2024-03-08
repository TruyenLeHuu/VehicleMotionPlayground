import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle
{
    width: 450*mainWindow.scale
    height: 50*mainWindow.scale
    color: "black"
    Label {
        anchors.centerIn: parent
        font.pointSize: 20*mainWindow.scale
        color: "#62ff00"
        text: rectangle0.labelAnnouncement
    }
}

