
all :
	python3 ../codeGenerator2014/codeGenerator.py proxi2c.py proxi2c_generated.py
	python3 ../codeGenerator2014/codeGenerator.py proxi2c.py ../asserv_uc/proxi2c_generated.ino
