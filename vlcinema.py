import tkinter as tk
from tkinter import ttk

from subprocess import check_output

class VLCinema():
	
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('VLCinema')
		self.root.geometry('600x800+50+100')
		
		message = ttk.Label(
			self.root,
			text = 'My IP is '+self.get_local_ip()
		)
		message.pack()
		
		start_button = ttk.Button(
			self.root,
			text = 'Start'
		)
		start_button.bind(
			'<Button>',
			self.on_start_button_click
		)
		start_button.pack()

	def get_local_ip(self):
		return check_output(
			'hostname -I',
			shell = True
		).decode(
			'ascii'
		).split(' ')[0]
		
	def on_start_button_click(self, event):
		if event.num == 1:
			self.run_cvlc()
	
	def run(self):
		self.root.mainloop()
		
	def run_cvlc(self):
		print('Run CVLC...')
		
	def set_title(self, title):
		self.root.title(title)



if __name__=='__main__':
	vlcinema = VLCinema()
	vlcinema.set_title('*** TEST ***')
	vlcinema.run()
