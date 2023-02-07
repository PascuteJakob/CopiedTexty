import PySimpleGUI as sg
sg.theme('DarkAmber')
import keyboard
import mouse
from threading import Thread

savedTexts = []
f = open('CopiedTextyData.csv', 'r')
for lines in f:
	savedTexts.append(lines.split(',')[0])
print(savedTexts)
modifiers = ['ctrl', 'shift', 'alt']
keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Gui:
	def __init__(self):
		self.mainWin()
		self.newWin()
		self.mainWin = sg.Window('Copied Texty', self.mainWin_layout,
 			finalize = True) 
	def mainWin(self):
		tab1_layout = [[
			sg.Text('Texty'),
			sg.Text('Hotkey', p=((80,0),(0,0))),
		],[
			sg.Listbox(savedTexts,
			default_values = None,
			size=(24,10),
			key='__textEntry__'),
			
		],[
			sg.Button('New', s=(6,1),p=((5,4),(0,0)), key='__New__'),
			sg.Button('Edit', s=(6,1), key='__Edit__'),
			sg.Button('Delete', s=(6,1), key='__Delete__')
		]]
		tab2_layout = [[
			sg.Text('My Second tab.'),
			sg.Text('poop'),
		]]
		tab3_layout = [[
			sg.Text('My Second tab.'),
			sg.Text('poop'),
		]]

		layout_tabgroup = [[
			sg.Tab('CopiedTexty', tab1_layout),
			sg.Tab('Settings', tab2_layout),
			sg.Tab('About', tab3_layout)
		]]

		self.mainWin_layout = [[
			sg.TabGroup(
				layout_tabgroup,
				)
		]]

	def newWin(self):
		self.newWin_layout = [[
			sg.Multiline('Input your new Texty here', s=(37,10), key=('__multiLine__')),
		],[
			sg.Text('Hotkey Combo'),
			sg.Combo(modifiers, s=(5,0), key=('__mod1__')),
			sg.Combo(modifiers, s=(5,0), key=('__mod2__')),
			sg.Combo(keys, s=(5,0), key=('__hotKey__')),
		],[
			sg.Button(button_text = "Save", key='__Save__')
		]]
<<<<<<< Updated upstream

=======
	def editWin(self, values):
		lines = []
		f = open('CopiedTextyData.csv', 'r')
		for x in f:
			lines.append(x.split(','))
		f.close()
		print('starting other loop')
		lineCounter = 0
		for i in lines:
			listValue = values['__textEntry__'][0]
			if i[0] == listValue:
				modOne = i[1]
				modTwo = i[2]
				hotkey = i[3]
				print(lineCounter)
			lineCounter += 1
	def createNewWindow(self):
		self.mainWinLocation = self.mainWin.CurrentLocation()
		print(self.mainWinLocation)
		self.newWin = sg.Window('Add Entry', self.newWin_layout,
			location=(self.mainWinLocation[0]+228,self.mainWinLocation[1]), finalize=True,)
		print('created window')
>>>>>>> Stashed changes
	def mainLoop(self):
		while True:
			mainWin_event, mainWin_values = self.mainWin.read() 
			if mainWin_event == sg.WIN_CLOSED:
				break
			if mainWin_event == '__New__':
				self.createNewWindow()
				newWin_event, newWin_values = self.newWin.read() 
				if newWin_event == '__Save__':
					print('saving')
					f = open('CopiedTextyData.csv', 'a+')
					f.write(newWin_values['__multiLine__'] + "," + newWin_values['__mod1__'] + "," + newWin_values['__mod2__'] + "," + newWin_values['__hotKey__'] + "\n")
					newText = f.read()
					f.close()
					savedTexts.append(newWin_values['__multiLine__'] + "\n")
					self.mainWin['__textEntry__'].update(savedTexts)
					self.newWin.close()

def main():
	myWin = Gui()
	myWin.mainLoop()

if __name__ == "__main__":
	main()

