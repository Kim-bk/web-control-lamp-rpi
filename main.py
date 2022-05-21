from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


app = Flask(__name__)

@app.route('/')
def main():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    return render_template('index.html')

@app.route('/turnON', methods = ['POST', 'GET'])
def turnON():
    data = request.get_json()
    led_yellow = data['led_yellow']
    led_blue = data['led_blue']
    #print(data)

    if led_yellow == True and led_blue == False:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        
    if led_yellow == False and led_blue == True:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
      
    if led_yellow == True and led_blue == True:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
      
    if led_yellow == False and led_blue == False:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

app.run(debug=True)


