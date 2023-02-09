import PySimpleGUI as sg
import keyboard
import mouse
import fileinput

defaultTheme = 'DarkAmber'
f = open('SelectedTheme.csv', 'r')
SelectedTheme = f.read()
f.close()
if SelectedTheme == "":
	sg.theme(defaultTheme)
else:
	sg.theme(SelectedTheme)

theme_name_list = sg.theme_list()
savedTextsList = []
savedTextsDict = {}

modifiers = ['ctrl', 'shift', 'alt']
keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
########################################
#WARNING WARNING WARNING WARNING WARNING
# GUI STARTS HERE YOU HAVE BEEN WARNED
#WARNING WARNING WARNING WARNING WARNING
########################################
class Gui:
	def __init__(self):
		self.loadOrSaveData()
		self.mainWin()
		self.newWin()
		self.mainWin = sg.Window('Copied Texty', self.mainWin_layout,)
	def loadOrSaveData(self, newWin = None, editWin = None, entry = []):
		if newWin:
			print('saving')
			f = open('CopiedTextyData.csv', 'a+')
			lenOfFile = len(f.readlines())
			f.write(entry + '\n')
			newText = f.read()
			f.close()
			entry = entry.split(',')
			savedTextsDict[entry[0]] = entry[1]
			self.mainWin['__listBox__'].update(savedTextsDict.values())
			newWin.close()
		
		if editWin:
			print('saving')
			f = open('CopiedTextyData.csv', 'r')
			data = f.readlines()
			data[int(entry[0])] = entry
			print(''.join(data))
			f.close()
			f = open('CopiedTextyData.csv', 'w')
			f.write(' '.join(data))
			f.close()
			entry = entry.split(',')
			savedTextsDict[entry[0]] = entry[1]
			self.mainWin['__listBox__'].update(savedTextsDict.values())
			editWin.close()

		f = open('CopiedTextyData.csv', 'r')
		for lines in f:
			if ',' in lines:
				savedTextIndex = lines.split(',')[0]
				savedTextData = lines.split(',')[1]
				dataForDict = savedTextData[0]
				#print(savedTextIndex, savedTextData)
				savedTextsDict[savedTextIndex] = savedTextData 
				print(savedTextsDict)
	def mainWin(self):
		tab1_layout = [[
			sg.Text('Texty'),
			sg.Text('Hotkey', p=((80,0),(0,0))),
		],[
			sg.Listbox(list(savedTextsDict.values()),
			default_values = None,
			size=(24,10),
			key='__listBox__',
			enable_events = True,),
			
		],[
			sg.Button('New', s=(6,1),p=((5,4),(0,0)), key='__New__'),
			sg.Button('Edit', s=(6,1), key='__Edit__'),
			sg.Button('Delete', s=(6,1), key='__Delete__')
		]]
		tab2_layout = [[
			sg.Text('Theme Selector', p=((0,0),(0,190))),
			sg.Listbox(theme_name_list, s=(10,12), key="__theme__", enable_events=True)
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
				),
		]]

	def newWin(self, values = []):
		newWin_layout = [[
			sg.Multiline('Input your new Texty here', s=(37,10), key=('__multiLine__')),
		],[
			sg.Text('Hotkey Combo'),
			sg.Combo(modifiers, s=(5,0), key=('__mod1__')),
			sg.Combo(modifiers, s=(5,0), key=('__mod2__')),
			sg.Combo(keys, s=(5,0), key=('__hotKey__')),
		],[
			sg.Button(button_text = "Save", key='__Save__')
		]]
		return newWin_layout

	def edit(self, values):
		lines = []
		f = open('CopiedTextyData.csv', 'r')
		for x in f:
			lines.append(x)
		f.close()
		selectedValue = values['__listBox__']
		return selectedValue

	def createNewWindow(self):
		mainWinLocation = self.mainWin.CurrentLocation()
		print(mainWinLocation)
		newWin = sg.Window('Add Entry', self.newWin(),
			location=(mainWinLocation[0]+228,mainWinLocation[1]), finalize=True,)
		print('created window')
		return newWin
########################################
#WARNING WARNING WARNING WARNING WARNING
# THIS SHOULD BE THE END OF GUI CODE
#WARNING WARNING WARNING WARNING WARNING
########################################
	def mainLoop(self):
		while True:
			mainWin_event, mainWin_values = self.mainWin.read() 
			if mainWin_event == sg.WIN_CLOSED:
				break
			if mainWin_event == '__New__':
				newWin = self.createNewWindow()
				newWin_event, newWin_values = newWin.read() 
				if newWin_event == '__Save__':
					self.loadOrSaveData(newWin, None, str(len(savedTextsDict)) + "," + newWin_values['__multiLine__'] + "," 
						+ newWin_values['__mod1__'] + "," + newWin_values['__mod2__'] + "," + newWin_values['__hotKey__'])
			if mainWin_event == '__Edit__':
				self.edit(mainWin_values)
				index = self.mainWin['__listBox__'].get_indexes()[0]
				f = open('CopiedTextyData.csv', 'r')

				data = f.readlines()[index].split(',')
				texty = data[1]
				modOne = data[2]
				modTwo = data[3]
				hotkey = data[4]
				print(texty, modOne, modTwo, hotkey)
				editWindow = self.createNewWindow()
				editWindow['__multiLine__'].update(value=texty)
				editWindow['__mod1__'].update(value=modOne)
				editWindow['__mod2__'].update(value=modTwo)
				editWindow['__hotKey__'].update(value=hotkey)
				editWindow_event, editWindow_values = editWindow.read()
				if editWindow_event == '__Save__':
					self.loadOrSaveData(None, editWindow, str(index) + "," + editWindow_values['__multiLine__'] + "," 
						+ editWindow_values['__mod1__'] + "," + editWindow_values['__mod2__'] + "," + editWindow_values['__hotKey__'])
			if mainWin_event == '__theme__':
				newTheme = mainWin_values['__theme__'][0]
				sg.theme(newTheme)
				f = open('SelectedTheme.csv', 'w')
				f.write(newTheme)
				f.close()
				self.mainWin.close()
				main()



def main():
	myWin = Gui()
	myWin.mainLoop()

if __name__ == "__main__":
	main()

