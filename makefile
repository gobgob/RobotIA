
all :
	python3 ../codeGenerator/codeGenerator.py proxi_serial.py proxi_generated.py
	python3 ../codeGenerator/codeGenerator.py proxi_serial.py ../asserv_uc/proxi2c_generated.ino
