from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BOARD) # use board pin numbers
pin_sensor = 7
GPIO.setup(pin_sensor, GPIO.IN) 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)


class SensorThreaded(threading.Thread):
    def __init__(self,):
        self._stop = threading.Event()
        self.count_clap = 0
        self.value_sensor = 0
        threading.Thread.__init__(self)
    
    def stop(self):
        self._stop.set()
    
    def stopped(self):
        return self._stop.isSet()

    @app.route('/turnAuto', methods = ['GET','POST'])
    def run(self):
        while True:
            if self.stopped():
                break
            else:
                self.value_sensor = GPIO.input(pin_sensor)
                if self.value_sensor == GPIO.HIGH:
                    timer = int(round(time.time() * 1000))
                    self.count_clap += 1
                    time.sleep(500)
                    while(int(round(time.time() * 1000)) - timer < 2000): #Read value sensor in next 2s
                        self.value_sensor = GPIO.input(pin_sensor)
                        print(self.value_sensor)
                        print('--')
                        if self.value_sensor == GPIO.HIGH:
                            self.count_clap += 1
                            time.sleep(100)

                print(self.count_clap)

                if self.count_clap == 1:
                    GPIO.output(17, GPIO.HIGH)
                    GPIO.output(18, GPIO.HIGH)
                    return render_template('index.html',rs = True)

                elif self.count_clap == 2:
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(18, GPIO.LOW)
                    return render_template('index.html',rs = False)
            
@app.route('/')
def main():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    return render_template('index.html', rs = False)

@app.route('/turnON', methods = ['POST', 'GET'])
def turnON():
    data = request.get_json()
    checkyel = data['checkyel']
    checkblue = data['checkyel']
    checksensor = data['checksensor']
    #print(data)
    
    if checkyel == True and checkblue is False:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        
    elif checkblue == True and checkyel is False:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
      
    elif checkblue == True and checkyel == True:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
      
    else:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    if checksensor == True:
        task.start()
    else:
        task.stop()
        task.join()

    return data

#Start our threaded task and flask
task = SensorThreaded()
app.run(debug=True)


