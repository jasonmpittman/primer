import npyscreen
import curses
import os


class MainForm(npyscreen.FormWithMenus):

  def afterEditing(self):
    #store values of the form
    self.parentApp.selectedServices = self.serviceBox.get_selected_objects()     
    self.parentApp.honeypotInfo = self.honeypotInfoBox.values
  #  f = open("demofile2.txt", "a")
  #  f.write(str(self.serviceBox.get_selected_objects()))
  #  f.write(str(self.honeypotInfoBox.values))
  #  f.close()
    #here is where we would store all the information about the values selected/input
    #build the string or whatever, and then store it, and then run it against the honeypot
    self.parentApp.setNextForm('PCAP')

  def create(self):
    y, x = self.useable_space()
    #create the honeypot form
    self.honeypotInfoBox = self.add(npyscreen.MultiLineEditableBoxed, name="Honeypot",
            custom_highlighting=True, scroll_exit = True, values=["IP: ", "Port: ", "Type: "],
            max_width=x // 2 - 5)
    #add the list of services, using the service object
    self.serviceBox = self.add(npyscreen.MultiSelect, name="Services", footer="footer", values = self.parentApp.services, scroll_exit = True,
            relx=x // 2, rely=2)  


#The form that will display all the attacks associated with the service it is called from
class PcapForm(npyscreen.Form):
  #currently filled w dummy code
  def afterEditing(self):
    self.parentApp.setNextForm(None)

  def beforeEditing(self):
    for i in self.parentApp.selectedServices:
      f = open("demofile2.txt", "a")
      f.write(str(i))
      f.write(str(self.parentApp.d.get(i)))
      
      #go through all the selected services
      #get the selected service from the map
      self.add(npyscreen.TitleText, name=i)
      f.write("Title Text Created\n")
      self.add(npyscreen.MultiSelect, name="Services", footer="footer", values = self.parentApp.d.get(i), scroll_exit = True)  
      f.write("MultiSelect Created\n")
      f.close()
    """
    self.selectedServices = self.parentApp.selectedServices
    self.dict = self.parentApp.d
    for i in self.selectedServices:
      #go through all the selected services
      #get the selected service from the map
      self.add(npyscreen.TitleText, name=i)
      self.add(npyscreen.MultiSelect, name="Services", footer="footer", values = self.dict.get(i), scroll_exit = True,
            relx=x // 2, rely=2)  
      f = open("demofile2.txt", "a")
      f.write(str(i))
      f.write(str(self.dict.get(i)))
      f.close()

    """
    return

  def create(self):



    self.myName        = self.add(npyscreen.TitleText, name='Name')
    self.myDepartment  = self.add(npyscreen.TitleMultiSelect, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
    self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Employed')


#The form that will display the pcaps selected as well as the ip address entered
class RunForm(npyscreen.Form):
  def afterEditing(self):
    self.parentApp.setNextForm(PcapForm)

  def beforeEditing(self):
    #hgffgh
    return
  
  def create(self):

    return

#Parent Class that controls the application with form data, etc
class Primer(npyscreen.NPSAppManaged):
  selectedServices = []
  honeypotIP, pcaps = None, None
  #read in the config file for the service list
  #MOVE THIS INTO ITS OWN FUNCTION
  f = open("config/services.csv", "r")
  services = f.read().split(",")
  
  pcaps = os.listdir(path='pcap/')

  #Mapping to service -> pcap
  d =  {
  "service": ["example.pcap"]
  }
  d.clear()
  f = open("config/mapping.csv", "r")
  mappings = f.read().split("\n")

  #Adding the dictionary Key (Service) to Values (Array of pcaps)
  for y in mappings:
    x = y.split(",")
    d.update( {x[0] : x[1::]} )


  def onStart(self):
    #add the forms we need
    self.addForm('MAIN', MainForm, name='PRIMER')
    self.addForm('PCAP', PcapForm, name='PCAP')
    #self.addForm('RUN', RunForm, name = 'RUN')


#running the app
if __name__ == '__main__':
 PrimerApp = Primer().run()

