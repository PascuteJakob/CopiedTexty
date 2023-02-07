import PySimpleGUI as sg
import keyboard
import mouse
from threading import Thread
    
def GuiFunc():
	sg.theme('DarkAmber')

	tab1_layout = [[
		sg.Text('My first tab.'),
		sg.Text('poop'),
	]]    
	tab2_layout = [[
		sg.Text('My Second tab.'),
		sg.Text('poop'),
	]]

	layout_tabgroup = [[
		sg.Tab('CopiedTexty', tab1_layout, tooltip='tip'),
		sg.Tab('Hotkeys', tab2_layout, tooltip='tip2'),
	]]

	layout = [[
		sg.TabGroup(
			layout_tabgroup,
			)
	]]
	window = sg.Window('Window Title', layout)    

	while True:
		event, values = window.read() 
		if event == sg.WIN_CLOSED:
			break



if __name__ == "__main__":
	GuiFunc()

