import npyscreen
import curses


class MainForm(npyscreen.Form):
  def afterEditing(self):
    self.parentApp.setNextForm(None)
    #here is where we would store all the information about the values selected/input
    #build the string or whatever, and then store it, and then run it against the honeypot

  def create(self):
    y, x = self.useable_space()
    #create the honeypot form
    obj = self.add(npyscreen.MultiLineEditableBoxed, name="Honeypot",
            custom_highlighting=True, scroll_exit = True, values=["IP: ", "Port: ", "Type: "],
            max_width=x // 2 - 5)

    #read in the config file for the service list
    #MOVE THIS INTO ITS OWN FUNCTION
    f=open("config/services.csv", "r")
    services =f.read().split(",")

    #add the list of services, using the service object
    self.add(Services, name="Services", footer="footer", values = services, scroll_exit = True,
            relx=x // 2, rely=2)

#Object that holds all our service selections - when edited, switch it to the PCAP form associated
#with the selected service. (check the mapping and populate based on that)
class Services(npyscreen.BoxTitle):
  _contained_widget = npyscreen.MultiSelect #defining this box as a multiselect

  #whenever we edit one of the selections - switch to the PCAP form
  #currently broken - unsure why
  def when_value_edited(self):
      #fix
      npyscreen.NPSAppManaged.switchForm('PCAP')

#The form that will display all the attacks associated with the service it is called from
class PcapForm(npyscreen.Form):
  #currently filled w dummy code
  def afterEditing(self):
      self.parentApp.setNextForm(MainForm)

  def create(self):
     self.myName        = self.add(npyscreen.TitleText, name='Name')
     self.myDepartment  = self.add(npyscreen.TitleMultiSelect, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
     self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Employed')


#Parent Class that controls the application with form data, etc
class Primer(npyscreen.NPSAppManaged):
  def onStart(self):
    #add the forms we need
    self.addForm('MAIN', MainForm, name='Primer')
    self.addForm('PCAP', PcapForm, name='PCAP List')

#running the app
if __name__ == '__main__':
 PrimerApp = Primer().run()
