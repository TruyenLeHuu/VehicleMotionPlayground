
(cl:in-package :asdf)

(defsystem "carla_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CarlaActorInfo" :depends-on ("_package_CarlaActorInfo"))
    (:file "_package_CarlaActorInfo" :depends-on ("_package"))
    (:file "CarlaActorList" :depends-on ("_package_CarlaActorList"))
    (:file "_package_CarlaActorList" :depends-on ("_package"))
    (:file "CarlaBoundingBox" :depends-on ("_package_CarlaBoundingBox"))
    (:file "_package_CarlaBoundingBox" :depends-on ("_package"))
    (:file "CarlaCollisionEvent" :depends-on ("_package_CarlaCollisionEvent"))
    (:file "_package_CarlaCollisionEvent" :depends-on ("_package"))
    (:file "CarlaControl" :depends-on ("_package_CarlaControl"))
    (:file "_package_CarlaControl" :depends-on ("_package"))
    (:file "CarlaEgoVehicleControl" :depends-on ("_package_CarlaEgoVehicleControl"))
    (:file "_package_CarlaEgoVehicleControl" :depends-on ("_package"))
    (:file "CarlaEgoVehicleInfo" :depends-on ("_package_CarlaEgoVehicleInfo"))
    (:file "_package_CarlaEgoVehicleInfo" :depends-on ("_package"))
    (:file "CarlaEgoVehicleInfoWheel" :depends-on ("_package_CarlaEgoVehicleInfoWheel"))
    (:file "_package_CarlaEgoVehicleInfoWheel" :depends-on ("_package"))
    (:file "CarlaEgoVehicleRotation" :depends-on ("_package_CarlaEgoVehicleRotation"))
    (:file "_package_CarlaEgoVehicleRotation" :depends-on ("_package"))
    (:file "CarlaEgoVehicleStatus" :depends-on ("_package_CarlaEgoVehicleStatus"))
    (:file "_package_CarlaEgoVehicleStatus" :depends-on ("_package"))
    (:file "CarlaLaneInvasionEvent" :depends-on ("_package_CarlaLaneInvasionEvent"))
    (:file "_package_CarlaLaneInvasionEvent" :depends-on ("_package"))
    (:file "CarlaStatus" :depends-on ("_package_CarlaStatus"))
    (:file "_package_CarlaStatus" :depends-on ("_package"))
    (:file "CarlaTrafficLightInfo" :depends-on ("_package_CarlaTrafficLightInfo"))
    (:file "_package_CarlaTrafficLightInfo" :depends-on ("_package"))
    (:file "CarlaTrafficLightInfoList" :depends-on ("_package_CarlaTrafficLightInfoList"))
    (:file "_package_CarlaTrafficLightInfoList" :depends-on ("_package"))
    (:file "CarlaTrafficLightStatus" :depends-on ("_package_CarlaTrafficLightStatus"))
    (:file "_package_CarlaTrafficLightStatus" :depends-on ("_package"))
    (:file "CarlaTrafficLightStatusList" :depends-on ("_package_CarlaTrafficLightStatusList"))
    (:file "_package_CarlaTrafficLightStatusList" :depends-on ("_package"))
    (:file "CarlaWalkerControl" :depends-on ("_package_CarlaWalkerControl"))
    (:file "_package_CarlaWalkerControl" :depends-on ("_package"))
    (:file "CarlaWeatherParameters" :depends-on ("_package_CarlaWeatherParameters"))
    (:file "_package_CarlaWeatherParameters" :depends-on ("_package"))
    (:file "CarlaWorldInfo" :depends-on ("_package_CarlaWorldInfo"))
    (:file "_package_CarlaWorldInfo" :depends-on ("_package"))
  ))