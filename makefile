
all :
	python3 ../codeGenerator2014/codeGenerator.py proxi_serial.py proxi_generated.py
	python3 ../codeGenerator2014/codeGenerator.py proxi_serial.py ../asserv_uc/proxi2c_generated.ino
