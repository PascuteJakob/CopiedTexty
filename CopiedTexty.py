import PySimpleGUI as sg
import keyboard
import mouse
from threading import Thread
  
savedTexts = ["test", "test2", "test3"]

class Gui:
	def __init__(self):
		self.mainWin()
		self.window = sg.Window('Copied Texty', self.layout) 
	def mainWin(self):
		sg.theme('DarkAmber')
		tab1_layout = [[
			sg.Text('Texty'),
			sg.Text('Hotkey', p=((80,0),(0,0))),
		],[
			sg.Listbox(savedTexts,
			default_values = "No saved texts",
			size=(24,10),
			key='__textEntry__'),
			
		],[
			sg.Button('New', s=(6,1),p=((5,4),(0,0))),
			sg.Button('Edit', s=(6,1)),
			sg.Button('Delete', s=(6,1))
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

		self.layout = [[
			sg.TabGroup(
				layout_tabgroup,
				)
		]]

	def mainLoop(self):
		while True:
			event, values = self.window.read() 
			if event == sg.WIN_CLOSED:
				break

def main():
	myWin = Gui()
	myWin.mainLoop()

if __name__ == "__main__":
	main()

