class Interface(object):
  def __init__(self):
    pass

  def display(self, aString):
    print aString
  
  def getInput(self, aPrompt):
    return raw_input(aPrompt)

  def getValidInput(self, aPrompt, validate):
    fPrompt=aPrompt+": "
    temp=self.getInput(fPrompt)
    while not validate(temp):
      self.display("Invalid Input")
      temp=self.getInput(fPrompt)
    return temp
def test():
  def tester(someIn):
    return someIn=="True"
  standard = Interface()
  standard.getValidInput("Enter true", tester)

