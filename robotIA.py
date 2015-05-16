#!/usr/bin/python3

from class_robot import *
from class_table import *
from math import *
from proxi_serial import *
from strategy_start import *
from strategy_bis import *
from time import *
import threading

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy);

TEMPO = 108;
PULSATION = 60 / TEMPO;

strategyStart=StrategyStart(robot)
strategyBis=StrategyBis(robot)


robot.distanceHard()
robot.rotationHard()


robot.setBras(100,100)

print("Waiting for Jumper")

while not robot.isJumperIn():
	pass

robot.setBras(0,0)
print("The Jumper is in.")



while robot.isJumperIn():
	pass
print("The Jumper is out.")

start = time() * 1000;

# robot appuyé contre tasseau posé sur bordure salle de cinéma
robot.setTicks(0,0)

mesure = 0;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi/8, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(100, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(-pi/8, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(100, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi/8, autocolor=False, noWait=True);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(100, noWait=True);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(-pi/8, autocolor=False, noWait=True);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);






mesure = 1;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi/2, autocolor=False, noWait=True);
robot.setBras(20, 20);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
robot.setBras(40, 40);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3*pi/2, autocolor=False, noWait=True);
robot.setBras(60, 60);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(4*pi/2, autocolor=False, noWait=True);
robot.setBras(90, 90);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(70, 70);
temps = 4.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(80, 80);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(50, 50);
temps = 5.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(60, 60);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(30, 30);
temps = 6.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 40);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);




mesure = 2;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(-pi/8, autocolor=False, noWait=True);
robot.setBras(90, 0);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);
robot.setBras(0, 0);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi/8, autocolor=False, noWait=True);
robot.setBras(0, 90);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);
robot.setBras(0, 0);




mesure = 3;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 90);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);






mesure = 4;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveBackward(50, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(20, 20);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 40);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(60, 60);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 90);






mesure = 5;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3*pi/4, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(2*pi/4, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(1*pi/4, autocolor=False, noWait=True);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0*pi/4, autocolor=False, noWait=True);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);






mesure = 6;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveBackward(50, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(20, 20);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 40);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(60, 60);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 90);






mesure = 7;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi/2, autocolor=False, noWait=True);
robot.setBras(20, 20);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
robot.setBras(40, 40);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3*pi/2, autocolor=False, noWait=True);
robot.setBras(60, 60);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(4*pi/2, autocolor=False, noWait=True);
robot.setBras(90, 90);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(70, 70);
temps = 4.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(80, 80);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(50, 50);
temps = 5.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(60, 60);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(30, 30);
temps = 6.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 40);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);




mesure = 8;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
robot.rotateTo(-pi/16, autocolor=False, noWait=True);
temps = 0.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 0);
robot.rotateTo(-2*pi/16, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
robot.rotateTo(-3*pi/16, autocolor=False, noWait=True);
temps = 1.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 0);
robot.rotateTo(-4*pi/16, autocolor=False, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
robot.rotateTo(-5*pi/16, autocolor=False, noWait=True);
temps = 2.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 0);
robot.rotateTo(-6*pi/16, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);
robot.rotateTo(0, autocolor=False, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
robot.rotateTo(pi/16, autocolor=False, noWait=True);
temps = 4.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 40);
robot.rotateTo(2*pi/16, autocolor=False, noWait=True);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
robot.rotateTo(3*pi/16, autocolor=False, noWait=True);
temps = 5.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 40);
robot.rotateTo(4*pi/16, autocolor=False, noWait=True);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
robot.rotateTo(5*pi/16, autocolor=False, noWait=True);
temps = 6.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 40);
robot.rotateTo(6*pi/16, autocolor=False, noWait=True);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);
robot.rotateTo(0, autocolor=False, noWait=True);






mesure = 9;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
temps = 0.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
temps = 1.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
temps = 2.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
temps = 3.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 90);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);






mesure = 10;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3*pi/4, autocolor=False, noWait=True);
robot.setBras(20, 0);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(2*pi/4, autocolor=False, noWait=True);
robot.setBras(40, 0);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(1*pi/4, autocolor=False, noWait=True);
robot.setBras(60, 0);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);
robot.setBras(90, 0);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 90);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 0);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 90);






mesure = 11;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi/2, autocolor=False, noWait=True);
robot.setBras(20, 20);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
robot.setBras(40, 40);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3*pi/2, autocolor=False, noWait=True);
robot.setBras(60, 60);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(4*pi/2, autocolor=False, noWait=True);
robot.setBras(90, 90);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(70, 70);
temps = 4.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(80, 80);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(50, 50);
temps = 5.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(60, 60);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(30, 30);
temps = 6.5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 40);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(0, 0);






mesure = 12;
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3.99*pi/4, autocolor=False, noWait=True);






mesure = 13;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3*pi/4, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(2*pi/4, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(1*pi/4, autocolor=False, noWait=True);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0*pi/4, autocolor=False, noWait=True);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);






mesure = 14;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveForward(50, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(0, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.moveBackward(50, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(20, 20);
temps = 5;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 40);
temps = 6;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(60, 60);
temps = 7;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(90, 90);






mesure = 15;
temps = 0;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(pi/4, autocolor=False, noWait=True);
temps = 1;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(2*pi/4, autocolor=False, noWait=True);
temps = 2;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(3*pi/4, autocolor=False, noWait=True);
temps = 3;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.rotateTo(4*pi/4, autocolor=False, noWait=True);
temps = 4;
while time() * 1000 < start + (mesure * 8 + temps ) * PULSATION * 1000:
	pass
robot.setBras(40, 40);
