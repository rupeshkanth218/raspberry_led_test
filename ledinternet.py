
import RPi.GPIO as GPIO
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url="https://rupeshkanth218.pythonanywhere.com/"
def get_data():
	data=urlopen(url)
	page=data.read()
	data.close()
	page=soup(page,"html.parser")

	code=page.find("h1")
	return code.text

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT,initial=GPIO.LOW)
prev_txt=""
try:
	while True:
		try:
			txt=get_data().lower()
			if txt!=prev_txt:
				if txt=='on':
					GPIO.output(14,GPIO.HIGH)
				else:
					GPIO.output(14,GPIO.LOW)
			
			prev_txt=txt
		except Exception as e:
			print(e)
			GPIO.output(14,GPIO.LOW)
		
		
except :
	GPIO.output(14,GPIO.LOW)
	
	
	
