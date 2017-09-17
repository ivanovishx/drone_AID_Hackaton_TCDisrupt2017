from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import os
import six.moves.urllib as urllib
app = Flask(__name__)
ask = Ask(app, "/drone_help")

def do_something():
	pass

@app.route('/')
def homepage():
	return "//////\\\\\\"

@ask.intent("wabalabadubdub")
def howdoifeel():
	msg = "wabalabadubdub"
	return statement(msg)

@ask.intent("startmisssion")
def mission():
	msg = "Starting mission"
	return statement(msg)
@ask.launch
def start_skill():
	welcome_message = "Would you like to turn the drone on?"
	return question(welcome_message)
@ask.intent("YesIntent")
def turnON():
	opener = urllib.request.URLopener()
	#opener.retrieve("http://dron-aid.com/app/drone.php?control=1&lat=37.7761859&long=-122.3887722")
	opener.retrieve("http://www.google.com")
	var = "Turning it on, would you like to start the reconnaissance mission now?"
	return question(var)
@ask.intent("NoIntent")
def donothing():
	var = "Ok, I will wait to do it"
	return statement(var)
@ask.intent("PictureIntent")
def take_pict():
	var = "Taking a picture, I will send it to Droneaid app"
	os.system("python ob_single.py 1.jpg")
	return statement(var)

@ask.intent("MoveLeft")
def moveLeft():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=2&lat=37.7761859&long=-122.3887722")
	var = "Moving left"
	return question(var)

@ask.intent("MoveRight")
def moveRight():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=3&lat=37.7761859&long=-122.3887722")
	var = "Moving right"
	return question(var)
	
@ask.intent("MoveUp")
def moveUp():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=4&lat=37.7761859&long=-122.3887722")
	var = "Moving"
	return question(var)

@ask.intent("MoveDown")
def moveDwn():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=5&lat=37.7761859&long=-122.3887722")
	var = "Moving down"
	return question(var)
	
@ask.intent("MoveFwd")
def moveFwd():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=6&lat=37.7761859&long=-122.3887722")
	var = "Moving forward"
	return question(var)

@ask.intent("MoveBkd")
def moveBkg():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=7&lat=37.7761859&long=-122.3887722")
	var = "Moving backwards"
	return question(var)

@ask.intent("Roll left")
def rollLft():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=8&lat=37.7761859&long=-122.3887722")
	var = "Rolling left"
	return question(var)
@ask.intent("sendsms")
def sendsms():
	var = "I will send a message to the number 4157927562"
	j = json.loads('{"content": "TEST","deliveryReport": "true","recipient": "4157927562","senderAddress": "2083399485",  "transactionID": "12345"}')
	r = requests.post('https://thingspace.verizon.com/api/messaging/v1/sms' ,j)
	return (var)

	

@ask.intent("Roll right")
def rollR():
	opener = urllib.request.URLopener()
	opener.retrieve("http://dron-aid.com/app/drone.php?control=9&lat=37.7761859&long=-122.3887722")
	var = "Rolling right"
	return question(var)
if __name__ == '__main__':
	app.run(debug=True)
