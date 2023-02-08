import PySimpleGUI as sg
sg.theme('DarkAmber')
import keyboard
import mouse
from threading import Thread

savedTextsList = []
savedTextsDict = {}

modifiers = ['ctrl', 'shift', 'alt']
keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Gui:
	def __init__(self):
		self.loadOrSaveData()
		self.mainWin()
		self.newWin()
		self.mainWin = sg.Window('Copied Texty', self.mainWin_layout,
 			finalize = True)
	def loadOrSaveData(self, newEntry = []):
		if newEntry:
			print('saving')
			f = open('CopiedTextyData.csv', 'a+')
			lenOfFile = len(f.readlines())
			f.write(newEntry)
			newText = f.read()
			f.close()
			newEntry = newEntry.split()[0].split(',')
			savedTextsDict[newEntry[0]] = newEntry[1]
			self.mainWin['__textEntry__'].update(savedTextsDict.values())
			self.newWin.close()
		f = open('CopiedTextyData.csv', 'r')
		for lines in f:
			if ',' in lines:
				savedTextIndex = lines.split(',')[0]
				savedTextData = lines.split(',')[1]
				print(savedTextIndex, savedTextData)
				savedTextsDict[savedTextIndex] = savedTextData 
	def mainWin(self):
		tab1_layout = [[
			sg.Text('Texty'),
			sg.Text('Hotkey', p=((80,0),(0,0))),
		],[
			sg.Listbox(savedTextsDict.values(),
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
			#print(listValue)
			print(i[0], listValue)
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
	def mainLoop(self):
		while True:
			mainWin_event, mainWin_values = self.mainWin.read() 
			if mainWin_event == sg.WIN_CLOSED:
				break
			if mainWin_event == '__New__':
				self.createNewWindow()
				newWin_event, newWin_values = self.newWin.read() 
				if newWin_event == '__Save__':
					self.loadOrSaveData(str(len(savedTextsDict)+1) + "," + newWin_values['__multiLine__'] + "," + newWin_values['__mod1__'] + "," + newWin_values['__mod2__'] + "," + newWin_values['__hotKey__'] + "\n")
			if mainWin_event == '__Edit__':
				self.editWin(mainWin_values)

def main():
	myWin = Gui()
	myWin.mainLoop()

if __name__ == "__main__":
	main()

