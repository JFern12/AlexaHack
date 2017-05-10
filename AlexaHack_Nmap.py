#!/usr/bin/python
import sys
from AlexaHack_Interface import Interface
import string
#Assumptions:
#IPv4
#No domain lookup for IP address

interface= Interface()#an interface for I/O
def validate(anOption, aValue):
  if anOption=='IP': #validate the IP instance
    parts=string.split(aValue, '/', 1)
    ipNum=string.split(parts[0], '.')
    print parts
    print ipNum
    if len(ipNum[0]) > 4:
      print '1'
      return False #more than 4 octects
    for i in ipNum:
      try:
        temp=int(i)
        if temp>255 or temp<0:
          print '2'
          return False
      except:
        print '3'
        return False
    if len(parts)>1:
      try:
        temp=int(i)
        if temp>32 or temp<8:
          print '4'
          return False
      except:
        print '5'
        return False
    return True	
  else:
    print '6'
    raise NameError(anOption+" is an invalid option")
#nmap
scanOption= '-sS'
ipAddress='127.0.0.1'
def getNextAction(options): #takes a list of options, interacts with the interface until the 
  while True:
    uInput=interface.getInput("What would you like to do next")
    if uInput in options:
      return uInput
    interface.display("Invalid option.")

def setIP(aVal):
  ipAddress=aVal

def hacking():
  getInput=True
  prompt="Provide an IP range"
  while getInput:
    IP=interface.getInput(prompt)
    getInput=validate('IP', interface.getInput(prompt))
  setIP(ipAddress)
  action=getNextAction()

interface.getValidInput("Give me an input", lambda x: validate('IP',x))

