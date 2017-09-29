import datetime
import time
import os

while True:
	os.system("cls")
	dt = datetime.datetime.now()
	print ("{}:{}:{}:{}".format(dt.hour,dt.minute,dt.second,dt.microsecond))
	time.sleep(0.5) #Tiempo en segundos mientras se pausa el programa.