import PySimpleGUI as sg
sg.theme('DarkAmber')
import keyboard
import mouse
from threading import Thread
  
savedTexts = []

class Gui:
	def __init__(self):
		self.mainWin()
		self.newWin()
		self.mainWin = sg.Window('Copied Texty', self.mainWin_layout,
 			finalize = True) 
		self.mainWinLocation = self.mainWin.CurrentLocation()
		print(self.mainWinLocation)
		self.newWin = sg.Window('Add Entry', self.newWin_layout,
			location=(self.mainWinLocation[0]+228,self.mainWinLocation[1]), finalize=True,)
		self.newWin.Hide()
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
			sg.Text('Input your new Texty here'),
		]]

	def mainLoop(self):
		while True:
			event, values = self.mainWin.read() 
			if event == sg.WIN_CLOSED:
				break
			if event == '__New__':
				self.newWin.UnHide()


def main():
	myWin = Gui()
	myWin.mainLoop()

if __name__ == "__main__":
	main()

