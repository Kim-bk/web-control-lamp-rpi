from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# import RPi.GPIO as GPIO
import threading
import time

# GPIO.setmode(GPIO.BOARD) # use board pin numbers
# pin_sensor = 7
# GPIO.setup(pin_sensor, GPIO.IN) 
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(18, GPIO.OUT)



# class SensorThreaded(threading.Thread):
#     def __init__(self,):
#         self.count_clap = 0
#         self.value_sensor = 0
#         threading.Thread.__init__(self)
        
#     def run(self):
#         while True:
#             self.value_sensor = GPIO.input(pin_sensor)
#             if self.value_sensor == GPIO.HIGH:
#                 timer = int(round(time.time() * 1000))
#                 self.count_clap += 1
#                 time.sleep(500)
#                 while(int(round(time.time() * 1000)) - timer < 2000): #Read value sensor in next 2s
#                     self.value_sensor = GPIO.input(pin_sensor)
#                     print(self.value_sensor)
#                     print('--')
#                     if self.value_sensor == GPIO.HIGH:
#                         self.count_clap += 1
#                         time.sleep(100)

#             print(self.count_clap)

#             if self.count_clap == 1:
#                 GPIO.output(17, GPIO.HIGH)
#                 GPIO.output(18, GPIO.HIGH)
#                 return render_template('turnOnBoth.html')

#             elif self.count_clap == 2:
#                 GPIO.output(17, GPIO.LOW)
#                 GPIO.output(18, GPIO.LOW)
#                 return render_template('index.html')
            

app = Flask(__name__)

@app.route('/')
def main():
    # GPIO.output(17, GPIO.LOW)
    # GPIO.output(18, GPIO.LOW)
    return render_template('index.html')

@app.route('/turnON', methods = ['POST', 'GET'])
def turnON():
    data = request.get_json()
    print(data)
    return data
    # print(checksensor)
   
    # if checkyel == 'on' and checkblue is None:
    #     GPIO.output(17, GPIO.HIGH)
    #     GPIO.output(18, GPIO.LOW)
    #     return render_template('turnOnYel.html')
    # if checkblue == 'on' and checkyel is None:
    #     GPIO.output(17, GPIO.LOW)
    #     GPIO.output(18, GPIO.HIGH)
    #     return render_template('turnOnBlue.html')
    # if checkblue == 'on' and checkyel == 'on':
    #     GPIO.output(17, GPIO.HIGH)
    #     GPIO.output(18, GPIO.HIGH)
    #     return render_template('turnOnBoth.html')
    # else:
    #     GPIO.output(17, GPIO.LOW)
    #     GPIO.output(18, GPIO.LOW)
    #     return render_template('index.html')

#Start our threaded task and flask
# task = SensorThreaded()
# task.start()
app.run(debug=True)


