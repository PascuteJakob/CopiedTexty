import PySimpleGUI as sg
import keyboard
import mouse
import fileinput
import threading
import time
import atexit
import autoit

defaultTheme = 'DarkAmber'
file = open('SelectedTheme.csv', 'r')
SelectedTheme = file.read()
file.close()
if SelectedTheme == "":
	sg.theme(defaultTheme)
else:
	sg.theme(SelectedTheme)

theme_name_list = sg.theme_list()
savedTextsList = []
savedTextsDict = {}
savedHotkeysDict = {}

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
	def mainWin(self):
		tab1_layout = [[
			sg.Text('Texty'),
			sg.Text('Hotkey', p=((80,0),(0,0))),
		],[
			sg.Listbox(list(savedTextsDict.values()),
			default_values = None,
			size=(17,10),
			key='__listBox__',
			enable_events = True,
			no_scrollbar = True,
			p=((5,0),(0,0)),),			
			sg.Listbox(list(savedHotkeysDict.values()),
			default_values = None,
			size=(9,10),
			key='__hotkeyListbox__',
			enable_events = True,
			no_scrollbar = True,
			p=((0,0),(0,0)),),
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
			sg.Input(default_text = 'My new Texty', s=(37,0), key=('__nameInput__')),
		],[
			sg.Multiline('Input your new Texty here', s=(37,10), key=('__multiLine__')),
		],[
			sg.Text('Hotkey Combo'),
			sg.Combo(modifiers, s=(5,0), key=('__mod1__'), default_value ="ctrl",),
			sg.Combo(modifiers, s=(5,0), key=('__mod2__'), default_value = "shift",),
			sg.Combo(keys, s=(5,0), key=('__hotKey__'), default_value="0",),
		],[
			sg.Button(button_text = "Save", key='__Save__')
		]]
		return newWin_layout

	def edit(self, values):
		lines = []
		file = open('CopiedTextyData.csv', 'r')
		for line in file:
			lines.append(line)
		file.close()
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
	def loadOrSaveData(self, newWin = None, editWin = None, entry = []):
			if newWin:
				print('saving')
				file = open('CopiedTextyData.csv', 'r')
				lines = file.readlines()
				print(lines)
				lenOfLines = len(lines)
				file.close()
				file = open('CopiedTextyData.csv', 'a')
				data = entry.split(',')
				newEntry = []
				for item in data:
					if item == data[0]:
						continue
					else:
						item = item.replace("\n", '<return>')
						newEntry.append("," + item)
				newEntry = "".join(newEntry)
				file.write(str(lenOfLines) + newEntry + '\n')
				#newText = file.read()
				file.close()
				file = open('CopiedTextyData.csv', 'r')
				lines = file.readlines()
				newDict = {}
				newHotkeyDict = {}
				for line in lines:
					line = line.split(',')
					newDict[line[0]] = line[5].replace('\n', '')
					savedModOne = line[2]
					savedModTwo = line[3]
					savedHotkey = line[4]
					hotkeyData = [savedModOne, savedModTwo, savedHotkey]
					newHotkeyDict[line[0]] = hotkeyData
				print('-------------------')
				print(newDict)
				print('-------------------')
				self.mainWin['__listBox__'].update(newDict.values())
				self.mainWin['__hotkeyListbox__'].update(newHotkeyDict.values())
				newWin.close()
			
			if editWin:
				print('saving')
				file = open('CopiedTextyData.csv', 'r')
				lines = file.readlines()
				lines[int(entry[0])] = entry
				file.close()
				file = open('CopiedTextyData.csv', 'w')
				for line in lines:
					if '\n' in line:
						pass
					else:
						line += '\n'
					file.write(line)
				file.close()
				newHotkeyDict = {}
				entry = entry.split(',')
				savedTextsDict[entry[0]] = entry[5]
				savedModOne = entry[2]
				savedModTwo = entry[3]
				savedHotkey = entry[4]
				hotkeyData = [savedModOne, savedModTwo, savedHotkey]
				savedHotkeysDict[entry[0]] = hotkeyData
				self.mainWin['__listBox__'].update(savedTextsDict.values())
				self.mainWin['__hotkeyListbox__'].update(savedHotkeysDict.values())
				editWin.close()

			file = open('CopiedTextyData.csv', 'r')
			lines = file.readlines()
			hotkeyListenerData = {}
			for line in lines:
				if ',' in line:
					savedTextIndex = line.split(',')[0]
					savedTextData = line.split(',')[1]
					savedTextName = line.split(',')[5]
					savedModOne = line.split(',')[2]
					savedModTwo = line.split(',')[3]
					savedHotkey = line.split(',')[4]
					hotkeyData = [savedModOne, savedModTwo, savedHotkey]
					hotkeyListenerData[savedTextIndex] = [savedTextData, savedModOne, savedModTwo, savedHotkey]
					dataForDict = savedTextData[0]
					#print(savedTextIndex, savedTextData)
					savedTextsDict[savedTextIndex] = savedTextName
					savedHotkeysDict[savedTextIndex] = hotkeyData
			file.close()
			keyboard.unhook_all_hotkeys()
			hotkeyListener(hotkeyListenerData)

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
						+ newWin_values['__mod1__'] + "," + newWin_values['__mod2__'] + "," + newWin_values['__hotKey__'] + "," + newWin_values['__nameInput__'])
			if mainWin_event == '__Edit__':
				self.edit(mainWin_values)
				index = self.mainWin['__listBox__'].get_indexes()[0]
				file = open('CopiedTextyData.csv', 'r')

				linesSplit = file.readlines()[index].split(',')
				file.close()
				texty = linesSplit[1]
				modOne = linesSplit[2]
				modTwo = linesSplit[3]
				hotkey = linesSplit[4]
				name = linesSplit[5]
				#print(texty, modOne, modTwo, hotkey)
				editWindow = self.createNewWindow()
				editWindow['__multiLine__'].update(value=texty)
				editWindow['__mod1__'].update(value=modOne)
				editWindow['__mod2__'].update(value=modTwo)
				editWindow['__hotKey__'].update(value=hotkey)
				editWindow['__nameInput__'].update(value=name)
				editWindow_event, editWindow_values = editWindow.read()
				if editWindow_event == '__Save__':
					editedEntry = str(str(index) + "," + editWindow_values['__multiLine__'].replace('\n', '<newline>').replace(',', '<comma>') + "," 
					+ editWindow_values['__mod1__'] + "," + editWindow_values['__mod2__']
					+ "," + editWindow_values['__hotKey__'] + ","
					+ editWindow_values['__nameInput__'])
					self.loadOrSaveData(None, editWindow, editedEntry)
			if mainWin_event == '__Delete__':
				index = self.mainWin['__listBox__'].get_indexes()[0]
				savedTextsDict[str(index)] = ""
				counter = 0
				newDict = {}
				for value in savedTextsDict.values():
					if value == "":
						continue
					elif value == "id":
						pass
					else:
						newDict[counter] = value
					counter+=1
				print(newDict)
				#del savedTextsDict[str(counter)]
				self.mainWin['__listBox__'].update(newDict.values())
				file = open('CopiedTextyData.csv', 'r')
				lines = file.readlines()
				file.close()
				file = open('CopiedTextyData.csv', 'w')
				counter = 0
				#file.write(lines[0])
				hotkeyListenerData = {}
				hotkeyListboxData = {}
				for line in lines:
					lineSplit = line.split(',')
					if lineSplit[0] == str(index):
						#print(savedTextsDict["2"])
						#del savedTextsDict[str(index)]
						#print(savedTextsDict)
						continue
					else:
						hotkeyListboxData[lineSplit[0]] = [lineSplit[2], lineSplit[3], lineSplit[4]]
						hotkeyListenerData[lineSplit[0]] = [lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4]]
						del lineSplit[0] 
						file.write(str(counter) + ',' + ','.join(lineSplit))
						counter += 1
				file.close()
				#print(newDict)
				self.mainWin['__hotkeyListbox__'].update(hotkeyListboxData.values())
				keyboard.unhook_all_hotkeys()
				#print(hotkeyListener)
				hotkeyListener(hotkeyListenerData)
			if mainWin_event == '__listBox__':
				print('working')
				index = self.mainWin['__listBox__'].get_indexes()[0]
				self.mainWin['__hotkeyListbox__'].update(set_to_index=[index],scroll_to_index=index)
			if mainWin_event == '__theme__':
				newTheme = mainWin_values['__theme__'][0]
				sg.theme(newTheme)
				file = open('SelectedTheme.csv', 'w')
				file.write(newTheme)
				file.close()
				self.mainWin.close()
				main()
