from vehicle_motion_api import VehicleMotionAPI
import time
import rospy
import speech_recognition as sr


# Initialize the speech recognizer 
r = sr.Recognizer()

 
def process_speech(): 
    with sr.Microphone() as source: 
        print("Listening...") 
        audio = r.listen(source) 
 
        try: 
            # Use Google Speech Recognition to convert audio to text 
            command = r.recognize_google(audio) 
            print(f"You said: {command}") 
            return command.lower() 
        except sr.UnknownValueError: 
            print("Sorry, I could not understand your command.") 
            return None 
        except sr.RequestError as e: 
            print(f"Could not request results from Google Speech Recognition service; {e}") 
            return None 
 
def control_variables(command, vm_api): 
    brake = 0 
    engine = 0 
 
    if "run" in command: 
        brake = 0 
        engine = 1 
        vm_api.vehicle_control(throttle = 0.4, brake = 0)
    elif "stop" in command: 
        brake = 1 
        engine = 0 
        vm_api.vehicle_control(throttle = 0, brake = 1)
 
    return brake, engine 
 


def main():
    """
    Main function
    """
    vm_api = VehicleMotionAPI()
    try:
        while (not vm_api.exit_flag):
            """ Begin application code """
            command = process_speech() 
            if command: 
                brake, engine = control_variables(command, vm_api) 
                print(f"Brake: {brake}, Engine: {engine}")
            time.sleep(0.01)
            """ End application code """
    except KeyboardInterrupt:
        print("Shutting down")
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    