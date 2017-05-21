import string
import subprocess

class Interface(object):
    def __init__(self):#, aPrompt='H@CK'):
        #Utterances for events
        backup=['exit','cancel','stop','back','halt']
        execute=['execute','run','launch','scan']
        yes=['yes','sure', 'y','definitely']
        no=['no','nope','n']
        options=['help','option','options','h']
        display=['display','show','open','read']
        #Option Value
        target=['target','IP', 'targetIP', 'target IP', 'target IP address', 'target network', 'IP address']
        
        events=[backup,execute,yes,no,options+target]
        self.thesarus={}
        for event in events:
            for utterance in event[1:]:
                self.thesarus[utterance]=event[0]
        #self.scanOptions={'syn':'s', 'tcp':', 'udp':'u}

    @staticmethod
    def display(aString): 
        print aString

    @staticmethod
    def getInput(aPrompt):
       return raw_input(aPrompt)

    def getEvent(self, uInput):
        temp=uInput.lower()
        if temp in self.thesarus: return self.thesarus[temp]
        return uInput

    def getValidInput(self, validate, aPrompt="H@CK/>", remedialPrompt=None):
        count=0 #use to implement a display option
        fPrompt=aPrompt+": " 
        uInput=self.getEvent(self.getInput(fPrompt))
        while not validate(uInput):
            count+=1
            self.display("Invalid Input")
            if count>=5:
                self.Display(remedialPrompt)
                count=0
            uInput=self.getInput(fPrompt)
            if uInput in self.thesarus: temp=self.thesarus[uInput]
        return uInput
        
    @staticmethod
    def validateIP(aValue):
        parts=string.split(aValue, '/', 1) #break out cider based on 1st /
        ipNum=string.split(parts[0], '.') #break out octets
        #print parts
        #print ipNum
        octect=0
        if len(ipNum)!=4:
            #print('Incorrect # of octets')
            return False
        else:
            for i in range(4):
                try: octet=int(ipNum[i])
                except:
                    #print(str(ipNum[i])+"is invalid (octect "+str(i)+")")
                    return False
                if octect>255 or octect<0:
                    #print(str(ipNum[i])+" is invalid (octect "+str(i)+")")
                    return False
            if len(parts)>1:
                try: temp=int(parts[1])
                except:
                    #print 'Not a valid subnet'
                    return False
                if temp>32 or temp<8:
                    #print 'Out of subnet range ([8,32])'
                    return False                 
            return True

    def getIP(self, options=[], aPrompt="H@CK/>"):
        bPrompt= 'Use the format 127.0.0.1 or 127.0.0.0\32'
        self.getValidInput(lambda x: self.validateIP(x) or x in options , remedialPrompt=bPrompt)

    def getOption(self, options=[], aPrompt="H@CK/>"):
        count=0 #use to implement a display option
        fPrompt=aPrompt+': '
        temp=self.getInput(fPrompt).lower()
        if temp in self.thesarus: temp=self.thesarus[temp]
        while temp not in options:
            count+=1
            self.display("Invalid Input"),
            if count>=5:
                self.display('Your options are:')
                for o in options:
                    self.display(o)
                count=0
            temp=self.getInput(fPrompt)
            if temp in self.thesarus: temp=self.thesarus[temp]
        return temp
    
def test(): 
   def tester(someIn):
       return someIn=="True" 
   standard = Interface() 
   standard.getValidInput("Enter true", tester) 


class nmap(object):

    def __init__(self, toolPath='.\\nmap-7.40', logPath='.\\Logs'):
        #Default State
        self.noIpSet=True
        self.running=True
        
        #Default Values
        self.targetIP='127.0.0.1'
        self.optSet=['scan']
        self.optSetting={'scan':'-sS'}

        #File Paths
        self.pathToNmap= toolPath
        self.errorLog=logPath+'\\error.log'
        self.outputLog=logPath+'\\output.log'
        self.cmdLog=logPath+'\\cmd.log'

        
        #PreDefined Globals
        self.topMenu=['execute', 'setTarget']
        self.minMenu=['exit', 'help', 'display']
        self.menu={'help': self.listOptions, 'execute': self.stage, 'stage': self.stage, 'exit':self.backUp, 'setTarget': self.setIP}
        self.menu['display']=self.showOutput
        self.interface=Interface()
        self.dPrompt="What would you like to do next?"
                
    def runOpt(self, anOpt):
        #print "running "+anOpt+" with", self.menu[anOpt]
        self.menu[anOpt]()

    def buildCmd(self):
        cmd=self.pathToNmap+'\\nmap'
        for option in self.optSet: cmd=cmd+' '+self.optSetting[option]
        return cmd+' '+self.targetIP

    def backUp(self):
        if self.Top: self.running=False
        self.curMenu=self.topMenu+self.minMenu
        self.prompt=self.dPrompt
        self.menuCMD=self.menu
        self.Top=True
        self.interface.display(self.dPrompt)

    def showOutput(self):
        op=open(self.outputLog, 'r')
        self.interface.display(op.read())
        op.close()
        
    def listOptions(self):
        self.interface.display("Your options are:")
        for option in self.curMenu:
            self.interface.display(option)

    def setIP(self):
        userChoice=self.interface.getIP(options=self.minMenu, aPrompt="IP")
        if userChoice in self.minMenu: runOpt(userChoice)
        else:
            self.TargetIP=userChoice
            self.noIpSet=False

    def stage(self):
        self.Top=False
        if self.noIpSet:
            self.interface.display("You must set your IP first")
            self.setIP()
        else:
            yes=['yes','execute']
            what=['what command']
            no=['no','exit']
            options=yes+what+no
            choice=self.interface.getOption(options, "Are you sure you want to execute this command?")
            if choice in yes: self.execute()
            else: self.backUp
        
    def readCommand(self):
        command ='scan '
        for i in self.option in self.optSet: command+' '+i+' '+self.optSetting[i]
        return command
    
    def execute(self):
            self.l=open(self.errorLog, 'a')
            self.o=open(self.outputLog, 'w')
            self.c=open(self.cmdLog, 'a')
            cmd=self.buildCmd()
            self.c.write(cmd+'\n')
            self.interface.display('dropping cyb3r nuk3s on'+self.targetIP)
            subprocess.call(cmd, stdout=self.o, stderr=self.l)
            self.interface.display('bombing run complete. RTB')
            self.l.close()
            self.o.close()
            self.c.close()
            self.backUp()
    def run(self):
        self.Top=True
	self.curMenu=self.topMenu+self.minMenu
        self.menuCMD=self.menu
        prompt=self.dPrompt
        self.interface.display("Cyb3r Nuk3s.")
	while self.running:
		uInput=self.interface.getOption(self.curMenu)
		self.runOpt(uInput)

	self.interface.display('Goodbye...')



tool=nmap()
tool.run()

inter= Interface()
    