def hotkeyListener(myDict):
	#print(myDict)
	#print(myDict)
	for entry in myDict:
		entry = myDict[entry]
		#keyboard.add_hotkey(entry[1] + "+" + entry[2] + "+" + entry[3], keyboard.write("entry[0]"))
		keyboard.add_hotkey(entry[1] + "+" + entry[2] + "+" + entry[3], keyboardWrite, args=[entry[0]], timeout=1,suppress=True)
	#keyboard.add_hotkey("")
def keyboardWrite(text):
	oldClip = autoit.clip_get()
	newClipText = text.replace("<newline>", "\n")
	newClipText = newClipText.replace("<comma>", ",")
	#time.sleep(1)
	autoit.clip_put(newClipText)
	autoit.send("^v")
	autoit.clip_put(oldClip)
	#time.sleep(5)

def main():
	dictForThread = {}
	file = open("CopiedTextyData.csv", "r")
	lines = file.readlines()
	file.close()
	for line in lines:
		lineSplit = line.split(',')
		dictForThread[lineSplit[0]] = lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4]
	#print(dictForThread["0"])
	hotkeyListener(dictForThread)
	myWin = Gui()
	myWin.mainLoop()
def exit_handler():
    keyboard.unhook_all_hotkeys()
if __name__ == "__main__":
	atexit.register(exit_handler)
	main()


