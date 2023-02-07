import PySimpleGUI as sg
import keyboard
import mouse
from threading import Thread
    
def GuiFunc():
	tab1_layout = [[sg.Text('My first tab.'), sg.Text('poop')]]    

	tab2_layout = [[sg.Text('My Second tab.'), sg.Text('poop')]]

	layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('tab 2', tab2_layout, tooltip='tip2')]])]]
	
	window = sg.Window('Window Title', layout)    

	while True:
		event, values = window.read() 
		if event == sg.WIN_CLOSED:
			break



if __name__ == "__main__":
	GuiFunc()

