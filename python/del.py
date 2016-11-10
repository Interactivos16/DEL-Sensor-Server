#!/usr/bin/python

from sht21 import SHT21
from sht1x.Sht1x import Sht1x as SHT15

from os import path
from time import time

SHT15.sdaPin = 11
SHT15.sclPin = 7

outputFile = path.abspath(path.join(path.dirname(__file__), 'data.csv'))

sht15 = SHT15(SHT15.sdaPin, SHT15.sclPin, SHT15.GPIO_BOARD)
sht21 = SHT21(1)

writeHeader = not path.isfile(outputFile)

with open(outputFile,"a") as fo:
  if writeHeader:
    fo.write ("time,temp15,hum15,temp21,hum21\n")
  fo.write ("%s,%s,%s,%s,%s\n"%(time(),
                                sht21.read_temperature(),
                                sht21.read_humidity(),
                                sht21.read_temperature(),
                                sht21.read_humidity()))
  fo.close()
