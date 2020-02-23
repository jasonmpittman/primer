import npyscreen

class MainForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
      """
      y, x = self.useable_space()
      self.myName        = self.add(npyscreen.TitleText, name='Name')
      self.myDepartment  = self.add(npyscreen.TitleMultiSelect, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
      
      obj = self.add(npyscreen.BoxTitle, name="BoxTitle",
            custom_highlighting=True, scroll_exit = True, values=["first line", "second line"],
            rely=y // 3, max_width=x // 2 - 5, max_height=y // 1)
      """
      y, x = self.useable_space()
      obj = self.add(npyscreen.BoxTitle, name="BoxTitle",
              custom_highlighting=True, values=["first line", "second line"],
              rely=y // 4, max_width=x // 2 - 5, max_height=y // 2)
      self.add(InputBox, name="Boxed MultiLineEdit", footer="footer",
              relx=x // 2, rely=2)

      #pcap = PcapForm.create(self)
      #obj = self.add(pcap)

class InputBox(npyscreen.BoxTitle):
    # MultiLineEdit now will be surrounded by boxing
    _contained_widget = npyscreen.MultiLineEdit

class PcapForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
       self.myName        = self.add(npyscreen.TitleText, name='Name')
       self.myDepartment  = self.add(npyscreen.TitleMultiSelect, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
       self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Employed')


class Primer(npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', MainForm, name='Primer')
       #self.addForm('PCAP ADD', PcapForm, name='PCAP List')
       # A real application might define more forms here.......

if __name__ == '__main__':
   PrimerApp = Primer().run()