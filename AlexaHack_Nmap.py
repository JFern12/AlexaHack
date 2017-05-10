#!/usr/bin/python
import sys
from AlexaHack_Interface import Interface
import string
#Assumptions:
#IPv4
#No domain lookup for IP address

class nMap(object):
  options=[]
  def __init__(self, anInterface):
    self.interface=anInterface
    self.scanOption= '-sS'
    self.ipAddress='127.0.0.1'
    self.options={'scan':self, 'setIP':self, 'execute':self, 'exit':self}
    self.moreOptions=True
  def displayOptions(self):
    self.interface.display("Your Options are:")
    for i in self.options: self.interface.display(i)
  def validInput(self, x):
	return x=='y' or x=='n'
  def doOption(self,x): 
     if x=='exit': self.moreOptions=False  
     if x=='scan': 
      choice=self.interface.getValidInput('Would You Like to Scan', self.validInput)
      if choice=='y': self.interface.display('scanning')
      else: self.hacking()
     if x=='setIP': self.setIP()
  def getOptions(self):
    return {'scan': self}
  def validateIP(self, aValue):
    parts=string.split(aValue, '/', 1)
    ipNum=string.split(parts[0], '.')
    if len(ipNum[0]) > 4: return False #more than 4 octects
    for i in ipNum:
      try:
        temp=int(i)
        if temp>255 or temp<0: return False
      except: return False
    if len(parts)>1:
      try:
        temp=int(i)
        if temp>32 or temp<8:return False
      except: return False
    return True
  def validate(self, anOption, aValue):
    if anOption=='IP': return self.validateIP(aValue)	
    else: raise NameError(anOption+" is an invalid option")
  def setIP(self):
    self.ipAddress=self.interface.getValidInput("What IP", lambda x: self.validate('IP',x))
  def hacking(self):
    while self.moreOptions:
      curInput=self.interface.getInput("AlexaHack: ")
      if curInput in self.options: self.options[curInput].doOption(curInput)
      else: 
	self.interface.display("Invalid Option")
	self.displayOptions()

def getNextAction(options): #takes a list of options, interacts with the interface until the 
  while True:
    uInput=interface.getInput("What would you like to do next")
    if uInput in options:
      return uInput
    interface.display("Invalid option.")


 
class AlexHack(object):
  options={}
  basicInterface=Interface()
  moreOptions=True
  def __init__(self):
     self.options={"exit":self}
     aNmap=nMap(self.basicInterface)
     self.options.update(aNmap.getOptions())
  def displayOptions(self):
    self.basicInterface.display("Your Options are:")
    for i in self.options: self.basicInterface.display(i)
  def doOption(self,x): 
     if x=='exit': self.moreOptions=False
  def hacking(self):
    while self.moreOptions:
      curInput=self.basicInterface.getInput("AlexaHack: ")
      if curInput in self.options: self.options[curInput].doOption(curInput)
      else: 
	self.basicInterface.display("Invalid Option")
	self.displayOptions()
  

newAlexa=AlexHack()
newAlexa.hacking()

