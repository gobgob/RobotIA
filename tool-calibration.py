#!/usr/bin/python

from math import *
from class_robot import *
from class_table import *
from strategy_calibration import *
from time import sleep

table = Table();
gobywan = Robot(table)

strategyCalibration=StrategyCalibration(table,gobywan)


strategyCalibration.CalibrateRotation(20)